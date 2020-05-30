'''
Instruções:
- Faça um programa em Python para resolver o problema. O preço ao consumidor de um carro novo é a soma do custo de fábrica com a porcentagem do distribuidor e dos impostos, ambos aplicados ao custo de fábrica. As porcentagem encontram-se na tabela a seguir. Faça um programa na linguagem Python que receba o custo de fábrica de um carro e mostre o preço ao consumidor.

+------------------------------+---------------------+-------------------+
|      Custo de Fábrica        | % do Distribuidor   |  % dos Impostos   |
+------------------------------+---------------------+-------------------+  
| até R$ 12.000                |         5           |     isento        |
+------------------------------+---------------------+-------------------+
|entre R$ 12.000 (inclusive) e |         10          |       15          |
| R$ 25.000 (inclusive)        |                     |                   |
+------------------------------+---------------------+-------------------+
| acima de R$ 25.000           |         15          |       20          |
+------------------------------+---------------------+-------------------+
'''
#Entradas
preco_fabrica = float(str(input('Digite o preço de fábrica(sem ponto ou vírgula para indicar os milhares): R$')).replace(',','.'))

#Processamento
if preco_fabrica < 12000:
  perc_dist = (preco_fabrica * 5) / 100
  imposto = 0
elif preco_fabrica >= 12000 and preco_fabrica <= 25000:
  perc_dist = (preco_fabrica * 10) / 100
  imposto = (preco_fabrica * 15) / 100
else:
  perc_dist = (preco_fabrica * 15) / 100
  imposto = (preco_fabrica * 20) / 100
preco_consumidor = preco_fabrica + perc_dist + imposto

#Saída
print(f'O preço pago pelo consumidor será: R${preco_consumidor:.2f}')
input('Aperte enter para finalizar a aplicação!')
