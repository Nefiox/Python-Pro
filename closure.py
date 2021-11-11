# Hola 3 -> HolaHolaHola
# Jack 4 -> JackJackJackJack

# def make_repeater_of(n):
#     def repeater(string):
#         assert type(string) == str, "Solo puedes usar strings"
#         return string * n
#     return repeater


# def run():
#     repeater_5 = make_repeater_of(5)
#     print(repeater_5('Hello '))

#     repeater_10 = make_repeater_of(10)
#     print(repeater_10('Jack '))


# if __name__ == '__main__':
#     run()


def make_division_by(n):
    def divider(x):
        assert type(n) == int, "Solo puedes usar números enteros positivos"
        return x / n
    return divider


def run():

    division_by_3 = make_division_by(3)
    print(division_by_3(18)) # 6

    division_by_5 = make_division_by(5)
    print(division_by_5(100)) # 20

    division_by_18 = make_division_by(18)
    print(division_by_18(54)) # 3

if __name__ == '__main__':
    run()

    