import matplotlib as mpl
import matplotlib.pyplot as plt
import networkx
import networkx as nx
import sys


dados = open('obj.txt')

grafo = {}
i = 1
for j in dados:
    j = j.replace('\n', '')
    a = []
    adjacencia = j.split(',')
    vertice = adjacencia.pop(0)
    adjacencia[1] = int(adjacencia[1])
    a.append(adjacencia)
    if vertice in grafo:
        grafo[vertice].append(adjacencia)
    else:
        grafo.update({vertice: a})

print(grafo)


G = nx.Graph()

for i in grafo:
    G.add_node(i)
    for j in grafo[i]:
        G.add_weighted_edges_from([(i, j[0], j[1])])

pos = nx.layout.random_layout(G)
node_sizes = []

for u in grafo:
    node_sizes.append(100*len(grafo[u]))

nodes = nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color='blue',label=True)
#label = nx.draw_networkx_labels(G, pos,font_size=10,font_family= "Arial")
edges = nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=5, width=2)

ax = plt.gca()
ax.set_axis_off()
plt.savefig("Graph.png", format="PNG")
plt.show()

print(nx.dijkstra_path(G,'2','4'))