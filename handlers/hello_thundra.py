'''test hello'''

import json
import logging
import os

from thundra.thundra_agent import Thundra
from thundra.plugins.trace.traceable import Traceable

THUNDRA_API_KEY = os.environ.get('THUNDRA_API_KEY', '')
thundra = Thundra(api_key=THUNDRA_API_KEY)

from thundra.plugins.log.thundra_log_handler import ThundraLogHandler

log_level = os.environ.get('LOG_LEVEL', 'INFO')
logging.root.setLevel(logging.getLevelName(log_level))  # type:ignore
thundra_handler = ThundraLogHandler()
_logger = logging.getLogger(__name__)
_logger.addHandler(thundra_handler)


@thundra
def handler(event, context):
    '''Function entry'''
    _logger.info('This is an info log')
    _logger.debug('This is a debug log')
    _logger.warning('This is a warning log')
    _logger.error('This is an error log')
    _logger.critical('This is a critical log')
    _logger.info('Request: {}'.format(json.dumps(event)))
    body = {
        'message': 'Hello Thundra!'
    }

    resp = {
        'statusCode': 200,
        'body': json.dumps(body)
    }
    return resp

