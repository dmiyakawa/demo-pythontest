#!/usr/bin/env python

import unittest
import main

class TestSequenceFunctions(unittest.TestCase):
    def testAdd(self):
        self.assertEqual(4, main.add(1, 2))

if __name__ == '__main__':
    unittest.main()

