
import unittest

from circle import*

class CircleTestCase(unittest.TestCase):
   def test_circle_area(self):
       test_data = ((1,1*math.pi), (2,4*math.pi), (3,9*math.pi), (0,0))
       for x,s in test_data:
          res = area(x)
          self.assertEqual(res, s)
       
   def test_circle_perimetr(self):
      test_data = ((1,2*math.pi), (10,20*math.pi), (3,6*math.pi),(0,0))
      for x,s in test_data:
         res = perimeter(x)
         self.assertEqual(res, s)
