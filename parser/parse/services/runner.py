import threading
from parse.services.parser import Parser


def run_parse_asynk(pk):
    parser = Parser(pk)
    parser.run()

def start_background_parse(pk):
    thread = threading.Thread(target=run_parse_asynk, args=(pk,), daemon=True)
    thread.start()