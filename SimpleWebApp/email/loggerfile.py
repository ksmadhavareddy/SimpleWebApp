import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%d-%m-%Y %H:%M:%S',
    level=logging.DEBUG,
    filename='logs.txt'
)

logger = logging.getLogger('books')

logger.info('This is info message')
logger.warning('This is warning message')
logger.debug('This is a debug message')
logger.critical('A critical error occurred')

