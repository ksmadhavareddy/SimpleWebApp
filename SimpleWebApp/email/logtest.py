import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger('logtest')

logger.info('This is info message')
logger.warning('This is warning message')
logger.debug('This is a debug message')
logger.critical('A critical error occurred')

