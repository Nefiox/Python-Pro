def is_pair(number: int) -> bool:
    if number % 2 == 0:
        return True
    else:
        return False

def run():
    print(is_pair(int(40)))

if __name__ == '__main__':
    run()