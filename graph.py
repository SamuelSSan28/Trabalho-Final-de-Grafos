import networkx as nx
import matplotlib.pyplot as plt
import sys


def dijkstra(grafo, inicio, fim,v = []):
    caminho = []
    soma = 0
    atual = inicio
    vertice = 0
    caminho.append(inicio)
    visitados = v
    visitados.append(inicio)
    alternativo = []

    while (atual != fim):
        menor = sys.maxsize
        for i in range(len(grafo[atual])):
            if grafo[atual][i][0] in caminho:
                continue

            if grafo[atual][i][1] == menor:
                visitados_local = []
                visitados_local += visitados

                alternativoAtual = dijkstra(grafo,grafo[atual][i][0],fim,v= visitados_local)

                visitados_local = []
                visitados_local += visitados
                visitados_local.append(grafo[atual][i][0])

                alternativoAnterior = dijkstra(grafo, anterior,fim, v=visitados_local)

                if len(alternativoAnterior[0]) < len(alternativoAtual[0]) or alternativoAnterior[1] < alternativoAtual[1]:
                    alternativa = caminho + alternativoAnterior[0]
                else:
                    alternativa = caminho + alternativoAtual[0]

                if len(alternativo) < len(alternativa) and len(alternativo) > 0:
                    caminho = alternativo
                else:
                    caminho = alternativa

                return  caminho,soma

            if grafo[atual][i][1] < menor and grafo[atual][i][0] not in visitados or grafo[atual][i][0] == fim :
                menor = grafo[atual][i][1]
                anterior = vertice = grafo[atual][i][0]

            visitados.append(grafo[atual][i][0])



        caminho.append(vertice)
        atual = vertice
        soma += menor

    return caminho,soma


# ---------------------main----------------------#
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
print(dijkstra(grafo, 'A', 'F'))

dados.close()

dados = open('obj2.txt','a+')
dados.close()
