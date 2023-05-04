from typing import Deque, Any
from collections import deque

BRANCO = 0
CINZA = 1
PRETO = 2

n, m = map(int, input().split())

distancia = [0]
pai = [-1]
cor = [BRANCO]

MA = [0 for j in range(n) for i in range(n)]    #Representação do grafo

while True:
    for i in range(m):
        u, v = map (int, input().split())
        # grafo não direcionado
        MA[u][v] = 1
        MA[v][u] = 1

        s = 1
        fila: Deque[int] = deque()
        fila.append(s)
        cor[s] = CINZA

        while (not fila):
            fila.popleft
            for i in range(MA):
                for j in range(MA):
                    #PRECISA FAZER O TESTE DE MA[i][j] e MA[j][i]
                    if ((MA[i][j] == 1) and (MA[j][i]) == 1):
                        if((cor[i][j] == BRANCO) and (cor[j][i] == BRANCO)):
                            #????
                            cor[i][j] = CINZA
                            cor[j][i] = CINZA

                            #??
                            pai[i][j] = u
                            pai[j][i] = u

                            #??????
                            distancia[i][j] = distancia[u] + 1
                            distancia[j][i] = distancia[u] + 1

    print("Distancias")
    for i in range(n):
        print(f"distancia[{i}]: {distancia[i]}")

    print("Pai")
    for i in range(n):
        print(f"pai[{i}]: {pai[i]}")

    print("*** * ***")








                












    