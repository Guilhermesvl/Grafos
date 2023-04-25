class MaxHeap:
    def __init__(self):
        self.nos = 0
        self.heap = []

    def adicionar(self, valor):
        self.heap.append(valor)
        self.nos += 1
        filho = self.nos
        
        while True:
            if filho == 1 :
                break 
            pai = filho // 2

            if self.heap[pai-1] >= self.heap[filho-1]:
                break
            else:
                self.heap[pai-1], self.heap[filho-1] = self.heap[filho-1], self.heap[pai-1]            
                filho = pai 
        

    def imprime(self):
        for x in self.heap:
            print(str(x), end = " ")

    def remove(self):
        raiz = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.nos -=1
        pai = 1

        for x in self.heap:
            filho = 2 * pai                 #filho da esquerda
            if filho > self.nos:
                break
            if (filho + 1) <= self.nos:     #cmparando para ver se os dois filhos existem
                if (self.heap[(filho + 1) -1]) > self.heap[(filho - 1)]:
                    filho += 1

        

h = MaxHeap()
i = 0

while i < 9:
    valor = int(input())
    h.adicionar(valor) 
    i +=1

h.imprime()