for i in range(1,50):
    lisskins=int(input("Лис: "))
    market=int(input("Маркет: "))
    viruchka=int((market*0.9025 - lisskins*1.05))
    print("Выручка:", viruchka)
    if viruchka<1000:
        print(">Не стоит<")
    if 1000<viruchka<2000:
        print(">Хороший выбор<")
    if 2000<viruchka<3000:
        print(">Отличный скин<")
    if viruchka>3000:
        print(">Сорвал куш<")