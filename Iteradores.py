# Creando un iterador
my_list = [1, 2, 3, 4, 5]
my_iter = iter(my_iter)

# Iterando un iterador

print(next(my_iter))

# Cuando no quedan datos, la excepción StopIteration es elevada


# # Creando un iterador
# my_list = [1, 2, 3, 4, 5]
# my_iter = iter(my_list)

# # Iterando un iterador
# while True:                  # Mientras todo sea verdadero, se creará un ciclo infinito
# 	try:
# 		element = next(my_iter)
# 		print(next(my_iter)) # Next nos permite acceder al siguiente elemento del iterador por cada llamada 
# 	except StopIteration:
# 		break                # Salimos del ciclo una vez que obtenemos el último valor iterable