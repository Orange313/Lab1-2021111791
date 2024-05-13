import re
import random
from ProcessText import process_text

def find_bridge_words(graph, word1, word2):
    if word1 not in graph.nodes or word2 not in graph.nodes:
        return set()
    successors_word1 = set(graph.successors(word1))
    predecessors_word2 = set(graph.predecessors(word2))
    return successors_word1.intersection(predecessors_word2)

def insert_bridge_word(text, word1, word2, bridge_words):
    if bridge_words:
        bridge_word = random.choice(list(bridge_words))
        return text.replace(word1 + ' ' + word2, word1 + ' ' + bridge_word + ' ' + word2)
    else:
        return text

if __name__ == "__main__":
    file_path = "input.txt"
    word_graph = process_text(file_path)

    new_text = input("请输入一行新文本：")
    words = re.findall(r'\b\w+\b', new_text.lower())  # 提取单词并转换为小写
    modified_text = new_text
    for i in range(len(words)-1):
        word1 = words[i]
        word2 = words[i+1]
        bridge_words = find_bridge_words(word_graph, word1, word2)
        modified_text = insert_bridge_word(modified_text, word1, word2, bridge_words)
    
    print("修改后的文本：", modified_text)







