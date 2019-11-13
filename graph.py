import networkx as nx
import matplotlib.pyplot as plt
import sys

param  = sys.argv[1:] #recebe inicio e final param[0]: inicio
                                           # param[1]: destino

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
        for i in nao_visitados: #percorre os vizinhosnão  visitados
            if i[0] not in visitados and (i[1] + soma) < (soma+menor[1]) and e_Vizinho(grafo,atual,i[0]): # encontra o menor vizinho não visitado
                    menor = i

        visitados.append(menor[0]) #adiciona o vertice a lista de visitados
        atual = menor[0] # atualiza o vertice atual para o que vai ser visitado agora
        soma = atualiza_soma(nao_visitados,atual,inicio) # atualiza soma de acordo com o vertice atual

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
        atual = lista[int(atual) - 1][2]
        menor.append(lista[int(atual) - 1][0])

    return menor[::-1]
# ---------------------main----------------------#
dados = open("C:\\Users\\samue\\PycharmProjects\\graph\\obj.txt") #leitura dos dados do grafo

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

if len(param): #se ao executar os parametros foram colocados na ordem certa
    dk = dijkstra2(grafo, param[0])
    menor = (menor_caminho(grafo,dk,param[0], param[1]))

    if dk == 0:
        menor = 0
else:
    print("Erro: Não passou os parametros")
    menor = 0

if menor != 0:
    #imprimindo o grafico graficamene kkkkk
    G = nx.Graph()

    for i in grafo:
        G.add_node(i)
        for j in grafo[i]:
            G.add_weighted_edges_from([(i, j[0], j[1])])

    pos = nx.planar_layout(G)

    node_sizes = []
    cores = [""]*len(grafo)
    pesos = []
    for key in grafo:
        node_sizes.append(500*len(grafo[key]))
        if key in menor:
            cores[int(key)-1]= "red"
        else:
            cores[int(key)-1] = "blue"

    nodes = nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=cores,label=True)
    label = nx.draw_networkx_labels(G, pos,font_size=10,font_family= "Arial")
    edges = nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=5, width=3)
    #edges_label = nx.draw_networkx_edge_labels(G, pos, edge_labels) #falta adicionar os pesos
    ax = plt.gca()
    ax.set_axis_off()
    titlo = "Menor caminho de " + str(menor[0]) + " a " +str(menor[len(menor)-1])
    plt.title(titlo)
    plt.savefig("Graph.png", format="PNG")
    plt.show()
else:
    print("Erro: Chaves não existem")