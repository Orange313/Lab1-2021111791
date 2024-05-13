import os
import re
from ProcessText import process_text

file_path = "input.txt"
word_graph = process_text(file_path)

def find_bridge_words(graph, word1, word2):
    bridge_words = []
    if word1 not in graph.nodes or word2 not in graph.nodes:
        return "No word1 or word2 in the graph!"
    successors_word1 = set(graph.successors(word1))
    predecessors_word2 = set(graph.predecessors(word2))
    bridge_words = successors_word1.intersection(predecessors_word2)
    if not bridge_words:
        return "No bridge words from {} to {}!".format(word1, word2)
    else:
        return "The bridge words from {} to {} are: {}.".format(word1, word2, ', '.join(bridge_words))
    
if __name__ == "__main__":
    word1 = input("请输入第一个单词：").lower()
    word2 = input("请输入第二个单词：").lower()
    result = find_bridge_words(word_graph, word1, word2)
    print(result)