# Autor: Pedro Arfux
# Fonte: https://www.youtube.com/watch?v=tRljLFDrzhg
# método da bisseção para encontrar raízes de funções

import numpy as np # pip install numpy

def bissec(a,b,erro):
  #calculand o número de iterações
  n=(np.log(b-a)-np.log(erro))/np.log(2)
  #afunção ceil pega o próximo inteiro
  n=np.ceil(n)
  i=0
  print("="*40)
  print("Valor das iterações")
  print("="*40)
  while i<n:
    #Verificando a condição de Bolzano
    if f(a)*f(b)>0:
      print("Não podemos afirmar se há raiz neste intervalo")
    else:
      #Criar um ponto médio m=(a+b)/2
      m=(a+b)/2
      m=round(m,6)
      if f(a)*f(m)<0:
        b=m
      else:
        a=m
    print(f'valor de x_{i+1}={m}')
    i+=1
  return print(f'\n 0 valor aproximado da raiz é:{m}')

#definindo a função
def f(x):
  y=x**2-7
  return y

bissec(2,3,0.01)