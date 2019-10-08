import unittest

from equacio1 import EquacioPrimerGrau


class TestEquacio(unittest.TestCase):
   def test_eq(self):
       self.assertEqual(EquacioPrimerGrau('20x + 4 = 70 ').calcula(),3.0)

if __name__ == "_main_":
   unittest.main()