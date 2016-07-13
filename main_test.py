#!/usr/bin/env python

import unittest
import main

class TestSequenceFunctions(unittest.TestCase):
    def testAdd(self):
        self.assertEqual(5, main.add(1, 3))

if __name__ == '__main__':
    unittest.main()

