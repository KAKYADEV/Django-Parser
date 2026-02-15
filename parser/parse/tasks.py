from celery import shared_task
from parse.services.parser import Parser
from parse.models import *
from services.exceptions import *


@shared_task
def start_background_parse(pk):
    print(f"Задача парсинга запущена для сайта с ID: {pk}")

    site = ReqSite.objects.get(pk=pk)
    site.status = ReqSite.Site.PROCESSING
    site.save(update_fields=['status'])

    try:
        parser = Parser(site.url)
        result = parser.run()
    except ParserError as e:
        site.status = ReqSite.Site.ERROR
        site.save(update_fields=['status'])
        print(f'Ошибка {e} при парсинге сайта {site.name}')
    except Exception as e:
        site.status = ReqSite.Site.ERROR
        site.save(update_fields=['status'])
        raise
    else:
        ParsedData.objects.create(
            site = site,
            title = result['title'],
            description = result['description'],
            keywords = result['keywords'],
        )

        site.status = ReqSite.Site.DONE
        site.save(update_fields=['status'])

        return 'success'
