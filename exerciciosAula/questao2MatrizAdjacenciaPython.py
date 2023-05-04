def retornaTransposto(MA, n):
    LA = [[] for _ in range(n)]

    for i in range(n):
        j = i
        for j in range(n):
            if (MA[i][j] == 1):
                LA[j].append(n)

    return LA

n, m = map(int, input().split())

while True:
    MA = [[0 for j in range(n)] for i in range(n)]     #matriz nxn inicializada com 0

    for i in range(m):
        u, v = map(int, input().split)
        MA[u][v] = 1

    LA = retornaTransposto(MA, n)
    for u in range(n):
        for j in LA[u]:
            v = LA[u][j]
            print(v, " ")
        print()
            
