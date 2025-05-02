def counter():
    count = 0

    def inner(value: int) -> int:
        nonlocal count
        count += value
        return count

    return inner

# ------------------------------------------


def adder(a: int) -> int:
    def inner(value: int):
        return value + a

    return inner


if __name__ == '__main__':
    count = counter()
    print(count(1))
    print(count(2))

    add_2 = adder(2)
    print(add_2(55))

