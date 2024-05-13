import os
import re
import matplotlib.pyplot as plt
import networkx as nx
from ProcessText import process_text


def save_graph(graph, output_path):
    pos = nx.spring_layout(graph, seed=42)  # 使用spring布局算法布局节点
    plt.figure(figsize=(12, 8))
    nx.draw_networkx_nodes(graph, pos, node_size=500, node_color='skyblue', alpha=0.8)
    nx.draw_networkx_labels(graph, pos, font_size=10, font_family='sans-serif')
    edge_labels = {(u, v): d['weight'] for u, v, d in graph.edges(data=True)}
    nx.draw_networkx_edges(graph, pos, width=1.5, alpha=0.6, edge_color='gray')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_size=8)
    plt.axis('off')
    plt.savefig(output_path, format="PNG")
    plt.show()

if __name__ == "__main__":
    file_path = "input.txt"
    word_graph = process_text(file_path)
    output_path = "output_graph.png"
    save_graph(word_graph, output_path)
    print("The gragh is saved successfully! ", output_path)

