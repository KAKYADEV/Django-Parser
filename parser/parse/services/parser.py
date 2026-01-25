from parse.models import ReqSite


class Parser:
    def __init__(self, site_id):
        self.site_id = site_id

    def run(self):
        site = ReqSite.objects.get(pk=self.site_id)

        try:
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

        