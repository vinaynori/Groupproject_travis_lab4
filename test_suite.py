import unittest
from test_ceasercipher import Testceasercipher
from test_multiplicative import Testmultiplicativecipher
from test_reversecipher import TestReversecipher
from test_transpositioncipher import Testtranspositioncipher

def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(Testceasercipher))
    suite.addTest(unittest.makeSuite(Testmultiplicativecipher))
    suite.addTest(unittest.makeSuite(TestReversecipher))
    suite.addTest(unittest.makeSuite(Testtranspositioncipher))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))
my_suite()