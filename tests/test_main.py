import argparse
import unittest
from main import TrieNode, construct_trie, search_word, generate_words, find_optional_solutions

class TestTrieFunctions(unittest.TestCase):
    def setUp(self):
        self.word_list = ['dismissed', 'anterior', 'region', 'nomadic', 'dysmetria', 'corned']
        self.trie = construct_trie(self.word_list)

    def test_construct_trie(self):
        self.assertIsInstance(self.trie, TrieNode)
        self.assertIn('c', self.trie.children)
        self.assertIn('d', self.trie.children)
        self.assertNotIn('x', self.trie.children)

    def test_search_word(self):
        self.assertTrue(search_word(self.trie, 'region'))
        self.assertTrue(search_word(self.trie, 'corned'))
        self.assertFalse(search_word(self.trie, 'cap'))
        self.assertFalse(search_word(self.trie, 'ca'))

    def test_generate_words(self):
        strings = ['dse', 'ima', 'nrg', 'oyc']
        words = generate_words(strings, self.trie)
        self.assertIn('region', words)
        self.assertNotIn('dysmetria', words)
        self.assertNotIn('nomadic', words)

class TestInputValidation(unittest.TestCase):
    def test_validate_input(self):
        from main import validate_input
        self.assertEqual(validate_input('abc'), 'abc')
        with self.assertRaises(argparse.ArgumentTypeError):
            validate_input('abcd')
        with self.assertRaises(argparse.ArgumentTypeError):
            validate_input('ab')

if __name__ == '__main__':
    unittest.main()