from parse.models import *
import time


class Parser:
    def __init__(self, site_id):
        self.site_id = site_id

    def run(self):
        site = ReqSite.objects.get(pk=self.site_id)

        try:
            time.sleep(15)  # Симуляция времени парсинга
            ParsedData.objects.create(
                site=site,
                title=f"Заголовок для {site.name}",
                description=f"Описание для {site.name}",
                keywords=f"ключевые слова для {site.name}"
            )
            print(f"Запущен парсинг сайта: {site.url}")
            # Здесь будет логика парсинга сайта

            site.status = ReqSite.Site.DONE
        except Exception as e:
            site.status = ReqSite.Site.ERROR
            print(f"Ошибка при парсинге сайта {site.url}: {e}")
            raise e
        finally:
            site.save(update_fields=['status'])
            return print("Парсер работает")

        