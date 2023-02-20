import logging

from logging import basicConfig

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logformat = '[ %(levelname)s ] - %(asctime)-15s :: %(message)s'
basicConfig(format=logformat)


__all__ = [
    'logger'
]
