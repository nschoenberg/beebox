import logging
from logging.handlers import RotatingFileHandler

def create_logger():
    log_formatter = logging.Formatter("%(asctime)s %(levelname)s %(funcName)s(%(lineno)d) %(message)s")
    logFile = "log.txt"

    log_handler = RotatingFileHandler(logFile, mode='a', maxBytes=2*1024*1024, backupCount=2, encoding=None, delay=0)
    log_handler.setFormatter(log_formatter)
    log_handler.setLevel(logging.INFO)

    app_log = logging.getLogger('root')
    app_log.setLevel(logging.INFO)
    app_log.addHandler(log_handler)
    return app_log;