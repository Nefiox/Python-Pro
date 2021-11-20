import time


def fibo_gen(limit_number):
    n1 = 0
    n2 = 1
    counter = 0
    aux = 0
    while aux < limit_number:
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        else:
            aux = n1 + n2
            n1, n2 = n2, aux
            counter += 1
            yield aux


if __name__ == '__main__':
    fibonacci = fibo_gen(50)
    for element in fibonacci:
        print(element)
        time.sleep(0.05) # Pausa cada 0.05 segundos después de imprimir cada uno de los elementos