# def decorador(func):
#     def envoltura(): # wrapper
#         print("Esto se añade a mi función original.")
#         func()
#     return envoltura

# def saludo():
#     print("¡Hola!")

# saludo()
# # Output:
# # ¡Hola!

# saludo = decorador(saludo) # Se guarda la función decorada en la variable saludo
# saludo()                   # La función saludo ahora está decorada
# # Output:
# # Esto se añade a mi función original.
# # ¡Hola!


# # Sugar syntax
# def decorador(func):
#     def envoltura():
#         print("Esto se añade a mi función original.")
#         func()
#     return envoltura

# # De esta manera se decora la función saludo (equivale a saludo = decorador(saludo) de la última línea, quedando ahora en la línea inmediata superior ):
# @decorador                
# def saludo():
#     print("¡Hola!")

# saludo()                   # La función saludo está ahora decorada


def decorator_upper(func):                  # Función decoradora
    def wrapper(text):                      # Función anidada
        return func(text).upper()           # Operación que realiza el decorado a la función (func), inserta el texto a la función original. Convierte todo a mayúsculas.
    return wrapper                          # Devuelve wapper como indica la regla de los Clousures

@decorator_upper                            # Decora la función message
def message(name):
    return f'{name}, recibiste un mensaje'  # Esto es lo que realiza la función message, previo a ser decorada.

@decorator_upper                            # Decora la función warning
def warning(name):
    return f'Usa solo mayúsculas {name}'  # Esto es lo que realiza la función warning, previo a ser decorada.

print(message("Cesar")) # Output: CESAR, RECIBISTE UN MENSAJE
print(warning("Cesar")) # Output: USA SOLO MAYÚSCULAS CESAR