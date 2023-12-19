import unittest
import math
from triangle import*
class TriangleTestCase(unittest.TestCase):
   def test_triangle_area(self):
       test_data = ((3,4,math.pi/2,6),)
       for x,y,c,s in test_data:
          res = area(x, y, c)
          self.assertEqual(res, s)
       
   def test_triangle_perimetr(self):
      test_data = ((1,1,1,3), (3,4,5,12))
      for x,y,c,s in test_data:
         res = perimeter(x, y, c)
         self.assertEqual(res, s)
