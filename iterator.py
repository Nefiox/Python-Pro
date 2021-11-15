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


class EvenNumbers:
  """Clase que implementa un iterador de todos los números pares,
  o los números pares hasta un máximo que definimos
  """

  # Constructor
  def __init__(self, max = None): # self = objeto futuro creado con esta clase | max = número máximo
    self.max = max

  # Método para tener elementos o atributos que voy a necesitar para que el iterador funcione
  def __iter__(self):
    self.num = 0            # Primer número par
    return self             

  # Método para tener la función "next" del ciclo for, es decir, recorrer cada valor.
  def __next__(self):
    if not self.max or self.num <= self.max:
      result = self.num
      self.num += 2
      return result
    else:
      raise StopIteration