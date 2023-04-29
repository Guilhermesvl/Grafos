from typing import Tuple
import random

def retornaGrau(LA, n, u):
    graudeEntrada = 0
    grau = (graudeEntrada, len(LA[u]))

    for i in range(n):
        for j in range(len(LA[i])):
            if(LA[i][j] == u):
                graudeEntrada +=1
    return tuple(grau)

n, m = map(int, input().split())


while True: 
    LA = [[] for _ in range(n)]
    
    
    for i in range(m):
        u, v = map(int, input().split())

    LA[u].append(v) 

    vertice = random.randint(0, n-1)
    grau = retornaGrau(LA, n, vertice)
    print(f"{vertice} {grau[0]} {grau[1]}")










