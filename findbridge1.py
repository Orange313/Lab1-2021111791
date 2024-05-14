import re


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

    def get_edge_weight(self, source, destination):
        if self.has_edge(source, destination):
            return self.graph[source][destination]
        else:
            return None
            
def find_bridge_words(graph, word1, word2):  
      # Check if words are in the graph  
     if word1 not in graph.graph and word2 not in graph.graph: 
        return f"No '{word1}' and '{word2}' in the graph!"  
     if word1 not in graph.graph:  
        return f"No '{word1}' in the graph!"  
     if word2 not in graph.graph:  
        return f"No '{word2}' in the graph!"  
      
     # Find all possible bridge words  
     bridge_words = set()  
     for neighbor in graph.graph[word1]:  
        if word2 in graph.graph[neighbor]:  
            bridge_words.add(neighbor)  
  
     # Format the output  
     if not bridge_words:  
        return "No bridge words from {} to {}!".format(word1, word2)  
      
     bridge_words_list = list(bridge_words)  
     bridge_words_str = ', '.join(bridge_words_list[:-1]) + bridge_words_list[-1]  
     return "The bridge words from {} to {} is: {}.".format(word1, word2, bridge_words_str) 

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


if __name__ == "__main__":  
    file_path = 'input.txt'  # Replace with your actual file path  
    word_graph = process_text(file_path)  
  
    # User input for two words  
    word1 = input("Enter the first word: ").strip().lower()  
    word2 = input("Enter the second word: ").strip().lower()  
  
    # Find bridge words  
    bridge_words_result = find_bridge_words(word_graph, word1, word2)  
    print(bridge_words_result)