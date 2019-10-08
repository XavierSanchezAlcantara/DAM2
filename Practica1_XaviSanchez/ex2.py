import unittest

from equacio1 import EquacioPrimerGrau


class TestEquacio(unittest.TestCase):
   def test_eq(self):
       self.assertEqual(Equacio('20x + 3 = 70 ').calcula(),3.0)

if __name__ == "_main_":
   unittest.main()