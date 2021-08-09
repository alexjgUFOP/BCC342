!pip install mip


#importando lib's
from mip import Model, xsum, INTEGER, MAXIMIZE, MINIMIZE


#custo de transporte entre fabrica e armazens
  # F1 nao envia para A4 e F2 nao envia para A1
cost = [[40,50,55,9999999999],
        [999999999,60,30,50]]

#declaracao do modelo
m = Model('Transporte',sense = MINIMIZE)

# definicao da variavel de decisao Xij
x = [[m.add_var(var_type=INTEGER, lb=0) for j in range(4)] for i in range(2)]


# definicao da funcao objetivo
m.objective = xsum(cost[i][j] * x[i][j] for i in range(2) for j in range(4))

# definicao das restricoes

# restricao de envio
m += x[0][3] == 0
m += x[1][0] == 0
# restricao de capacidade produtiva
  # Obs.: = 6000 e 9000 porque caso contrario a sol. otima = 0
m += xsum(x[0][j] for j in range(4)) == 6000
m += xsum(x[1][j] for j in range(4)) == 9000
# restricao de capacidade de armazenamento
m += x[0][0] <= 2500
m += xsum(x[i][1] for i in range(2)) <= 4500
m += xsum(x[i][2] for i in range(2)) <= 5500
m += x[1][3] <= 3500


# otimizacao do modelo
m.optimize()

# impressao dos resultados
print('Optimal Solution: {}'.format([x[i][j].x for i in range(2) for j in range(4)]))
