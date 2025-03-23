import random
import pandas as pd

def create_frequence_table(graph):
    frequency_table = {node: {other_node: 0 for other_node in graph.keys()} for node in graph.keys()}
    for node in graph.keys():
        for neighbor in graph[node].neighbors:
            frequency_table[node][neighbor] = graph[node].neighbors[neighbor]
    
    df = pd.DataFrame(frequency_table)
    df['start'] = [graph[node].start for node in df.index]
    # Export the table to a CSV file
    df.to_csv('frequency_table.csv', index=True)
    return df
    
def find_most_appeared_start(df):
    return df[df['start'] == df['start'].max()]

def most_appeared_statement(graph, starting_words):
    # starting_word = find_most_appeared_start(df).index[0]
    starting_word = max(starting_words, key=starting_words.get)
    statement = [starting_word]
    while graph[statement[-1]].end == False:
        next_word = max(graph[statement[-1]].neighbors, key=graph[statement[-1]].neighbors.get)
        statement.append(next_word)
    return ' '.join(statement)

def random_statement(graph, starting_words):
    # non_zero_start_nodes = df[df['start'] != 0].index.tolist()
    # starting_word = random.choice(non_zero_start_nodes)
    starting_word = random.choice(list(starting_words.keys()))
    statement = [starting_word]
    while graph[statement[-1]].end == False:
        next_word = random.choice(list(graph[statement[-1]].neighbors.keys()))
        statement.append(next_word)
    return ' '.join(statement)

def create_file(graph, starting_words):
    with open('output.txt', 'w') as file:
        file.write('Most appeared statement:\n')
        file.write(most_appeared_statement(graph, starting_words))
        file.write('\n\n5 Random statements:\n')
        for i in range(5):
            file.write(random_statement(graph, starting_words))
            file.write('\n')
        file.write('\n')