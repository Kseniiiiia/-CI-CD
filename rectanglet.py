
import unittest
from rectangle import*

class RectangleTestCase(unittest.TestCase):
   def test_rectangle_area(self):
       test_data = ((1,1,1), (2,2,4), (3,3,9),(0,2,0),(2,0,0))
       for x,y,s in test_data:
          res = area(x, y)
          self.assertEqual(res, s)
       
   def test_rectangle_perimetr(self):
      test_data = ((1,1,4), (10,1,22), (3,3,12),(2,3,10),(3,2,10))
      for x,y,s in test_data:
         res = perimeter(x, y)
         self.assertEqual(res, s)

