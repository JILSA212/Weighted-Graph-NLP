import re
# import string
punctuation = ".!?;:"

starting_words = {}
graph = {}
line_number = 0

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

def process_data(input, log_file):
    global line_number
    line_number += 1
    words = word_splitting(input)

    log_file.write("Line " + str(line_number) + ":\n")
    log_file.write("Words Count: " + str(len(words)) + "\n")

    start = True
    for word in words:
        log_file.write("Processing Word: " + str(word) + "\n")

        if word not in graph:
            log_file.write("\tCreating Node: " + str(word) + "\n")

            graph[word] = graphNode(word)
            if start:
                log_file.write("\tSetting Start: " + str(word) + "\n")

                graph[word].set_start()
                try:
                    starting_words[word] += 1
                except:
                    starting_words[word] = 1
                
                log_file.write("\tCurrent Count: " + str(starting_words[word]) + "\n")
                start = False
            # if word in string.punctuation:
            if word in punctuation:
                log_file.write("\tPunctuation Found (Setting End): " + str(word) + "\n")

                graph[word].set_end()
                start = True
            try:
                graph[word].add_neighbor(words[words.index(word) + 1])
                log_file.write("\tAdding Neighbor: " + str(words[words.index(word) + 1]) + "\n")
                log_file.write("\t\tCurrent Neighbor: " + str(graph[word].neighbors) + "\n")
            except:
                log_file.write("\tNo Neighbor Found\n")
                log_file.write("\tPunctuation Found (Setting End): " + str(word) + "\n")
                graph[word].set_end()
                start = True
                pass
        else:
            if start:
                log_file.write("\tSetting Start: " + str(word) + "\n")

                graph[word].set_start()
                try:
                    starting_words[word] += 1
                except:
                    starting_words[word] = 1
                
                log_file.write("\tCurrent Count: " + str(starting_words[word]) + "\n")
                start = False
            # if word in string.punctuation:
            if word in punctuation:
                log_file.write("\tPunctuation Found (Setting End): " + str(word) + "\n")

                graph[word].set_end()
                start = True
            try:
                graph[word].add_neighbor(words[words.index(word) + 1])
                log_file.write("\tAdding Neighbor: " + str(words[words.index(word) + 1]) + "\n")
                log_file.write("\t\tCurrent Neighbor: " + str(graph[word].neighbors) + "\n")
            except:
                log_file.write("\tNo Neighbor Found\n")
                log_file.write("\tPunctuation Found (Setting End): " + str(word) + "\n")
                graph[word].set_end()
                start = True
                pass
    return graph

def dump_graph(log_file):
    log_file.write("\n\nDumping Graph:\n")
    for node in graph:
        log_file.write("Node: " + str(node) + "\n")
        log_file.write("\tNeighbors: " + str(graph[node].neighbors) + "\n")
        log_file.write("\tStart: " + str(graph[node].start) + "\n")
        log_file.write("\tEnd: " + str(graph[node].end) + "\n")

def dump_starting_words(log_file):
    log_file.write("\n\nDumping Starting Words:\n")
    for word in starting_words:
        log_file.write("Word: " + str(word) + "\n")
        log_file.write("\tCount: " + str(starting_words[word]) + "\n")

def make_starting_word_list():
    # starting_words = {}
    # for node in graph:
    #     if graph[node].start != 0:
    #         starting_words[node] = graph[node].start
    return starting_words