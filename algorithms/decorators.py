import logging, logging.config  # noqa: E401
from functools import wraps
from typing import Callable
from timeit import default_timer as timer


logging.config.fileConfig(fname="logging.ini")
logger = logging.getLogger(__name__)


def process_timer(function: Callable[[list], list]):
    """decorator for processing timer sorting algorithm functions

    :param function: function of sorting algorithms
    :type function: Callable[[list], list]
    :return: decorated function of sorting algorithms with process time
    :rtype: Callable[[list], list]
    """

    @wraps(function)
    def wrapper(*args, **kwargs):
        start_time = timer()
        result = function(*args, **kwargs)
        process_time = (timer() - start_time) * 1_000_000  # convert to microseconds
        logger.info(f"{function.__name__}[{len(result)}]: {process_time:.4f} μs")
        return result

    return wrapper
