#################################################################################
#                           Análise de Algoritmos                               #
#                                                                               #
#                               Bionda Rozin                                    #
#                           João Pedro Brum Terra                               #
#                           Marina Barbosa Américo                              #
#                            Nikolas Gomes de Sá                                #
#                                                                               #
#                Professor: Daniel Carlos Guimarães Pedronette                  #
#                                                                               #
#           Trabalho final da Disciplina: Six Degrees of Kevin Bacon            #
#                                                                               #
#                                02/03/2022                                     #
#################################################################################

# Imports
import math

# Algoritmo de busca em largura

def BFS(G, s): #O(V+E)
    # Declaração de variáveis
    d = {}
    pai = {}
    cor = {}
    Q = []
    comparacoes = 0

    # Inicialização
    d[s] = 0
    cor[s] = "cinza"
    pai[s] = None

    for key in G:
        comparacoes+=1
        if key != s:
            d[key] = math.inf
            pai[key] = None
            cor[key] = "branca"

    # Início da fila
    Q.append(s)
    #print("Fila:", Q)

    while Q:
        # Remove primeiro elemento da fila
        u = Q.pop(0)
        # Análise dos vizinhos de u
        for v in G[u]:
            comparacoes+=1
            if cor[v] == "branca":
                cor[v] = "cinza"
                d[v] = d[u] + 1
                pai[v] = u
                Q.append(v)
        # Todos os vértices de u foram visitados
        cor[u] = "preta"
        #print("Fila:", Q)

    # retorno das distâncias de s a v, retorno da árvore BFS e das comparações realizadas no algoritmo
    return d, pai, comparacoes

def FindPath (G, s, v, pai, lista): #O(V)
    # Variável para contar iterações
    comparacoes = 1
    if v == s: # Caso base 1
        lista.append(s)
        return comparacoes
    else:
        comparacoes+=1
        if pai[v] == None: # Caso base 2
            #print("Não existe caminho de", s, "a", v)
            lista.append("Não existe caminho de " + s + " a "+ v)
            return comparacoes
        else:
            # Recursão
            comparacoes += FindPath(G, s, pai[v], pai, lista)
            lista.append(v)
            return comparacoes

def PrintPath(lista): # O(N), sendo N = len(lista)
    # Variável para contar iterações
    comparacoes = 0
    # Exibição do primeiro ator
    print(lista[0], end=" ")
    # Se existe caminho
    if not ("Não existe caminho de " in lista[0]):
        for i in range (1,len(lista)):
            # Nenhum ator está diretamente ligado a outro ator
            comparacoes+=1
            if i%2 == 0:
                # Ator
                print("com", lista[i])
                comparacoes+=1
                if i != len(lista)-1:
                    print(lista[i], end=" ")
            else:
                # Filme
                print("participou de", lista[i], end=" ")

        # O grau de separação de dois atores (bacon number) corresponde
        # à metade do tamanho da lista obtida pela função FindPath, justamente
        # porque nenhum ator está diretamente ligado a outro ator
        print("grau de separação:", i//2)

    # Retorno do número de comparações
    return comparacoes

def ContagemGraus(G, lista_atores): # O(V)
    # Declaração de variáveis
    d = {}
    comparacoes = 0

    # A contagem dos graus dos vértices correspondente aos atores permite
    # identificar quais destes possuem mais interligações diretas
    for a in lista_atores:
        comparacoes+=1
        d[a] = len(G[a])

    # Retorno dos graus dos vértices e do número de comparações
    return d, comparacoes

def findallPaths(G, lista_atores, pai): # O(V^2)
    # Declaração de variáveis
    bacon_num = {}
    comparacoes = 0
    
    # Cálculo do caminho para cada ator
    for a in lista_atores:
        lista = []
        comparacoes+=FindPath(G, "Kevin Bacon", a, pai, lista)
        # Cálculo do Bacon Number
        # É realizado apenas se a pessoa tiver alguma conexão com Kevin Bacon
        if not ("Não existe caminho de " in lista[0]):
            bacon_num[a] = len(lista)//2

    # Retorno dos Bacon Numbers dos atores e do número de comparações
    return bacon_num, comparacoes