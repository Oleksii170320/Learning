from unittest import TestCase, main

from pythonProject.Python.other.lessons.calculator import calculator


class CalculatorTest(TestCase):
    def test_plus(self):
        self.assertEquals(calculator("2+2"), 4)

    def test_minus(self):
        self.assertEquals(calculator("3-1"), 2)

    def test_multi(self):
        self.assertEquals(calculator("2*2"), 4)

    def test_divide(self):
        self.assertEquals(calculator("2/2"), 1)

    def test_no_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator("dsfgsdgdsf")
        self.assertEquals('the expression may mean one of the signs (+-/*)', e.exception.args[0])

    def test_two_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator("2+2+2")
        self.assertEquals("the expression may mean two signs", e.exception.args[0])

    def test_many_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator("2+2*4+2")
        self.assertEquals("the expression may mean two signs", e.exception.args[0])


if __name__ == '__main__':
    main()
