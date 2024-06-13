import unittest
from ProcessText import DirectedGraph, process_text
from FindBridge import find_bridge_words


class TestFindBridgeWords(unittest.TestCase):
    def setUp(self):
        file_path = "input.txt"
        self.graph = process_text(file_path)

    def test_bridge_word_exists(self):
        word1 = "to"
        word2 = "strange"
        expected_output = "The bridge words from to to strange is: explore."
        result = find_bridge_words(self.graph, word1, word2)
        self.assertEqual(result, expected_output)

    def test_no_bridge_words(self):
        word1 = "seek"
        word2 = "to"
        expected_output = "No bridge words from seek to to!"
        result = find_bridge_words(self.graph, word1, word2)
        self.assertEqual(result, expected_output)

    def test_words_not_in_graph(self):
        word1 = "exciting"
        word2 = "synergies"
        expected_output = "No 'exciting' and 'synergies' in the graph!"
        result = find_bridge_words(self.graph, word1, word2)
        self.assertEqual(result, expected_output)

    def test_word1_not_in_graph(self):
        word1 = "like"
        word2 = "seek"
        expected_output = "No 'like' in the graph!"
        result = find_bridge_words(self.graph, word1, word2)
        self.assertEqual(result, expected_output)

    def test_word2_not_in_graph(self):
        word1 = "and"
        word2 = "exciting"
        expected_output = "No 'exciting' in the graph!"
        result = find_bridge_words(self.graph, word1, word2)
        self.assertEqual(result, expected_output)

    def test_empty_graph(self):
        empty_graph = DirectedGraph()
        word1 = "apple"
        word2 = "cherry"
        expected_output = "No 'apple' and 'cherry' in the graph!"
        result = find_bridge_words(empty_graph, word1, word2)
        self.assertEqual(result, expected_output)


if __name__ == "__main__":
    unittest.main()
