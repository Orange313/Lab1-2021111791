import random
from ProcessText import process_text

def find_bridge_words(graph, word1, word2):
    if word1 not in graph.graph and word2 not in graph.graph:
        return f"No '{word1}' and '{word2}' in the graph!"
    if word1 not in graph.graph:
        return f"No '{word1}' in the graph!"
    if word2 not in graph.graph:
        return f"No '{word2}' in the graph!"

    bridge_words = set()
    for neighbor in graph.graph[word1]:
        if word2 in graph.graph[neighbor]:
            bridge_words.add(neighbor)

    if not bridge_words:
        return "No bridge words from {} to {}!".format(word1, word2)

    bridge_words_list = list(bridge_words)
    bridge_words_str = ', '.join(bridge_words_list[:-1]) + bridge_words_list[-1]
    return "The bridge words from {} to {} is: {}.".format(word1, word2, bridge_words_str)

def insert_bridge_words(graph, text):
    words = text.split()
    new_text = []
    for i in range(len(words) - 1):
        new_text.append(words[i])
        word1 = words[i].lower()
        word2 = words[i + 1].lower()
        new_text.extend(choose_bridge_word(graph, word1, word2))
    new_text.append(words[-1])
    return ' '.join(new_text)

def choose_bridge_word(graph, word1, word2):
    bridge_words = []
    for neighbor in graph.graph[word1]:
        if word2 in graph.graph[neighbor]:
            bridge_words.append(neighbor)
    if bridge_words:
        return [random.choice(bridge_words)]
    return []

# Example usage:
if __name__ == "__main__":
    # Assume you have your DirectedGraph instance stored in 'graph'
    # and your text in 'text'
    text = "Seek to explore new and exciting synergies"
    new_text = insert_bridge_words(graph, text)
    print("Original text:", text)
    print("New text:", new_text)
