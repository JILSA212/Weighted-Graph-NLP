import os
import datetime
import graph
import visualize
import analyze

# input = "This is the input statement. And everything here works fine. Do you have any question? If so, please don't ask."

datetime_name = str(str(datetime.datetime.now()).replace(":", "_").replace(" ", "_"))
os.path.isdir('Result\\' + datetime_name) or os.makedirs('Result\\' + datetime_name)

log_file = open('Result\\' + datetime_name + '\\log' + datetime_name + '.txt', 'w')

with open('input.txt', 'r', encoding="utf8") as file:
    for input in file:
        result = graph.process_data(input, log_file)
graph.dump_graph(log_file)
visualize.visualize_graph(result)
# df = analyze.create_frequence_table(result)
starting_words = graph.make_starting_word_list()

log_file.write("Starting Words Calculated\n")
log_file.write("\tLength: " + str(len(starting_words)) + "\n")
graph.dump_starting_words(log_file)

analyze.create_file(result, starting_words, datetime_name, log_file)
analyze.analysis_file_creation(result, datetime_name, log_file)

log_file.close()