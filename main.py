import datetime
import graph
import visualize
import analyze

# input = "This is the input statement. And everything here works fine. Do you have any question? If so, please don't ask."

log_file = open('log' + str(str(datetime.datetime.now()).replace(":", "_").replace(" ", "_")) + '.txt', 'w')

with open('input.txt', 'r') as file:
    for input in file:
        result = graph.process_data(input, log_file)
graph.dump_graph(log_file)
visualize.visualize_graph(result)
# df = analyze.create_frequence_table(result)
starting_words = graph.make_starting_word_list()

log_file.write("Starting Words Calculated\n")
log_file.write("\tLength: " + str(len(starting_words)) + "\n")
graph.dump_starting_words(log_file)

analyze.create_file(result, starting_words, log_file)

log_file.close()