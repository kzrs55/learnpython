#coding=utf-8
import unittest
from design_pattern.facade import Facade
__author__ = 'zjutK'


class FacadeTestCase(unittest.TestCase):
    """test for facade.py"""
    def test_facade(self):
        self.assertTrue(Facade().module_two)

if __name__ == '__main__':
    unittest.main()