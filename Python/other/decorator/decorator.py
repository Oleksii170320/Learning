from functools import wraps
from datetime import datetime


def logger(func):
    @wraps(func)
    def inner(*args, **kwargs):
        start = datetime.now()
        print(f'Start {func.__name__} function ')
        res = func(*args, **kwargs)
        print(f'End {func.__name__} function')
        t = datetime.now() - start
        print(f'Work time - {t}')
        return res

    return inner


@logger
def summ(a, b):
    """
    Return sun "a" and "b"

    :param a, b
    :return int()
    """

    return a + b


if __name__ == "__main__":
    function = summ
    print(function(2, 3))
    # print(function.__name__)
    # print(function.__doc__)
    print(function.__dict__)
