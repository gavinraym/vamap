import networkx 
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from pyvis.network import Network
from data import nodes, edges

def Create_Graph(nodes, connections, output_type='saveshow'):
    graph = networkx.Graph()
    for node in nodes:
        graph.add_node(node['label'], title=node['title'])
        node = graph.nodes[node['label']]
        print('Woo')
        print(node)
        #for arg in params:
            #graph[label][arg]=params[arg]

    for edge in edges:
        graph.add_edge(*edge)
        for arg in edges[edge]:
            graph[edge[0]][edge[1]][arg] = edges[edge][arg]

    network = Network(bgcolor='#222222', font_color='white')
    network.from_nx(graph)


    network.save_graph('graph1.html')

    network.show('graph1.html')

if __name__ == '__main__':
    Create_Graph(nodes, edges)