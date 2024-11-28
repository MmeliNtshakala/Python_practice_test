import unittest
from Part1 import *

class TestFunctions(unittest.TestCase):

    def test_compute_standard_deviation(self):
        self.assertAlmostEqual(compute_standard_deviation([1, 2, 3, 4, 5]), 1.4142135623730951)
        self.assertEqual(compute_standard_deviation([]), None)
        self.assertAlmostEqual(compute_standard_deviation([10, 10, 10]), 0)

    def test_find_second_largest(self):
        self.assertEqual(find_second_largest([1, 2, 3, 4, 5]), 4)
        self.assertEqual(find_second_largest([1, 1, 1]), None)
        self.assertEqual(find_second_largest([5, 5, 4, 4]), 4)

    def test_character_frequency_per_word(self):
        self.assertEqual(character_frequency_per_word("hello world"),
                         {'hello': {'h': 1, 'e': 1, 'l': 2, 'o': 1}, 'world': {'w': 1, 'o': 1, 'r': 1, 'l': 1, 'd': 1}})
        self.assertEqual(character_frequency_per_word("abc abc"), {'abc': {'a': 1, 'b': 1, 'c': 1}})

    def test_check_palindrome(self):
        self.assertTrue(check_palindrome([1, 2, 3, 2, 1]))
        self.assertFalse(check_palindrome([1, 2, 3, 4]))
        self.assertTrue(check_palindrome([1, 1, 1]))

    def test_longest_word_in_sentence(self):
        self.assertEqual(longest_word_in_sentence("The quick brown fox jumped"), "jumped")
        self.assertEqual(longest_word_in_sentence("Hello world"), "Hello")
        self.assertEqual(longest_word_in_sentence("A quick fox"), "quick")

    def test_merge_sorted_lists(self):
        self.assertEqual(merge_sorted_lists([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(merge_sorted_lists([], [1, 2, 3]), [1, 2, 3])
        self.assertEqual(merge_sorted_lists([1, 3, 5], []), [1, 3, 5])

    def test_find_intersection(self):
        self.assertEqual(find_intersection([1, 2, 3, 4], [3, 4, 5, 6]), [3, 4])
        self.assertEqual(find_intersection([1, 2], [3, 4]), [])
        self.assertEqual(find_intersection([1, 2, 3], [3, 2, 1]), [1, 2, 3])

    def test_nth_fibonacci(self):
        self.assertEqual(nth_fibonacci(0), 0)
        self.assertEqual(nth_fibonacci(1), 1)
        self.assertEqual(nth_fibonacci(6), 8)
        self.assertEqual(nth_fibonacci(10), 55)

    def test_reverse_words_in_sentence(self):
        self.assertEqual(reverse_words_in_sentence("The quick brown fox"), "fox brown quick The")
        self.assertEqual(reverse_words_in_sentence("Hello world"), "world Hello")
        self.assertEqual(reverse_words_in_sentence("A B C"), "C B A")

    def test_unique_ual(self):
        # self.acharacters_in_string(self):
        self.assertEqual(unique_characters_in_string("aabbcc"), "abc")
        self.assertEqual(unique_characters_in_string("hello"), "ehlo")
        self.assertEqual(unique_characters_in_string("racecar"), "acer")

if __name__ == '__main__':
    unittest.main()
