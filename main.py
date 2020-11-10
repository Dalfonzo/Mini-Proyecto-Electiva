sizes = [
    {
        "size": "Grande",
        "price": 580,
        "id": "g"
    },
    {
        "size": "Mediana",
        "price": 430,
        "id": "m"
    },
    {
        "size": "Personal",
        "price": 280,
        "id": "p"
    },
]

ingredients = [
    {
        "name": "Jamón",
        "price": 40,
        "id": "ja"
    },
    {
        "name": "Champiñones",
        "price": 35,
        "id": "ch"
    },
    {
        "name": "Pimentón",
        "price": 30,
        "id": "pi"
    },
    {
        "name": "Doble queso",
        "price": 40,
        "id": "dq"
    },
    {
        "name": "Aceitunas",
        "price": 57.5,
        "id": "ac"
    },
    {
        "name": "Pepperoni",
        "price": 38.5,
        "id": "pp"
    },
    {
        "name": "Salchichón",
        "price": 62.5,
        "id": "sa"
    },
]


def size_menu():
    while True:
        ids = []
        print("Tamaños:", end=' ')
        for size in sizes:
            ids.append(size["id"])
            print(f'{size["size"]} ( {size["id"]} )', end=' ')
        print(":", end=' ')
        option = input('')
        if option.lower() in ids:
            return option
        print("=> Debe seleccionar el tamaño correcto!!")


def ingredients_menu():
    extra_ing = set()
    while True:
        ids = []
        print("Ingredientes:")
        for ing in ingredients:
            ids.append(ing["id"])
            print(f'{ing["name"]} ( {ing["id"]} )')
        option = input('\nIndique ingrediente (enter para terminar): ')
        if option.lower() in ids:
            extra_ing.add(option.lower())
        elif option == "":
            return list(extra_ing)
        else:
            print("=> Debe seleccionar un ingrediente correcto!!\n")


def generate_bill(pizza_size, extra_ing):
    size_list = list(filter(lambda el: el["id"] in pizza_size, sizes))
    subtotal = size_list[0]["price"]
    print(f"Usted seleccionó una pizza {size_list[0]['size']}", end=" ")
    if not extra_ing:
        print("Margarita\n")
    else:
        ing_list = list(filter(lambda el: el["id"] in extra_ing, ingredients))
        print("con: ", end=" ")
        for ing in ing_list:
            subtotal += ing["price"]
            print(ing["name"], end=" ")
        print("\n")  #Cambiar
    print(f"Subtotal a pagar por una pizza {size_list[0]['size']}: {subtotal}")
    return subtotal


def main_menu():
    hr_line = "*" * 30
    print(hr_line)
    print(f"*{'PIZZERIA UCAB'.center(28)}*")
    print(hr_line)
    print("\nOpciones")
    size, extra_ing = size_menu(), ingredients_menu()
    generate_bill(size, extra_ing)
    print(hr_line)

    print(extra_ing)
    print(size)


main_menu()
