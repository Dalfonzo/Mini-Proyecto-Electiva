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
        if (option.lower() in ids):
            return option
        print("=> Debe seleccionar el tamaño correcto!!")


def ingredients_menu():
    while True:
        ids = []
        print("Ingredientes:")
        for ingredient in ingredients:
            ids.append(ingredient["id"])
            print(f'{ingredient["name"]} ( {ingredient["id"]} )')
        option = input('\nIndique ingrediente (enter para terminar):', end=' ')
        if (option.lower() in ids):
            # continue
            return option
        print("=> Debe seleccionar el ingrediente correcto!!")


def main_menu():
    print("*" * 30)
    print(f"*{'PIZZERIA UCAB'.center(28)}*")
    print("*" * 30)
    print("\nOpciones")
    size = size_menu()

    print(size)


menu()
# for x in ingredients:
#     print(x["name"])
