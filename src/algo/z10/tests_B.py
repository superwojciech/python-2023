from solution_B import find_compatible_array 
import unittest

class LongestStreakTests(unittest.TestCase):

    def test_1(self):
        self.assertTrue(find_compatible_array('<<>', [2,8,10,7]))
 
    def test_2(self):
        self.assertTrue(find_compatible_array('<<>', [4,5,9,-1]))

    def test_3(self):
        self.assertFalse(find_compatible_array('-(>)', [4,5,9,-1]))        

    def test_4(self):
        self.assertTrue(find_compatible_array('<><>', [1,2,1,2,1]))         
      
    def test_5(self):
        self.assertFalse(find_compatible_array('<<<<<>', [1,2,3])) 

    def test_6(self):
        self.assertTrue(find_compatible_array('>>>><', [10,9,8,7,6,10]))   

    def test_7(self):
        self.assertFalse(find_compatible_array('0', [0]))                 
               
if __name__ == '__main__':
    unittest.main()