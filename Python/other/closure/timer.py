from datetime import datetime


def timer():
    start = datetime.now()

    def inner():
        return datetime.now() - start

    return inner


if __name__ == '__main__':
    delta = timer()
    print(delta())
    print(delta())
    print(delta())
