# Codigo para calcular uma probabilidade pelo metodo de Chapman Kolmogorov
# Aluno: Matheus Chaves Menezes

P = ((0.08,0.184,0.368,0.368),(0.632,0.368,0.0, 0.0),(0.264,0.368,0.368,0.0),(0.08,0.184,0.368,0.368))

def c_kolmogorov (mat_prob, n, m, i, j):
    p_ij = 0
    if m == 1:
        return mat[i][j]

    for k in range (n):
        p_ij += mat[i][k] * c_kolmogorov(mat_prob, n, m - 1, k, j )
    return p_ij


print (c_kolmogorov(P, 2, 2, 0, 1))
