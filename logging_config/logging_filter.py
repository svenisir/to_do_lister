import logging


class DebugFilter(logging.Filter):
    def filter(self, record):
        return record.levelname == 'DEBUG'


class InfoFilter(logging.Filter):
    def filter(self, record):
        return record.levelname == 'INFO'


class WarningFilter(logging.Filter):
    def filter(self, record):
        return record.levelname == 'WARNING'


class ErrorFilter(logging.Filter):
    def filter(self, record):
        return record.levelname == 'ERROR'


class CriticalFilter(logging.Filter):
    def filter(self, record):
        return record.levelname == 'CRITICAL'
