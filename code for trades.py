for i in range(1,50):
    lisskins=int(input("Лис: "))
    market=int(input("Маркет: "))
    viruchka = int((market - (lisskins*1.05)) * 0.9025)
    print("Выручка:", viruchka)
    if viruchka<2000:
        print(">Не стоит<")
    if 2000<viruchka<3000:
        print(">Хороший выбор<")
    if 3000<viruchka<5000:
        print(">Отличный скин<")
    if viruchka>5000:
        print(">Сорвал куш<")