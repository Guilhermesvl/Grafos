def verticeUniversal(MA, n, m):
    for i in range(n):
        for j in range(n):
            if (MA[i][j] == 1):
                if ((i == j) and (MA[i][j] == 0)) :
                    return MA[i][j]
                else:
                    return "nao ha"
                
n, m = map(int, input().split())

while True:
   MA = [[0 for j in range(n)] for i in range(n)]
   
   for i in range(m):
       u, v = map(int, input().split())
       MA[u][v] == 1

verticeUniversal(MA, n, m)

       