nums = [1, 2, 212]

while True:
    print(f"Все числа {nums}")
    print("1 добавить число")
    print("2 удалить число")
    print("3 выход")

    act = input("выберите действие: ")

    if act == "1":
        try:
            add = int(input("введите число для добавления"))
            nums.append(add)
            print(f"число {add} добавлено")
        except ValueError:
            print("вы ввели не число")

    elif act == "2":
        try:
            rem = int(input("введите число для удаления: "))
            if rem in nums:
                nums.remove(rem)
                print(f"число {rem} удалено")
            else:
                print("числа нет в списке")
        except ValueError:
            print("вы ввели не число")

    elif act == "3":
        print("пока!")
        break
