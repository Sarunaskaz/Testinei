import unittest
from uzd import prideti_elementa, ar_lyginis, ar_palindromas, palyginti_sarasus


class TestFunkcijos(unittest.TestCase):

    def setUp(self):
        self.x = [1,3,5,7,9]
        self.y = [2,4,6,8,10]
        self.rezultatas = [2]
        self.vienodi = [2,2]
    
    def tearDown(self):
        self.x = None
        self.y = None
    
    # def test_prideti_elementa_sar(self):
    #     for elementas in self.x:
    #         rezult = prideti_elementa(elementas)
    #         self.assertEqual(rezult, [elementas])
            
    def test_prideti_elementa_sarasas(self):
        rezult = prideti_elementa(2, self.x)
        self.assertEqual(rezult, [1,2,3,5,7,9])

    def test_prideti_elementa_sarasas2(self):
        rezult = prideti_elementa(3, self.x)
        self.assertEqual(rezult, 'Elementas jau yra sarase')

    def test_prideti_elementa_sarasas3(self):
        sar = []
        for sk in self.y:
            sar = prideti_elementa(sk, sar)
        self.assertEqual(self.y, sar)
            
    def test_prideti_elementa_sarasas4(self):
        sar = []
        for sk in self.vienodi:
            sar = prideti_elementa(sk, sar)
        self.assertEqual(sar, 'Elementas jau yra sarase')

    # def test_pridedti_elementa(self):
    #     rezult = prideti_elementa(elementas=self.y[0])
    #     self.assertEqual(rezult, self.rezultatas)

    def test_ar_lyginis(self):
        rezult = ar_lyginis(3)
        self.assertTrue(rezult)
    
    def test_ar_palindromas(self):
        rezult = ar_palindromas('labas', 'sabal')
        self.assertTrue(rezult)

    def test_palyginti_sarasus(self):
        rezult = palyginti_sarasus([2,4,6,8,10], [2,4,6,8,10])
        self.assertEqual(rezult, True)
        self.assertNotEqual(rezult, False)


if __name__ == '__main__':
    unittest.main()