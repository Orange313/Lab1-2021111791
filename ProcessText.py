import re
import networkx as nx

def process_text(file_path):
    word_graph = nx.DiGraph()
    with open(file_path, 'r') as file:
        for line in file:
            line = re.sub(r'[^a-zA-Z\s]', ' ', line)  # 将标点符号替换为空格
            words = line.split()
            for i in range(len(words)-1):
                word1 = words[i].lower()
                word2 = words[i+1].lower()
                if word1 != word2:
                    if word_graph.has_edge(word1, word2):
                        word_graph[word1][word2]['weight'] += 1
                    else:
                        word_graph.add_edge(word1, word2, weight=1)
    return word_graph
