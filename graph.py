import networkx as nx
import matplotlib.pyplot as plt
import sys

param  = sys.argv[1:] #recebe inicio e final param[0]: inicio
                                           # param[1]: destino
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
    atual = inicio # primeio vertice a ser visitado é o inicio
    soma = 0
    if inicio not in grafo:
        return ""

    for i in grafo:
            nao_visitados.append([i,sys.maxsize]) #criando uma lista de não visiados e colocando o peso de le em 'infinito'

    nao_visitados[int(inicio)-1] = [inicio,0,inicio] #custo do inicial até ele é 0
    visitados.append(inicio) #visitando o vertice inicial

    while (len(visitados) != len(grafo)): #enquanto a lista de visitados for menor que a quantidade de vvertices faça:
        for i in range(len(grafo[atual])): #percorre todos os vizinho do vertice i atualizando os custos
            if grafo[atual][i][0] not in visitados: # se o vizinho não foi visitado
                if nao_visitados[int(grafo[atual][i][0]) -1][1] > grafo[atual][i][1] + soma: # e se novo custo for menor do que está nesse vertice
                    nao_visitados[int(grafo[atual][i][0]) -1] = [grafo[atual][i][0],grafo[atual][i][1] + soma,atual] # recebe novo custo

        menor = [0,sys.maxsize] # inicializando menor

        for i in nao_visitados: #percorre os vizinhos não  visitados
            if i[0] not in visitados and (i[1] + soma) < (soma+menor[1]): # encontra o menor vizinho não visitado
                    menor = i

        visitados.append(menor[0]) #adiciona o vertice a lista de visitados
        atual = menor[0] # atualiza o vertice atual para o que vai ser visitado agora
        soma = atualiza_soma(nao_visitados,atual,menor[2]) # atualiza soma de acordo com o vertice atual

    return nao_visitados

def menor_caminho(grafo,lista,inicio,fim):
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

    if fim not in grafo:
        return 0
    menor.append(fim)
    while (atual != inicio):
        print(atual)
        atual = lista[int(atual) - 1][2]
        menor.append(lista[int(atual) - 1][0])

    return menor[::-1]


def graph_plot(grafo):
    '''
    è responsavel por imprimir o grafico graficamene kkkkk
    :param grafo: é o grafo
    :return:
    '''
    dk = dijkstra2(grafo, param[0])
    menor = (menor_caminho(grafo, dk, param[0], param[1]))
    print(menor)
    G = nx.Graph()

    for i in grafo: #adicionado vertices,arestas e pesos no grafo
        G.add_node(i)
        for j in grafo[i]:
            G.add_weighted_edges_from([(i, j[0], j[1])])

    pos = nx.kamada_kawai_layout(G) #layout do grafo
    grafo_labels = nx.get_edge_attributes(G, 'weight') #lista com os pesos
    cores = [""] * len(grafo) #lista de cores de cada vertice do grafo

    i = 0
    for key in G.nodes(): #colorindo o menor caminho
        if key in menor:
            cores[i] = "red"
        else:
            cores[i] = "black"
        i += 1

    nodes = nx.draw_networkx_nodes(G, pos, node_size=130, node_color=cores, label=True) #desenhando nodes
    label = nx.draw_networkx_labels(G, pos, font_size=8, font_family="Arial", font_color='white')#desenhando nomes/labes nos nodes
    edges = nx.draw_networkx_edges(G, pos, width=1)#desenhando arestas
    edges_label = nx.draw_networkx_edge_labels(G, pos, edge_labels=grafo_labels, font_size=6)#desenhando pesos
    ax = plt.gca()
    ax.set_axis_off()
    titulo = "Menor caminho de " + str(menor[0]) + " a " + str(menor[len(menor) - 1])
    plt.title(titulo)
    plt.savefig("Graph.png", format="PNG") #salvando grafo
    plt.show() #exibindo o grafo graficamente


def main():
    dados = open("obj3.txt") #leitura dos dados do grafo

    grafo = {}
    i = 1
    for j in dados: #leitura do arquivo para filtras as informações e gerar o grafo
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

    if len(param) == 2: #se ao executar os parametros foram colocados na ordem certa
        graph_plot(grafo)
    else:
        print("Erro: Não passou os parametros")



main()