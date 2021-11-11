def main():
    a = 1 # Variable global

    def nested():
        print(a) # Imprime variable global

    return nested # Retorna la función nested()

my_func = main()
my_func()
# my_func es una variable que guarda un objeto de tipo función, esa función contiene la función nested y por lo tanto my_func se puede ejecutar utilizando los paréntesis.
# Se va ejecutar el print(a) de la función nested y va retornar el valor 1.

# -------------------------------
def main():
    a = 1 # Variable global

    def nested():
        print(a) # Imprime variable global

    return nested # Retorna la función nested()

my_func = main()
my_func()

del(main)
my_func()

# Output:
# 1
# 1

# -------------------------------
def make_multiplier(x):

    def multiplier(n):
        return x * n
    
    return multiplier

times10 = make_multiplier(10)
times4 = make_multiplier(4)

print(times10(3))
print(times4(5))
print(times10(times4(2)))

# Output
# 30
# 20
# 80