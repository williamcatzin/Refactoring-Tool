import unittest
from django.test import TestCase
from mlModels import MLmodels

class TestMLmodels(unittest.TestCase):
    """ To run the test, cd into tool directory and use the command:
        python -m unittest tests.py
    """

    def test_sar(self):
        """ test_sar checks if sarClassification() returns
            a list of length 3 containing string values
        """
        mod = MLmodels("Refactored for more logical structure.")
        result = mod.sarClassification()
        if self.assertEqual(len(result), 3):
            for val in result:
                self.assertIsInstance(val, str)
    
    def test_nonSAR(self):
        """ test_nonSAR checks if sarClassification() returns
            a list of length 1 containing a string value.
        """
        mod = MLmodels("Unit tests for undirected graphs.")
        result = mod.sarClassification()
        if self.assertEqual(len(result), 1):
            self.assertIsInstance(result[0], str)
