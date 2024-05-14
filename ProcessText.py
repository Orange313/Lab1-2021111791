import re
import matplotlib.pyplot as plt
import networkx as nx

class DirectedGraph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, source, destination, weight=1):
        if source not in self.graph:
            self.graph[source] = {}
        if destination not in self.graph:
            self.graph[destination] = {}

        if destination in self.graph[source]:
            self.graph[source][destination] += weight
        else:
            self.graph[source][destination] = weight

    def has_edge(self, source, destination):
        return source in self.graph and destination in self.graph[source]

    def get_neighbors(self, node):
        return self.graph.get(node, {}).items()

    def get_edge_weight(self, source, destination):
        if self.has_edge(source, destination):
            return self.graph[source][destination]
        else:
            return None
    
    #def get_nodes(self):
    #    return list(self.graph.keys())


def process_text(file_path):
    word_graph = DirectedGraph()
    with open(file_path, 'r') as file:
        for line in file:
            line = re.sub(r'[^a-zA-Z\s]', ' ', line)  # 将标点符号替换为空格
            words = line.split()
            for i in range(len(words)-1):
                word1 = words[i].lower()
                word2 = words[i+1].lower()
                if word1 != word2:
                    if word_graph.has_edge(word1, word2):
                        word_graph.add_edge(word1, word2, weight=word_graph.get_edge_weight(word1, word2) + 1)
                    else:
                        word_graph.add_edge(word1, word2, weight=1)
    return word_graph

def draw_graph(graph):
    G = nx.DiGraph()
    for source, targets in graph.graph.items():
        for target, weight in targets.items():
            G.add_edge(source, target, weight=weight)

    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(10, 6))
    nx.draw(G, pos, with_labels=True, node_size=500, node_color="pink", font_size=10, arrowsize=10)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title("Directed Graph")
    plt.show()

if __name__ == "__main__":
    file_path = "input.txt"  # 替换成你的文件路径
    word_graph = process_text(file_path)
    draw_graph(word_graph)