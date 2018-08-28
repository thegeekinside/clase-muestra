import unittest
from time_conversion import time_conversion


class TimeConversionTestCase(unittest.TestCase):
    def test_conversion_afternoon(self):
        result = time_conversion("07:15:01PM")
        self.assertEqual(result, "19:15:01")


if __name__ == '__main__':
    unittest.main()
