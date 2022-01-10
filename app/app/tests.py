from django.test import TestCase
from app.calc import substraction
from app.calc import add

class CalcTests(TestCase):
    def test_add_number(self):
        #Test that two number added togather
        self.assertEqual(add(3,8), 11)

    def test_substraction_number(self):
        self.assertEqual(substraction(8,3),5)
        