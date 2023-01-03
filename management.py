from restaurant.menu import AVAILABLE_MENU


def get_item(item_id: int):
    for product in AVAILABLE_MENU:
        if product["id"] == item_id:
            return product


def add_item_to_tab(table_tab: list, item_id: int, amount: int):
    find_product = get_item(item_id=item_id)
    
    if find_product:
        table_tab.append({"id": find_product["id"],
        "name": find_product["name"],
        "price": find_product["price"],
        "amount": amount})
        return True


def calculate_tab(table_tab: list):
    soma = 0
    for product in table_tab:
        soma += product["price"] * product["amount"]
        
    return soma