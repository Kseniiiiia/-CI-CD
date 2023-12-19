import unittest
from square import*
class SquareTestCase(unittest.TestCase):
   def test_square_area(self):
       test_data = ((1,1), (2,4), (3,9), (0,0))
       for x,s in test_data:
          res = area(x)
          self.assertEqual(res, s)
       
   def test_square_perimetr(self):
      test_data = ((1,4), (10,40), (3,12),(2,8),(0,0))
      for x,s in test_data:
         res = perimeter(x)
         self.assertEqual(res, s)
