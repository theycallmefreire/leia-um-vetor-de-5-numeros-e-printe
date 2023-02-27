# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

#vetor indefinida
v = []
#laço que conta até 10
for i in range(10):
  #pergunta o numero pra o usuario
    n = float(input(f"{i+1} digite um numero: "))
  #add esse numero no vetor "v"
    v.append(n)
#printa o vetor
print(v)
