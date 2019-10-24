import unittest
import simplecalculator


class TestSimpleCalculator(unittest.TestCase):

    def test_add(self):
        
        self.assertEqual(simplecalculator.add(15,15),30)
        self.assertEqual(simplecalculator.add(45,60),105)
        self.assertEqual(simplecalculator.add(75,22),97)

    def test_multiply(self):
        
        self.assertEqual(simplecalculator.multiply(5,10),50)
        self.assertEqual(simplecalculator.multiply(7,5),35)
        self.assertEqual(simplecalculator.multiply(9,9),81)