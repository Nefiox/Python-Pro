# [1, 1, 2, 2, 4] -> [1, 2, 4]

def remove_duplicates(some_list):
    without_duplicates = []
    for element in some_list:
        if element not in without_duplicates:
            without_duplicates.append(element)
    return without_duplicates

def run():
    random_List = [1, 1, 2, 2, 3, 3, 1 , 4]
    print(remove_duplicates(random_List))

if __name__ == '__main__':
    run()