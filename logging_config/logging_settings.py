from logging_config.logging_filter import (DebugFilter, InfoFilter, WarningFilter,
                                           ErrorFilter, CriticalFilter)

logging_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '[{asctime}] #{levelname:8} {filename}:'
                      '{lineno} - {name} : {funcName} - {message}',
            'style': '{'
        }
    },
    'filters': {
        'debug_filter': {
            '()': DebugFilter,
        },
        'info_filter': {
            '()': InfoFilter,
        },
        'warning_filter': {
            '()': WarningFilter,
        },
        'error_filter': {
            '()': ErrorFilter,
        },
        'critical_filter': {
            '()': CriticalFilter,
        }
    },
    'handlers': {
        'default': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        },
        'debug_file': {
            'class': 'logging.FileHandler',
            'filename': 'logging_config/debug.log',
            'mode': 'a',
            'encoding': 'utf-8',
            'level': 'DEBUG',
            'formatter': 'default',
            'filters': ['debug_filter']
        },
        'info_file': {
            'class': 'logging.FileHandler',
            'filename': 'logging_config/info.log',
            'mode': 'a',
            'encoding': 'utf-8',
            'level': 'INFO',
            'formatter': 'default',
            'filters': ['info_filter']
        },
        'warning_file': {
            'class': 'logging.FileHandler',
            'filename': 'logging_config/warning.log',
            'mode': 'a',
            'encoding': 'utf-8',
            'level': 'WARNING',
            'formatter': 'default',
            'filters': ['warning_filter']
        },
        'error_file': {
            'class': 'logging.FileHandler',
            'filename': 'logging_config/error.log',
            'mode': 'a',
            'encoding': 'utf-8',
            'level': 'ERROR',
            'formatter': 'default',
            'filters': ['error_filter']
        },
        'critical_file': {
            'class': 'logging.FileHandler',
            'filename': 'logging_config/critical.log',
            'mode': 'a',
            'encoding': 'utf-8',
            'level': 'CRITICAL',
            'formatter': 'default',
            'filters': ['critical_filter']
        }
    },
    'loggers': {
        '__main__': {
            'level': 'DEBUG',
            'handlers': ['default']
        },
        'database.queries.core': {
            'level': 'DEBUG',
            'handlers': ['default']
        }
    },
    'root': {
        'formatter': 'default',
    }
}

