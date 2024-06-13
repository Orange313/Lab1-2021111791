import unittest
import random
from ProcessText import DirectedGraph, process_text, draw_graph


class TestRandomTraversal(unittest.TestCase):
    def setUp(self):
        file_path = "input.txt"
        self.word_graph = process_text(file_path)

    def test_random_traversal(self):
        visited_nodes = set()
        visited_edges = []

        # 从图中随机选择一个起始节点
        start_node = random.choice(list(self.word_graph.graph.keys()))
        current_node = start_node
        visited_nodes.add(current_node)

        while True:
            out_edges = list(self.word_graph.get_neighbors(current_node))
            if not out_edges:  # 如果当前节点不存在出边，停止遍历
                break

            next_node, _ = random.choice(out_edges)  # 随机选择一个下一个节点
            next_edge = (current_node, next_node)

            visited_edges.append(next_edge)
            visited_nodes.add(next_node)
            current_node = next_node  # 更新当前节点为下一个节点

        # Assert that visited edges are valid in the graph
        for edge in visited_edges:
            self.assertTrue(self.word_graph.has_edge(edge[0], edge[1]))

        # Assert that visited nodes are all in the graph
        for node in visited_nodes:
            self.assertIn(node, self.word_graph.graph)


if __name__ == "__main__":
    unittest.main()
