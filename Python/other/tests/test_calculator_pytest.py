import pytest

from pythonProject.Python.other.lessons.calculator import calculator


def test_plus():
    assert calculator("2+2") == 4


def test_no_signs():
    with pytest.raises(ValueError) as error:
        calculator("dsfgsdgdsf")
    assert 'the expression may mean one of the signs (+-/*)' == error.value.args[0]


if __name__ == "__main__":
    pytest.main()
