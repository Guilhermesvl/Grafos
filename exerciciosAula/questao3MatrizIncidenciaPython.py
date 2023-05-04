def MA_para_MI(MA, n, m):
    MI = [[0 for j in range(n)] for i in range(m)]

    k = 0
    for i in range(n):
        for j in range(i, n):
            if(MA[i][j] == 1) and (MA[j][i] == 1):
                MI[k][i] = MI[k][j] = 1
                k+=1

    return MI

n, m = map(int, input().split())

while True:
    MA = [[0 for j in range(n)] for i in range(n)]

    for i in range(m):
        u, v = map(int, input().split())
        MA[u][v] = MA[v][u] = 1

    MI = MA_para_MI(MA, n, m)

    for e in range(m):
        print(*MI[e])
   
    
