#цикл для вывода всех склонений.


number = int(input("Введите число от 1 до 20"))

if number > 20:
    print("Число больше 20")
elif number < 1:
    print("Число меньше 1")
elif number > 4:
    print(number, "процентов")
elif number < 2:
    print(number, "процент")
else:
    print(number, "процента")


print("Все склонения:")
number = 0

while number < 20 or number == 20:
    if number > 4:
        print(number, "процентов")
    elif number < 2:
        print(number, "процент")
    else:
        print(number, "процента")
    number += 1