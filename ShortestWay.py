import re
import random
from collections import deque
from ProcessText import process_text

def shortest_path(graph, start_word, end_word):
    visited = set() # 存储已访问节点
    predecessors = {} # 字典存储前驱节点
    queue = deque([start_word]) # 创建队列，加入起始单词
    found = False #用于标识找到终点

    while queue:
        current_word = queue.popleft() # 左侧弹出，如果是终点，设置标志位退出
        if current_word == end_word:
            found = True
            break
        #遍历当前节点所有邻居，记录当前节点为邻居的前驱，将邻居加入队列
        for neighbor, weight in graph.get_neighbors(current_word):
            if neighbor not in visited:
                visited.add(neighbor)
                predecessors[neighbor] = current_word
                queue.append(neighbor)

    if not found:
        return None, float('inf')

    # 从最后弹出的节点（终点），往前回溯，知道遇到起始节点
    path = []
    current_word = end_word
    while current_word != start_word:
        path.append(current_word)
        current_word = predecessors[current_word]
    path.append(start_word)
    path.reverse() #反转路径

    # 计算路径长度
    #path_length = sum(graph.get_edge_weight(path[i], path[i+1]) for i in range(len(path)-1))
    for i in range(len(path)-1):
        sum = graph.gragh.get_edge_weight(path[i], path[i+1])
        path_length += sum

    return path, path_length
'''
if __name__ == "__main__":
    file_path = "input.txt"
    word_graph = process_text(file_path)

    start_word = input("Please enter the source word:").lower()
    end_word = input("Please enter the destination word:").lower()

    shortest_path, path_length = shortest_path(word_graph, start_word, end_word)
    if shortest_path:
        print("the shortest way is:", " → ".join(shortest_path))
        print("length:", path_length)
    else:
        print("the two words entered are unreachable.")
'''