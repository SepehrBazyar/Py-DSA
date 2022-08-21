from functools import wraps
from typing import Callable
from timeit import default_timer as timer


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
        process_time = (timer() - start_time) * 1_000_000  # convert to seconds
        print(f"{function.__name__}[{len(result)}]: {process_time}s")
        return result

    return wrapper
