# Ejercicio 3
# Dadas dos listas, crear otra que tenga los elementos
# que están en la primera y que no están en la segunda:
# 1. Usando bucles tradicionales.
# 2. Usando listas por comprensión.
# Cada elemento debe aparecer tantas veces como en
# la lista original.

lista1 = [1,2,3]
lista2 = [1,2,3,45,6,7,2]

# #forma 1
# lista3 = lista1 and lista2
# print(lista3)

#forma 2
lista3 = lista1
for i in lista2:
    if i  not in lista1:
        lista3.append(i)
        
print(lista3)