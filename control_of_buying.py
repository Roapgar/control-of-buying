sum_of_buyig = 0
count = 0
price = 0
buying = True
start_sum = 0
list_of_products = []
write_list = True

def itogi():
    global buying
    global sum

    if sum <= 0:

        print("\n")
        print("=" * 20)
        print(f"""Количество покупок: {count}
Общая сумма покупок: {sum_of_buyig}
Затратыы выше бюджета: {abs(sum)}""")
        print("=" * 20)
        print("\n")

    else:
        print("\n")
        print("=" * 20)
        print(f"""Количество покупок: {count}
Общая сумма покупок: {sum_of_buyig}
Нынешний бюджет: {sum}""")
        print("=" * 20)
        print("\n")



print("Добро пожаловать!!\n")
print("Когда вам понадобиться прекратить покупки введите -1")

sum = int(input("Введите бюджет на покупки:"))
print(f"Ваш бюджет {sum} \n")

start_sum = sum



while write_list == True:

    x = input("Введите название продукта: ")

    if x == "-1":
        write_list = False
        break

    list_of_products.append(x.upper())

print(f"{list_of_products}\n")



while buying == True:

    price = int(input("Введите стоимомть данной покупки:"))

    if price == -1:
        break

    elif price >= sum:
        print("""ПРЕДУПРЕЖДЕНИЕ!!!!!
ВЫ ВЫШЛИ ЗА РАМКИ БЮДЖЕТА
СОВЕТУЮ ПРЕКРАЩАТЬ ПОКУПКИ""")
        #continue

    for i in range(len(list_of_products)):
        print(f"{i + 1}. {list_of_products[i]}\n")

    number = int(input("""Какой продукт вы хотите купить?
Напишите цифру под каким номером стоит нужный продукт"""))

    del list_of_products[number - 1]

    count +=1
    sum_of_buyig += price
    sum -= price

    if sum <=0:

        print("\n")
        print("=" * 20)
        print(f"""Количество покупок: {count}
Ценна данной покупки: {price}
Общая сумма покупок: {sum_of_buyig}
Затратыы выше бюджета: {abs(sum)}""")
        print("=" * 20)
        print("\n")

    else:
        print("\n")
        print("=" * 20)
        print(f"""Количество покупок: {count}
Ценна данной покупки: {price}
Общая сумма покупок: {sum_of_buyig}
Нынешний бюджет: {sum}""")
        print("=" * 20)
        print("\n")


    #if sum == 0:
        #print("Извините, но ваш бюджет закончился, спасибо что использовали ту программу")
        #itogi()

    if list_of_products == []:
        print("Вы купили все не обходимое можете идти на кассу")
        print("спасибо что использовали эту программу")


itogi()
print("Досвидание!")
