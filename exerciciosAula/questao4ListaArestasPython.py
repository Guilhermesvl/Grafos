def LA_para_LAr(LA, n):
    LAr = []

    #Percorre a LA  e adiciona na LAr (sem nenhuma exceção)
    for i in range(n):
        for aresta in LA[i]:
            j = aresta[0]
            peso = aresta[1]

            if i <= j:         #Apenas para evitar repetição (grafo-não direcionado)
                LAr.append((peso, (i, j)))

    return LAr

while True:
    n, m = map (int, input().split())

    LA = [[] for _ in range(n)]

    for i in range(m):
        u, v, peso = map (int, input().split())

        LA[u].append((v, peso))
        LA[v].append((u, peso))

    LAr = LA_para_LAr(LA, n)

    for aresta in LAr:
        print(f"[{aresta[0]}]({aresta[1][0]},{aresta[1][1]})" , end = " ")
    print()




        
