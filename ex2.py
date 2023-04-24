inicial = 10
mensal = 5
meses = 24
taxa = 1.01
t = 0 
soma = 0
while t< meses:
    soma += taxa ** t
    t += 1

valor = inicial * taxa ** meses + mensal * soma
print(valor)