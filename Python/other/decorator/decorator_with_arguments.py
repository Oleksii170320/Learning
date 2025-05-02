from functools import wraps


def typer(type_):
    def typer(func):

        @wraps(func)
        def inner(*args, **kwargs):
            for arg in args:
                if not isinstance(arg, type_):
                    raise ValueError(f'Type is not {type_}. Please check your input data. ')

            return func(*args)

        return inner

    return typer


@typer(int)
def summ(a: int, b: int, c: int) -> int:
    """
    Return sun "a" and "b"

    :param a, b
    :return int()
    """

    return a + b + c


@typer(str)
def concat(a: str, b: str, c: str) -> str:
    """
    Return sun "a" and "b"

    :param a, b
    :return int()
    """

    return a + b + c


if __name__ == "__main__":
    function_int = summ
    function_str = concat

    print(function_int(3, 5, 7))
    print(function_str("a", "b", "c"))
