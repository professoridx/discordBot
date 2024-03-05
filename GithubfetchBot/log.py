from logging.config import dictConfig
import logging

LOGGING_CONFIG = {
  "version": 1,
  "disable_existing_loggers": False,
  "formatters": {
    "verbose": {
      "format": "%(asctime)s : %(name)-10s - %(levelname)s -%(module)-15s : %(message)s"
    }
  },
  
  'handlers': {
    "console": {
      "level": "DEBUG",
      "class": "logging.StreamHandler",
      "formatter": "standard"},
    
    "console2": {
      "level": "Warning",
      "class": "logging.StreamHandler",
      "formatter": "standard"},
    
    "file": {
      'level': 'INFO',
      'class': 'logging.FileHandler',
      'filename': 'logs.log',
      'mode': 'w',
      'formatter': 'standard',
      
      },
    
  },
  
  "loggers": {
    "bot": {
      
      'handlers': ['handlers'],
      "level": "INFO",
      "propagate": False,
      'formatter': 'verbose',
      
    },
    "discord": {
      'handlers': ['console2', 'file'],
      'level': 'INFO',
      'propagate': False,
    },
  },
}