import string


def password(value: str) -> str:

    if len(value) < 8:
        return 'Too Weak'

    digits = string.digits
    lowers = string.ascii_lowercase
    uppers = lowers.upper()
    count = 0

    for symb in (digits, lowers, uppers):
        if any(e in symb for e in value):
            count += 1
            continue

    if count == 3:
        return 'Very good'

    return 'Weak' if count == 1 else 'Good'


if __name__ == '__main__':
    assert password('') == 'Too Weak'
    assert password('1234567') == 'Too Weak'
    assert password('qazwsxe') == 'Too Weak'
    assert password('QAZWSXE') == 'Too Weak'
    assert password('1Da') == 'Too Weak'
    assert password('12345678') == 'Weak'
    assert password('123456789') == 'Weak'
    assert password('QAZWSXED') == 'Weak'
    assert password('QAZWSXEDC') == 'Weak'
    assert password('qazwsxed') == 'Weak'
    assert password('qazwsxedc') == 'Weak'
    assert password('qwerQWER') == 'Good'
    assert password('qwerQWERC') == 'Good'
    assert password('1234QWER') == 'Good'
    assert password('1234QWERD') == 'Good'
    assert password('12345qazw') == 'Good'
    assert password('12345QAZWS') == 'Good'
    assert password('123456 qQ') == 'Very good'
    assert password('1QAZWSXe') == 'Very good'
    assert password('12qazwsX') == 'Very good'

