import unittest
from funkcijos import sudetis, atimtis, daugyba, dalyba


class TestFunkcijos(unittest.TestCase): # Pasijamam is unitest TestCase

    def test_sudetis(self):
        rezult = sudetis(5,3)
        self.assertEqual(rezult, 8)

if __name__ == '__main__':
    unittest.main()