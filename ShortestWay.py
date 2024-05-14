import re
import random
from collections import deque
from ProcessText import process_text

def shortest_path(graph, start_word, end_word):
    visited = set()
    predecessors = {}
    queue = deque([start_word])
    found = False

    while queue:
        current_word = queue.popleft()
        if current_word == end_word:
            found = True
            break

        for neighbor, weight in graph.get_neighbors(current_word):
            if neighbor not in visited:
                visited.add(neighbor)
                predecessors[neighbor] = current_word
                queue.append(neighbor)

    if not found:
        return None, float('inf')

    # 重构路径
    path = []
    current_word = end_word
    while current_word != start_word:
        path.append(current_word)
        current_word = predecessors[current_word]
    path.append(start_word)
    path.reverse()

    # 计算路径长度
    path_length = sum(graph.get_edge_weight(path[i], path[i+1]) for i in range(len(path)-1))

    return path, path_length

if __name__ == "__main__":
    file_path = "input.txt"
    word_graph = process_text(file_path)

    start_word = input("请输入起始单词：").lower()
    end_word = input("请输入目标单词：").lower()

    shortest_path, path_length = shortest_path(word_graph, start_word, end_word)
    if shortest_path:
        print("最短路径：", " → ".join(shortest_path))
        print("路径长度：", path_length)
    else:
        print("输入的两个单词不可达。")
