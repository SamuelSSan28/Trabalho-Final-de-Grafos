import networkx as nx
import matplotlib.pyplot as plt
import sys

param  = sys.argv[1:] #recebe inicio e final

def e_Vizinho(grafo,v1,v2):
    '''
    Funcao verifica se o vertice v2 é vizinho vertice v1
    :param grafo: é o grafo
    :param v1: vertice atual
    :param v2: possivel vizinho
    :return:
    '''
    r = False
    for i in range(len(grafo[v1])):
        if v2 == grafo[v1][i][0]:
            r = True
    return  r

def atualiza_soma(lista,atual,inicial):
    '''
    Atualiza a soma acumulada a cada atualização dos valores do Dijkstra
    :param lista: lista de vertices não visitados
    :param atual: vertice que está sendo visitado
    :param inicial: vertice incial
    :return:
    '''
    x =0
    while(atual != inicial):
        x += lista[int(atual)-1][1]
        atual = lista[int(atual)-1][2]

    return  x


def dijkstra2(grafo,inicio):
    '''
    Algoritmo de Dijkstra que calcula o menor caminho de um vertice a todos os outros
    :param grafo: é o grafo
    :param inicio: vertice inicial
    :return:
        lista com o vertice e a distancia dele em relacao ao vertice inicial
    '''
    visitados = []
    nao_visitados = []
    atual = inicio
    soma = 0

    for i in grafo:
            nao_visitados.append([i,sys.maxsize])

    nao_visitados[int(inicio)-1] = [inicio,0,inicio]
    visitados.append(inicio)

    while (len(visitados) != len(grafo)):
        for i in range(len(grafo[atual])):
            if grafo[atual][i][0] not in visitados:
                if nao_visitados[int(grafo[atual][i][0]) -1][1] > grafo[atual][i][1] + soma:
                    nao_visitados[int(grafo[atual][i][0]) -1] = [grafo[atual][i][0],grafo[atual][i][1] + soma,atual]

        menor = [0,sys.maxsize]
        for i in nao_visitados:
            if i[0] not in visitados and (i[1] + soma) < (soma+menor[1]) and e_Vizinho(grafo,atual,i[0]):
                    menor = i

        visitados.append(menor[0])
        atual = menor[0]
        soma = atualiza_soma(nao_visitados,atual,inicio)

    return nao_visitados

def menor_caminho(lista,inicio,fim):
    '''
    Mostra o menor caminho do vertice inicial até o vertice fim
    :param lista: saída da funcção dijkstra(grafo,inicio)
    :param inicio: vertice inicial utilizado na função dijkstra
    :param fim: vertice destino
    :return:
        retorna o caminho e o peso do caminho inicio ao fim
    '''
    menor = []
    atual = fim

    menor.append(fim)
    while (atual != inicio):
        atual = lista[int(atual) - 1][2]
        menor.append(lista[int(atual) - 1][0])

    return menor[::-1]
# ---------------------main----------------------#
dados = open("C:\\Users\\samue\\PycharmProjects\\graph\\obj.txt")

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
dados.close()

if len(param):
    dk = dijkstra2(grafo, '5')
    menor = (menor_caminho(dk, '5', '3'))
else:
    menor = "0"


G = nx.Graph()

for i in grafo:
    G.add_node(i)
    for j in grafo[i]:
        G.add_weighted_edges_from([(i, j[0], j[1])])

pos = nx.layout.random_layout(G)
node_sizes = []

for u in grafo:
    node_sizes.append(500*len(grafo[u]))

nodes = nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color='blue',label=True)
label = nx.draw_networkx_labels(G, pos,font_size=10,font_family= "Arial")
edges = nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=10, width=3)

ax = plt.gca()
ax.set_axis_off()
plt.savefig("Graph.png", format="PNG")
plt.show()
