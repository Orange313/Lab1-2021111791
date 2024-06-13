import unittest
from ProcessText import DirectedGraph,process_text
from FindBridge import find_bridge_words

class TestFindBridgeWords(unittest.TestCase):

    def setUp(self):
        # 初始化一个 DirectedGraph 实例作为测试用的图数据结构
        self.graph = DirectedGraph()
        # 添加一些边来构建一个测试用的图
        self.graph.add_edge('apple', 'banana')
        self.graph.add_edge('apple', 'orange')
        self.graph.add_edge('banana', 'cherry')
        self.graph.add_edge('orange', 'cherry')

    def test_bridge_words_exists(self):
        word1 = 'apple'
        word2 = 'cherry'
        expected_output = "The bridge words from apple to cherry is: banana, orange."
        result = find_bridge_words(self.graph, word1, word2)
        self.assertEqual(result, expected_output)

    def test_no_bridge_words(self):
        word1 = 'banana'
        word2 = 'orange'
        expected_output = "No bridge words from banana to orange!"
        result = find_bridge_words(self.graph, word1, word2)
        self.assertEqual(result, expected_output)

    def test_words_not_in_graph(self):
        word1 = 'pear'
        word2 = 'grape'
        expected_output = "No 'pear' and 'grape' in the graph!"
        result = find_bridge_words(self.graph, word1, word2)
        self.assertEqual(result, expected_output)

    def test_word1_not_in_graph(self):
        word1 = 'pear'
        word2 = 'orange'
        expected_output = "No 'pear' in the graph!"
        result = find_bridge_words(self.graph, word1, word2)
        self.assertEqual(result, expected_output)

    def test_word2_not_in_graph(self):
        word1 = 'apple'
        word2 = 'grape'
        expected_output = "No 'grape' in the graph!"
        result = find_bridge_words(self.graph, word1, word2)
        self.assertEqual(result, expected_output)

    def test_empty_graph(self):
        empty_graph = DirectedGraph()
        word1 = 'apple'
        word2 = 'cherry'
        expected_output = "No 'apple' and 'cherry' in the graph!"
        result = find_bridge_words(empty_graph, word1, word2)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
