m = [][]

# calcula a multiplicacao das matrizes
def exp_matriz(h, m):
    p = m
    for i in range(int(h)-1):
        p = p.dot(m)
    return p
    
def classificar_estados(n):

  
