from decisions import dict_dec
from def_decision import decisions

plan, directions = decisions()

if plan == 0:
    print("Подходящего факультета нет")
else:
    for direct in directions:
        print("\nФакультет/Институт: ", dict_dec[direct]["Факультет/Институт"], end="\n")
        print("Направление: ", direct, end="\n")

        if plan == "Платное":
            print("Цена за год: ", dict_dec[direct][plan]["Цена"], end="\n")

        print("Количество мест: ", dict_dec[direct][plan]["Мест"], end="\n")

        print("\nПроходные баллы:\nРусский: ", dict_dec[direct][plan]["Русский"], end="\n")
        print("Математика: ", dict_dec[direct][plan]["Математика"], end="\n")

        if dict_dec[direct][plan]["Информатика"] != 0:
            print("Информатика: ", dict_dec[direct][plan]["Информатика"], end="\n")

        if dict_dec[direct][plan]["Физика"] != 0:
            print("Физика: ", dict_dec[direct][plan]["Физика"], end="\n")

        print("\nОбщая сумма проходных баллов: ", dict_dec[direct][plan]["Проходной балл"], end="\n")
        print("_________________________", end="\n")
