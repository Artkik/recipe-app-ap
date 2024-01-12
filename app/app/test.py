# Sample test

from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):

    def test_add_numbers(self):
        res = calc.add(5, 6)

        self.assertEqual(res, 11)


#Subtract Numbers test
    def test_subtract_numbers(self):

        res = calc.subtract(10, 15)

        self.assertEqual(res, 5)d