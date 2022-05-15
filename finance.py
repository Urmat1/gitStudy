print("Учет заработка и расходов")

while True:
    a = input("Введите ваш уровень заработка за текущий период:")
    if a == '':
        print("Ошибка! Заполните данные !")
    else:
        break
h = float(a)
while True:
    b = input("На продукты питания:")
    if b =='':
        print("Ошибка! Заполните данные !")
    else:
        break
v = float(b)
while True:
    g = input("На коммунальные услуги:")
    if g =='':
        print("Ошибка! Заполните данные !")
    else:
        break
f = float(g)
while True:
    i = input("На средства передвижения:")
    if i =='':
        print("Ошибка! Заполните данные !")
    else:
        break
s = float(i)

eat = (100/(h/v))
print("Ваши траты на продукты составляют:" + " " + str(round(eat, 1)) + "%" + "От вашего дохода")

uslugi = (100/(h/f))
print("Ваши траты на коммунальные услуги составляют:" + " " + str(round(uslugi, 1)) + "%" + "От вашего дохода")

fuel = (100/(h/s))
print("Ваши траты на передвижение:" + " " + str(round(fuel, 1)) + "%" + "От вашего дохода")

total = (h - v - f - s)
print("Остаток за текущий период составляет:" + " " + str(round(total, 1)) + "сом." )




