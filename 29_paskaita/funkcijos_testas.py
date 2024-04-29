import unittest
from funkcijos import sudetis, atimtis, daugyba, dalyba, ar_lyginis, suapvalinta_dalyba, prideti_i_zodyna


class TestFunkcijos(unittest.TestCase): # Pasijamam is unitest TestCase

    def setUp(self):
        self.x = 10
        self.y = 5
    
    def tearDown(self):
        self.x = None
        self.y = None

    def test_sudetis(self):
        rezult = sudetis(5,3)
        self.assertEqual(rezult, 8)
    
    def test_atimtis(self):
        rezult= atimtis(10,5)
        self.assertEqual(rezult,5) # ar lygus rezult

    def test_daugyba(self):
        rezult = daugyba(5, 10)
        self.assertNotEqual(rezult, 40) # ar nelygus rezult

    def test_ar_lyginis(self):
        rezult = ar_lyginis(8)
        self.assertTrue(rezult) # ar tiesa. assertTrue gera praktika nes griztant prie kodo po kurio laiko lengviau skaityti kas ivyko

    def test_ar_lyginis_nelyginis(self):
        rezult = ar_lyginis(3)
        self.assertFalse(rezult)

    def test_suapvalinta_dalyba(self):
        rezult = suapvalinta_dalyba(16,3)
        self.assertAlmostEqual(rezult, 5.3, places=1)

    def test_dalyba(self):
        rezult = dalyba(self.x , self.y)
        self.assertEqual(rezult, 2)

    def test_dalyba_is_nulio(self):
        with self.assertRaises(ZeroDivisionError):
            dalyba(10,0)
        
    def test_zodynas(self):
        self.assertDictEqual({'key':'value'},{'key':'value'})

    def test_prideti_i_zodynas(self):
        rezult = prideti_i_zodyna("siandien yra pirmadienis")
        zodynas = {'raktas': 'siandien yra pirmadienis'}
        self.assertDictEqual(rezult,zodynas)



if __name__ == '__main__':
    unittest.main()