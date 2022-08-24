import logging
from rich.logging import RichHandler
from rich.traceback import install
import os


install()

def create_logger(logger_name: str = __name__):
    """

    Args:
        logger_name (str): Logger Name

    Returns:
        logging instance
    """
    loglevel = os.environ.get('LOGLEVEL', 'INFO').upper()
    rich_handler = RichHandler(rich_tracebacks=True, markup=True)
    logging.basicConfig(level=loglevel, format='%(message)s',
                        datefmt="[%d/%b/%Y %H:%M:%S]",
                        handlers=[rich_handler])
    return logging.getLogger(logger_name)


def log_exception(sender, exception, **extra) -> None:
    """ Log an exception to our logging framework """
    sender.logger.error(f'Exception ({repr(exception)}): {str(exception)} | {extra} ')

LOG_ERRORS = {
    'NotFound': {
        'message': "Resource Not Found!.",
        'status': 404,
        'extra': """The requested URL was not found on the server. 
                If you entered the URL manually please check your spelling and try again.            
            """
    },
}