import unittest
import simplecalculator


class TestSimpleCalculator(unittest.TestCase):

    # def test_add(self):
    def test_add(self):
        self.assertEqual(simplecalculator.add([14,16]),30)
        self.assertEqual(simplecalculator.add([45,60]),105)
        self.assertEqual(simplecalculator.add([75,22]),97)

        self.assertEqual(simplecalculator.add([14,16,22]),52)
        self.assertEqual(simplecalculator.add([45,60,45,19]),169)
        self.assertEqual(simplecalculator.add([75,22,53,77]),227)

    def test_multiply(self):
        self.assertEqual(simplecalculator.multiply([5,10]),50)
        self.assertEqual(simplecalculator.multiply([7,5]),35)
        self.assertEqual(simplecalculator.multiply([9,9]),81)

        self.assertEqual(simplecalculator.multiply([5,10,2]),100)
        self.assertEqual(simplecalculator.multiply([7,5,10,9]),3150)
        self.assertEqual(simplecalculator.multiply([10,7,5,9,12,6]),226800)