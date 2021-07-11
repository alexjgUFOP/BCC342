import math

# QUESTÃO 01: implementar 0 bracket method em um intervalo unimodal

# Funcao Bracket method
def bracket(a,f,s=0.001,m=2):
  """ Finds an interval [a,b] where the function f is unimodal
  Args:
    a: Starting point
    f: Objective function
    s: Initial step size
    m: scaling factor for the step size
  Returns:
    A list with the lower and upper bounds of the interval 
    in wich f is supposedly unimodal 
  """
  
  # definindo b como a + s (tolerância de busca) 
  b = a + s
  # criando uma lista bracket com o intervalo de busca
  bracket = [a,b] 

  # verificando os valores da função para f(a) e f(b)
  fa = f(a)
  fb = f(b)

  # se f(a) >= f(b), então o ponto auxiliar c fica a direita de b
  if fa >= fb :
  
    c = b + s
    fc = f(c)
    # enquanto fc < fb continuamos aproximando do mínimo atribuindo c em b
    while fc < fb:
      b = c
      fb = fc
      s = s*m
      c = c + s
      fc = f(c)
      
      # atualizando a lista com o novo intervalo aproximando
      bracket = [a,c]

  # se f(a) < f(b), então o ponto auxiliar c fica a esquerda de a
  elif fa < fb :
    c = a - s
    fc = f(c)
    # enquanto fc < fa continuamos aproximando do mínimo atribuindo c em a
    while fc < fa:
      a = c
      fa = fc
      s = s*m
      c = c -  s
      fc = f(c)
      
      # atualizando a lista com o novo intervalo aproximando
      bracket = [c,b] 

  # intervalo mínimo de extremo alcançado
  return bracket

# QUESTÃO 02: implementação do Golden-section Method

# Golden Search method
def goldenSearch(f,a,b,t=1e-6):
  '''
    Metodo de implementacao baseado no metodo de Fibonacci
    Encontra um ponto extremo em um intervalo unimodal da funcao
    
    Argumentos: 
      f: funcao objetivo
      a: ponto inicial do intervalo
      b: ponto final do intervalo
      t: tolerancia para o ponto extremo de mínimo
  '''

  # definindo o golden ratio
  gr = (math.sqrt(5) +1 )/2

  c = b - (b-a)/gr
  d = a + (b-a)/gr

  while abs(b-a) > t:
    if f(c) > f(d):
      a = c
    else:
      b = d
      
    c = b - (b-a)/gr
    d = a + (b-a)/gr

  # retorna o pont de mínimo que é apresentado na metade do intervalo e com uma tolerância de erro igual = t/2 no intervalo [a,b] de f
  return (b+a)/2


# definindo uma funcao f
f = lambda x: (x+2)**2

# aplicando os metodos a nossa funcao f
b = bracket(1,f)
g = goldenSearch(f,-4,1)

print(b)
print(g)
