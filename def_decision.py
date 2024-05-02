from def_only_physics import only_physics
from def_only_it import only_it
from def_physics_and_math import physics_it


def decisions():
    print("Введите баллы за экзамены (если экзамен не сдавался, введите 0):\n")

    rus = int(input("Русский: "))
    math = int(input("Математика: "))
    it = int(input("Информатика: "))
    physics = int(input("Физика: "))

    if rus == 0 or math == 0:
        print("Ошибка: один из обязательных экзаменов не сдан\n")
        direction = decisions()
        return direction
    if it == 0 and physics == 0:
        print("Ошибка: для выбора направления должен быть сдан хотя бы один из экзаменов: физика или математика\n")
        direction = decisions()
        return direction
    if rus < 0 or math < 0 or it < 0 or physics < 0:
        print("Ошибка: некоторые баллы отрицательны\n")
        direction = decisions()
        return direction

    summary = rus + math + it + physics
    print("\nОбщая сумма баллов: ", summary, end="\n")

    while True:
        print("\nВыберите в какой сфере программирование вас интересует:\n"
              "1 - Чистое программирование\n"
              "2 - Программирование и математика\n"
              "3 - Программирование и физика\n"
              "4 - Программирование и экономика\n")

        sphere = int(input())

        if 1 <= sphere <= 4:
            break

        print("\nОшибка: выбран элемент не из списка, попробуйте ещё раз\n")

    while True:
        print("\nВыберите на какой основе вы хотите поступать:\n"
              "1 - Бюджетная основа\n"
              "2 - Платная основа\n")

        plan = int(input())

        if 1 <= plan <= 2:
            break

        print("\nОшибка: выбран элемент не из списка, попробуйте ещё раз\n")

    if it == 0:
        return only_physics(rus, math, physics, summary, sphere, plan)
    if physics == 0:
        return only_it(rus, math, it, summary, sphere, plan)

    return physics_it(rus, math, it, physics, summary, sphere, plan)

