import os
from restaurant.management import add_item_to_tab, calculate_tab, get_item

TABLE_TAB = []


def initial_screen():
    os.system("clear")

    while True:
        print("1. Adicionar item a comanda")
        print("2. Fechar comanda")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            os.system("clear")
            add_item_screen()

        elif choice == "2":
            os.system("clear")
            check_out_screen()

        else: 
            os.system("clear")
            print("Escolha uma opção válida (1, 2) \n")


def add_item_screen():

    os.system("clear")

    while True:

        id_item = int(input("Digite o id do item: "))
        quantity_item = int(input("Digite a quantidade desejada: "))

        find_product = add_item_to_tab(TABLE_TAB, (id_item), (quantity_item))
        if find_product:
            products = get_item(id_item)    
            print(products)
            os.system("clear")
            if products:
                print(f'{quantity_item} {products["name"]} adicionados a comanda!')

            back = input("Digite 'back' para voltar ou aperte 'enter' para continuar: ")    

            if back.upper() == "BACK":
                os.system("clear")
                initial_screen()    
            else:
                add_item_screen()
        else:
            print(f'{id_item} não é um id de item válido')
            break
    initial_screen()
   



def check_out_screen():
    numero_item = 0
    for products in TABLE_TAB:
        numero_item += 1
        print(f'Item {numero_item}: {products["amount"]} {products["name"]} - R$ {products["price"] * products["amount"]: .2f}') 
    print("---------------------------------------")
    print(f'Total - {calculate_tab(TABLE_TAB): .2f}')
    exit_system = input("Digite F para finalizar o sistema: \n")

    if exit_system.upper() == "F":
        os.system("clear")
        os.abort()
    
    check_out_screen()