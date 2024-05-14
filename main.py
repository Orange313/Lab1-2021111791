import re
import random
from ProcessText import process_text, DirectedGraph
from FindBridge import find_bridge_words
from GenerateNewText import insert_bridge_word
from ShortestWay import shortest_way
from RandomWalking import random_traversal, write_traversal_to_file

def display_menu():
    print("请选择功能：")
    print("1. 处理文本生成有向图")
    print("2. 计算桥接词")
    print("3. 插入桥接词生成新文本")
    print("4. 计算最短路径")
    print("5. 随机游走")
    print("6. 退出")

def main():
    word_graph = None
    bridge_words_cache = {}
    
    while True:
        display_menu()
        choice = input("请输入选项（1-6）：")
        
        if choice == '1':
            file_path = input("请输入文本文件路径：")
            word_graph = process_text(file_path)
            print("文本处理完成，生成了有向图。")

        elif choice == '2':
            if word_graph is None:
                print("请先处理文本生成有向图（选择功能1）。")
                continue
            word1 = input("请输入第一个单词：").lower()
            word2 = input("请输入第二个单词：").lower()
            bridge_words = find_bridge_words(word_graph, word1, word2)
            if bridge_words:
                print(f"桥接词为：{', '.join(bridge_words)}")
                bridge_words_cache[(word1, word2)] = bridge_words
            else:
                print(f"No bridge words from '{word1}' to '{word2}'.")

        elif choice == '3':
            if word_graph is None:
                print("请先处理文本生成有向图（选择功能1）。")
                continue
            new_text = input("请输入一行新文本：")
            words = re.findall(r'\b\w+\b', new_text.lower())
            modified_text = new_text
            for i in range(len(words)-1):
                word1 = words[i]
                word2 = words[i+1]
                bridge_words = bridge_words_cache.get((word1, word2)) or find_bridge_words(word_graph, word1, word2)
                if bridge_words:
                    modified_text = insert_bridge_word(modified_text, word1, word2, bridge_words)
            print("修改后的文本：", modified_text)

        elif choice == '4':
            if word_graph is None:
                print("请先处理文本生成有向图（选择功能1）。")
                continue
            word1 = input("请输入第一个单词：").lower()
            word2 = input("请输入第二个单词：").lower()
            shortest_path, path_length = shortest_way(word_graph, word1, word2)
            if shortest_path:
                print("最短路径为：", " -> ".join(shortest_path))
                print("路径长度为：", path_length)
            else:
                print(f"'{word1}' 和 '{word2}' 之间不可达。")

        elif choice == '5':
            if word_graph is None:
                print("请先处理文本生成有向图（选择功能1）。")
                continue
            visited_edges = random_traversal(word_graph)
            traversal_text = " -> ".join([edge[0] for edge in visited_edges] + [visited_edges[-1][1]])
            print("随机遍历的节点路径：", traversal_text)
            output_file = input("请输入输出文件路径：")
            write_traversal_to_file(visited_edges, output_file)
            print("遍历结果已写入文件。")

        elif choice == '6':
            print("退出程序。")
            break

        else:
            print("无效的选项，请重新输入。")

if __name__ == "__main__":
    main()
