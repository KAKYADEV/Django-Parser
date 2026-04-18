from celery import shared_task
from parse.services.parser import Parser
from parse.models import *
from .services.exceptions import *
from selenium.common.exceptions import TimeoutException
import logging
from parse.services.seo_analysis import seo_counter, img_storage


tasks_logger = logging.getLogger(__name__)

@shared_task
def start_background_parse(pk):
    site = ReqSite.objects.get(pk=pk)
    site.status = ReqSite.Site.PROCESSING
    site.save(update_fields=['status'])

    tasks_logger.info(f"Задача парсинга запущена для сайта с ID: {pk}")

    try:
        parser = Parser(site.url)
        result = parser.run()
        seo_points = seo_counter(result)
        imgs_prev = img_storage(result, seo_points['imgs_score'])
    except TimeoutException as e:
        site.status = ReqSite.Site.CAPTCHA
        site.save(update_fields=['status'])
        tasks_logger.exception("TimeoutException", exc_info=True)
    except ParserError as e:
        site.status = ReqSite.Site.ERROR
        site.save(update_fields=['status'])
        tasks_logger.exception("ParserError", exc_info=True)
    except Exception as e:
        site.status = ReqSite.Site.ERROR
        site.save(update_fields=['status'])
        tasks_logger.exception(f"{e}", exc_info=True)
        raise
    else:
        ParsedData.objects.create(
            site = site,
            title = result['title'],
            description = result['description'],
            keywords = result['keywords'],
            headers = result['headers'],
            images = result['images'],
            seo_score = seo_points,
            images_preview = imgs_prev,
            headers_overview = seo_points['header_info'][1],
        )

        site.status = ReqSite.Site.DONE
        site.save(update_fields=['status'])
        tasks_logger.info(f"Задача парсинга выполнена для сайта с ID: {pk}")

        return 'success'
