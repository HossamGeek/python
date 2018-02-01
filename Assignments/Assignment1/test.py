
from pkg.module import * 
import unittest


class TestStringMethods(unittest.TestCase):
    
    def test_upper(self):
        self.assertEqual(replacefunc("mobile"), 'mbl')
    
    
    def test_calc(self):
        self.assertEqual(calcword("this is javascript","i"), [2, 5, 15])
   
    
    def test_multi(self):
        self.assertEqual( multifunc(3), [[1], [2, 4], [3, 6, 9]] )
    
    
    def test_calcarea(self):
        self.assertEqual(calcarea('r',10,7), 70)
    
    
    
    def test_names(self):
        self.assertEqual(dicnames(["Alaa","Ahmed","Ehmed","Fatma", "Hossam","Heba"]), [('A', ['Ahmed', 'Alaa']), ('E', ['Ehmed']), ('F', ['Fatma']), ('H', ['Heba', 'Hossam'])])
    
    """    
    def test_stars(self):
        self.assertEqual(star(7))   
        
    """

if __name__ == '__main__':
    unittest.main()
