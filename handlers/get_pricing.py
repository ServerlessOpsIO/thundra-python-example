'''get pricing multiple'''

import logging
import json
import os
import random
import time

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


def _random_slowdown():
    '''Add a random slow down to annoy people.'''
    # random slow down.
    if random.randint(1, 100) > 95:
        _logger.info('Hit slowdown...')
        time.sleep(random.randint(3, 8))


def _get_pricing_multiple():
    '''Return pricing multiple.'''
    multiple = 1
    if random.randint(1, 10) > 8:
        multiple = _get_pricing_multiple_discount()
        _logger.info('DISCOUNT: {}'.format(multiple))
    elif random.randint(1, 10) < 3:
        multiple = _get_pricing_multiple_surge()
        _logger.info('SURGE: {}'.format(multiple))
    else:
        _logger.info('STANDARD')

    return multiple


def _get_pricing_multiple_discount():
    '''Return pricing multiple.'''
    return (100 - random.randint(5, 20)) / 100


def _get_pricing_multiple_surge():
    '''Return pricing multiple.'''
    return ((random.randint(1, 10)) / 10) + 1

@thundra
def handler(event, context):
    '''Function entry'''
    _logger.info('This is an info log')
    _logger.debug('This is a debug log')
    _logger.warning('This is a warning log')
    _logger.error('This is an error log')
    _logger.critical('This is a critical log')
    _logger.info('Request: {}'.format(json.dumps(event)))

    _random_slowdown()
    pricing_multiple = _get_pricing_multiple()

    resp_body = {'PricingMultiple': pricing_multiple}

    resp = {
        'statusCode': 201,
        'body': json.dumps(resp_body)
    }
    _logger.info(resp)
    return resp

