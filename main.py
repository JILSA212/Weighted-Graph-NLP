import graph
import visualize
import analyze

# input = "This is the input statement. And everything here works fine. Do you have any question? If so, please don't ask."

file = open('input.txt', 'r')
input = file.read()
file.close()

result = graph.process_data(input)
visualize.visualize_graph(result)
df = analyze.create_frequence_table(result)
analyze.create_file(result, df)