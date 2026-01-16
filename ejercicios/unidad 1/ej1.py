# Dada una lista de números encontrar el promedio
# de sus elementos:
# 1. Sin usar ninguna función.
# 2. Usando funciones incorporadas de Python


numero = [1,2,3,4,33,2,1,3,7,53,4,56,6]

cantidad = len(numero)
total = 0
for i in  numero:
    total = total + i
    

prom = total / cantidad
print(prom)