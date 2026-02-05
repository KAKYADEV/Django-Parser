from celery import shared_task
from parse.services.parser import Parser


@shared_task
def start_background_parse(pk):
    print(f"Задача парсинга запущена для сайта с ID: {pk}")
    parser = Parser(pk)
    parser.run()
    return 'success'
