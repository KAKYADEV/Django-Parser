from logging import FileHandler

class CustomHandler(FileHandler):
    def emit(self, record):
        super().emit(record)
        self.flush()