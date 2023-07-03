import unittest
from medicalTourism import MedicalTourism
from package import Package
from reservation import Reservation


class TestStringMethods(unittest.TestCase):

    system = MedicalTourism()
    p1 = Package("1", "true 20 midrange")
    r1 = Reservation(p1,"")

    def test_reserve_creation(self):
        n_r = self.system.add_reservation(self.p1, "")
        self.assertIsInstance(n_r, Reservation)

    def test_finalize_reserve(self):
        report = self.system.finalize_res(self.r1, "1234")
        self.assertIsInstance(report, str)

    def test_find_package_by_id(self):
        with self.assertRaises(Exception):
            self.system.find_package_by_id(1000)

    def test_calc_total_cost(self):
        c = self.r1.calc_total_cost()
        self.assertEqual(c, self.r1.package.calc_cost() * 1.1)

    def test_pay1(self):
        self.r1.pay("1234")
        self.assertEqual(self.r1.status, "FINAL")

    def test_pay2(self):
        with self.assertRaises(Exception):
            self.r1.pay("123")

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())
    #     self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':
    unittest.main()