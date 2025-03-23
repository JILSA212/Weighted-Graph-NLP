import networkx as nx
import matplotlib.pyplot as plt

def visualize_graph(graph):
    data = {}
    node_colors = []
    for node in graph:
        data[node] = graph[node].neighbors
        if graph[node].start:
            node_colors.append('blue')
        elif graph[node].end:
            node_colors.append('red')
        else:
            node_colors.append('green')
    
    G = nx.DiGraph(data)
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color=node_colors)
    nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5, edge_color='black')
    nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')
    plt.axis('off')
    plt.show()