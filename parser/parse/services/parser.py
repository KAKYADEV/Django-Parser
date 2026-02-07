import time


class Parser:
    def __init__(self, site_url):
        self.site_url = site_url

    def run(self):

        try:            
            print(f"Запущен парсинг сайта: {self.site_url}")  
            time.sleep(15)  # Здесь будет логика парсинга сайта
           
        except Exception as e:
            #site.status = ReqSite.Site.ERROR
            print(f"Ошибка при парсинге сайта {self.site_url}: {e}")
            raise e
        
        finally:
            return {
                'title': f"{self.site_url}",
                'description': f"Описание для {self.site_url}",
                'keywords': f"Ключевые слова для {self.site_url}",
            }

        