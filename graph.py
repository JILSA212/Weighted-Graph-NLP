import re
import string

# starting_words = set()

def word_splitting(input):
    pattern = r'\w+|[^\w\s]'
    bag_of_words = re.findall(pattern, input)
    return bag_of_words

class graphNode:
    def __init__(self, word):
        self.word = word
        self.neighbors = {}
        self.start = 0
        self.end = False

    def set_start(self):
        self.start += 1

    def set_end(self):
        self.end = True

    def add_neighbor(self, neighbor):
        if neighbor not in self.neighbors:
            self.neighbors[neighbor] = 1
        else:
            self.neighbors[neighbor] += 1

def process_data(input):
    words = word_splitting(input)
    graph = {}
    start = True
    for word in words:
        if word not in graph:
            graph[word] = graphNode(word)
            if start:
                graph[word].set_start()
                # starting_words.add(word)
                start = False
            if word in string.punctuation:
                graph[word].set_end()
                start = True
            try:
                graph[word].add_neighbor(words[words.index(word) + 1])
            except:
                pass
    return graph