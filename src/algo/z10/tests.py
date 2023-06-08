from solution import find 
import unittest

class LongestStreakTests(unittest.TestCase):

    def test_1(self):
        self.assertEquals(find("<<>"), 2)

    def test_2(self):
        self.assertEquals(find("<>"), 1)

    def test_3(self):
        self.assertEquals(find("<>>><<"), 3)   

    def test_4(self):
        self.assertEquals(find("<>>>>"), 4)     

    def test_4(self):
        self.assertEquals(find("x12da3<>>"), 2)    

    def test_5(self):
        self.assertEquals(find("<><><><><><><><>"), 1)        

    def test_6(self):
        self.assertEquals(find("x12da3"), 0)  

    def test_6(self):
        self.assertEquals(find("<<<..>>>"), 3)                                     
      
if __name__ == '__main__':
    unittest.main()