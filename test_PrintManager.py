#!/usr/bin/env python3

import unittest
import printManager


class TestPrintManager(unittest.TestCase):
    def test_get_json_data(self):
        self.assertEqual(printManager.get_json_data("user", "printer", "data"),
                         {"userName": "user", "printerName": "printer", "data": "data"})

    def test_get_stdout_data(self):
        self.assertEqual(printManager.get_stdout_data("maravenec"), """a: 2\nc: 1\ne: 2\nm: 1\nn: 1\nr: 1\nv: 1""")


if __name__ == "__main__":
    unittest.main()
