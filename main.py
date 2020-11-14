from datetime import datetime
from data import ingredients, sizes


def pizza_bill(pizza_size, extra_ing):
    """
    Esta función genera el resumen de pago para la pizza seleccionada.
    Recibe como parámetros un string con la opción del tamaño de la pizza
    y un list de ingredientes extras
    """
    size_list = list(filter(lambda el: el["id"] in pizza_size, sizes))
    subtotal = size_list[0]["price"]
    aux_list = []
    print(f"Usted seleccionó una pizza {size_list[0]['size']}", end=" ")
    if not extra_ing:
        print("Margarita\n")
    else:
        ing_list = list(filter(lambda el: el["id"] in extra_ing, ingredients))
        for ing in ing_list:
            subtotal += ing["price"]
            aux_list.append(ing["name"])
        print(f"con: {', '.join(aux_list)}\n")
    print(
        f"Subtotal a pagar por una pizza {size_list[0]['size']}: {subtotal:.1f}"
    )
    return subtotal


def save_file(total, client):
    """
    Esta función guarda la información de la venta en un archivo .txt
    Recibe como parametros el total de la venta y un Diccionario con la
    información del cliente
    """
    with open('data_file.txt', 'a') as writer:
        writer.write(str(total).ljust(10))
        writer.write(client["id"][:9].lower().ljust(10))
        writer.write(client["name"][:14].lower().ljust(15))
        writer.write(client["lname"][:14].lower().ljust(15))
        writer.write(datetime.today().strftime('%d-%m-%Y %H:%M:%S'))
        writer.write("\n")


def read_file():
    """
    Esta función lee la información del archivo data_file.txt
    y la imprime en pantalla
    """
    print("Ventas registradas:\n")
    print("Total".ljust(10) + "Cedula".ljust(10) + "Nombre".ljust(15) +
          "Apellido".ljust(15) + "Fecha y Hora")
    with open('data_file.txt', 'r') as reader:
        print(reader.read())
    input('\nPulse cualquier tecla para continuar...\n\n')


def check_new_order(ord_list, client):
    """
    Esta función verifica si el usuario desea otro pedido y retorna un boolean
    Recibe como parámetro un list con la orden y un diccionario con la
    información del cliente
    """
    total = sum(ord_list)
    while True:
        res = input("¿Desea continuar [s/n]?: ")
        print("*" * 30)
        if res.lower() == "n" or res.lower() == "s":
            break
        print("=> Debe seleccionar una opción correcta!!")
    if res.lower() == "n":
        print(
            f"El pedido tiene un total de {len(ord_list)} pizza(s) por un monto de {total:.1f}\n"
        )
        print("Gracias por su compra, regrese pronto")
        input('\nPulse cualquier tecla para continuar...\n\n')
        save_file(total, client)

    return res.lower() == "s"


def size_menu():
    """
    Esta función despliega un menú para elegir el tamaño de la pizza
    Retorna un string con la opción elegida
    """
    while True:
        ids = []
        print("Tamaños:", end=" ")
        for size in sizes:
            ids.append(size["id"])
            print(f"{size['size']} ( {size['id']} )", end=" ")
        print(":", end=" ")
        opt = input("")
        if opt.lower() in ids:
            selected = list(filter(lambda el: el["id"] == opt.lower(), sizes))
            print(f"Tamaño seleccionado: {selected[0]['size']}\n")
            return opt
        print("=> Debe seleccionar el tamaño correcto!!")


def ingredients_menu():
    """
    Esta función muestra un menú de ingredientes
    Retorna una lista con las opciones elegidas
    """
    extra_ing, ids = [], []
    print("Ingredientes:")
    for ing in ingredients:
        ids.append(ing["id"])
        print(f"{ing['name']} ( {ing['id']} )")
    print()
    while True:
        option = input("Indique ingrediente (enter para terminar): ")
        if option.lower() in ids:
            extra_ing.append(option.lower())
        elif option == "":
            return extra_ing
        else:
            print("=> Debe seleccionar un ingrediente correcto!!\n")


def client_menu():
    """
    Esta función solicita y valida la información del usuario
    retorna un diccionario con la información
    """
    client = {}
    while True:
        res = input("Indique su primer nombre: [Ej: Jose]: ")
        if res.isalpha():
            client["name"] = res
            break
        print("=>Inserte un nombre valido")
    while True:
        res = input("Indique su apellido: [Ej: Suarez]: ")
        if res.isalpha():
            client["lname"] = res
            break
        print("=>Inserte un apellido valido")
    while True:
        res = input("Indique su cedula de identidad: ")
        if res.isnumeric() and int(res) > 0 and int(res) < 100000000:
            client["id"] = res
            break
        print("=>Inserte un numero de cedula valido")
    print("*" * 30)
    print()
    return client


def order_menu():
    """
    Esta función ejecuta el ciclo de compra para n pizzas
    que el usuario solicite
    """
    order_list = []
    hr_line = "*" * 30
    print(hr_line)
    print(f"*{'PIZZERIA UCAB'.center(28)}*")
    print(hr_line)
    client = client_menu()
    while True:
        print(f"Pizza número {len(order_list) + 1}")
        print("\nOpciones")
        size = size_menu()
        extra_ing = ingredients_menu()
        order_list.append(pizza_bill(size, extra_ing))
        print(hr_line)
        if not check_new_order(order_list, client):
            break


def main_menu():
    while True:
        print('*' * 30 + '\n')
        print("Bienvenido, por favor seleccione una opción:\n")
        print("0 - Salir")
        print("1 - Registrar nueva venta")
        print("2 - Ver registro de ventas")
        opc = int(input())
        switch = {
            0: exit,
            1: order_menu,
            2: read_file,
        }
        print('\n' * 2 + '*' * 30)
        switch.get(opc,
                   lambda: print('=> Opción invalida, intente de nuevo!'))()


if __name__ == "__main__":
    main_menu()
