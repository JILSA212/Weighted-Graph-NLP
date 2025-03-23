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

def most_appeared_statement(graph, starting_words, log_file):
    statement_limit = 100
    log_file.write('\n\nCreating most appeared statement\n')

    # starting_word = find_most_appeared_start(df).index[0]
    starting_word = max(starting_words, key=starting_words.get)
    log_file.write('\tStarting word: ' + starting_word + '\n')

    statement = [starting_word]
    log_file.write('\tCurrent Statement: ' + str(statement) + '\n')

    while graph[statement[-1]].end == False:
        log_file.write('\tInside While\n')

        next_word = max(graph[statement[-1]].neighbors, key=graph[statement[-1]].neighbors.get)
        log_file.write('\tNext Word: ' + str(next_word) + '\n')

        statement.append(next_word)
        log_file.write('\tCurrent Statement: ' + str(statement) + '\n')

        if(len(statement) > statement_limit):
            log_file.write('\tStatement length exceeded the given limit (limit: ' + str(statement_limit) + ')\n')
            break
    return ' '.join(statement)

def random_statement(graph, starting_words, log_file):
    statement_limit = 100
    log_file.write('\n\nCreating Random statement\n')

    # non_zero_start_nodes = df[df['start'] != 0].index.tolist()
    # starting_word = random.choice(non_zero_start_nodes)
    starting_word = random.choice(list(starting_words.keys()))
    log_file.write('\tStarting word: ' + starting_word + '\n')

    statement = [starting_word]
    log_file.write('\tCurrent Statement: ' + str(statement) + '\n')

    while graph[statement[-1]].end == False:
        log_file.write('\tInside While\n')

        next_word = random.choice(list(graph[statement[-1]].neighbors.keys()))
        log_file.write('\tNext Word: ' + str(next_word) + '\n')

        statement.append(next_word)
        log_file.write('\tCurrent Statement: ' + str(statement) + '\n')

        if(len(statement) > statement_limit):
            log_file.write('\tStatement length exceeded the given limit (limit: ' + str(statement_limit) + ')\n')
            break
    return ' '.join(statement)

def create_file(graph, starting_words, log_file):
    with open('output.txt', 'w') as file:
        log_file.write('\n\nCreating output file\n')

        file.write('Most appeared statement:\n')
        file.write(most_appeared_statement(graph, starting_words, log_file))
        log_file.write('\nMost Appeared Statement Process Completed\n')

        file.write('\n\n5 Random statements:\n')
        for i in range(5):
            file.write(random_statement(graph, starting_words, log_file))
            file.write('\n')
        log_file.write('\nRandom Statement Process Completed\n')
        file.write('\n')