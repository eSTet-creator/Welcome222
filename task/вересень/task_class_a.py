

purchases = []



def add_product(products_list, product):
    products_list.append(product)
    print(f"продукт {product} успішно додано!")



def del_product(products_list, product):
    if product in products_list:
        products_list.remove(product)
        print(f"продукт {product} успішно видалено!")
    else:
        print(f"продукту {product} немає в списку")



def show_list(products_list):
    print("поточний список продуктів:", products_list)


while True:
    try:
        decision = int(
        input(
            "\nобери дію \n1 - додати \n2 - видалити \n3 - переглянути вміст \n4 - вийти \nвведіть число: "
        )
    )
    except ValueError:
        print("Помилка! Нагадую для тупих - число від 1 до 4")
        continue

    if decision == 1:
        print("\nтут додавання")
        new_product = input("введіть назву продукту для додавання: ")

        add_product(purchases, new_product)

    elif decision == 2:
        print("\nтут видалення")
        remove_product = input("введіть назву продукту для видалення: ")

        del_product(purchases, remove_product)

    elif decision == 3:
        print("\nперегляд списку")

        show_list(purchases)

    elif decision == 4:
        print("\nвиходимо")
        break

    else:
        print("Заєб@л, нема такого пункту - дивись уважно!")