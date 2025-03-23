import random
import pandas as pd
import evaluate

perplexity_list = []

# def create_frequence_table(graph):
#     frequency_table = {node: {other_node: 0 for other_node in graph.keys()} for node in graph.keys()}
#     for node in graph.keys():
#         for neighbor in graph[node].neighbors:
#             frequency_table[node][neighbor] = graph[node].neighbors[neighbor]
    
#     df = pd.DataFrame(frequency_table)
#     df['start'] = [graph[node].start for node in df.index]
#     # Export the table to a CSV file
#     df.to_csv('frequency_table.csv', index=True)
#     return df
    
# def find_most_appeared_start(df):
#     return df[df['start'] == df['start'].max()]

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

        # next_word = max(graph[statement[-1]].neighbors, key=graph[statement[-1]].neighbors.get)
        try:
            next_word = max(
                (word for word in graph[statement[-1]].neighbors if word not in statement),
                key=lambda word: graph[statement[-1]].neighbors[word]
            )
        except:
            next_word = random.choice(list(graph[statement[-1]].neighbors.keys()))
            log_file.write('\tRandomly selecting next word\n')
            
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

def create_file(graph, starting_words, datetime_name, log_file):
    global perplexity_list
    with open('Result\\' + datetime_name + '\\output.txt', 'w') as file:
        log_file.write('\n\nCreating output file\n')

        file.write('Most appeared statement:\n')
        statement = most_appeared_statement(graph, starting_words, log_file)
        score = evaluate.calculate_perplexity(statement)
        file.write(str(statement) + "\n")
        file.write('Perplexity: ' + str(score))
        log_file.write('\nPerplexity Score: ' + str(score) + '\n')
        log_file.write('\nMost Appeared Statement Process Completed\n')

        file.write('\n\n5 Random statements:\n')
        for i in range(5):
            statement = random_statement(graph, starting_words, log_file)
            score = evaluate.calculate_perplexity(statement)
            perplexity_list.append(score)
            file.write(str(statement) + "\n")
            file.write('Perplexity: ' + str(score) + "\n\n")
            log_file.write('\nPerplexity Score: ' + str(score) + '\n')
        log_file.write('\nRandom Statement Process Completed\n')
        file.write('\n')

def analysis_file_creation(graph, datetime_name, log_file):
    log_file.write('\n\nCreating analysis file\n')
    analysis_file = open('Result\\' + datetime_name + '\\analysis' + datetime_name + '.txt', 'w')
    analysis_file.write("Input Size: " + str(len(graph)) + "\n")
    analysis_file.write("Max Perplexity: " + str(max(perplexity_list)) + "\n")
    analysis_file.write("Min Perplexity: " + str(min(perplexity_list)) + "\n")
    analysis_file.write("Average Perplexity: " + str(sum(perplexity_list) / len(perplexity_list)) + "\n")
    log_file.write('\nAnalysis File Created\n')
    analysis_file.close()