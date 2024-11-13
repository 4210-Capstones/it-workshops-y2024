import unittest
from string_util import reverse_string, count_vowels

class StringUtilTest(unittest.TestCase):

    def test_reverse_string(self):
        result = reverse_string("hello")
        self.assertEqual(result, "olleh")

        result = reverse_string("world")
        self.assertEqual(result, "dlrow")

    def test_count_vowels(self):
        result = count_vowels("hello")
        self.assertEqual(result, 2)

        result = count_vowels("world")
        self.assertEqual(result, 1)
if __name__ == "__main__":
    unittest.main()