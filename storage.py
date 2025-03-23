products = [
    {
        "name": "Audi",
        "price": 50
    },
    {
        "name": "Audi A8",
        "price": 60
    },
    {
        "name": "Mercedes",
        "price": 80
    },
    {
        "price": 30,
        "name": "BMW R8",
    },
    {
        "name": "BMW",
        "price": 30
    }
]

def print_products():
    for product in products:
        print(f"Název produktu: {product['name']}, cena: {product['price']}$")


def add_product():
    product_name = input("Název produktu: ")

    while True:
        try:
            product_price = float(input("Cena produktu: "))
            if product_price < 0:
                print("Cena musí být kladné číslo!")
                continue
            break
        except ValueError:
            print("Zadej pouze číslo.")

    product = {
        'name': product_name,
        'price': product_price
    }

    products.append(product)
    print("Produkt byl úspěšně přidán!\n")

def search_product():
    query = input("Zadej název nebo část názvu produktu: ").lower()
    found = []

    for product in products:
        if query in product['name'].lower():
            found.append(product)

    if len(found) > 0:
        for product in found:
            print("Název:", product['name'], ", Cena:", product['price'], "$")
    else:
        print("Žádné produkty nenalezeny.")


def total_price():
    total = 0
    for product in products:
        total += product['price']
    print("Celková cena všech produktů:", total, "$")


def cheapest_price():
    min_price = 0
    cheap_products = []
    for product in products:
        if min_price == 0 or product['price'] < min_price:
            min_price = product['price']
            cheap_products = [product]
        elif product['price'] == min_price:
            cheap_products.append(product)
    print("Nejlevnější produkt:")
    for product in cheap_products:
        print("Název:", product['name'], ", Cena:", product['price'], "$")


def most_expensive_price():
    max_price = 0
    expensive_products = []
    for product in products:
        if max_price == 0 or product['price'] > max_price:
            max_price = product['price']
            expensive_products = [product]
        elif product['price'] == max_price:
            expensive_products.append(product)
    print("Nejdražší produkt:")
    for product in expensive_products:
        print("Název:", product['name'], ", Cena:", product['price'], "$")


def average_price():
    total = 0
    count = 0
    for product in products:
        total += product['price']
        count += 1

    if count > 0:
        avg = total / count
        print("Průměrná cena produktů:", avg, "$")
    else:
        print("Nebyly nalezeny žádné produkty")


def edit_product():
    if len(products) == 0:
        print("Žádné produkty k úpravě.")
        return
    print("Seznam produktů:")
    index = 0
    for product in products:
        print(index, "-", product['name'], ":", product['price'], "$")
        index += 1
    try:
        index = int(input("Zadejte číslo produktu, který chcete upravit: "))
        if index < 0 or index >= len(products):
            print("Neplatné číslo produktu.")
            return
    except ValueError:
        print("Musíte zadat číslo!")
        return
    product = products[index]
    original_name = product['name']
    original_price = product['price']

    changed = False

    change_name = input("Chcete změnit název? (ano/ne): ").strip().lower()
    if change_name == "ano":
        new_name = input("Zadej nový název: ")
        if new_name and new_name != original_name:
            product['name'] = new_name
            changed = True

    change_price = input("Chcete změnit cenu? (ano/ne): ").strip().lower()
    if change_price == "ano":
        try:
            new_price = float(input("Zadejte novou cenu: "))
            if new_price != original_price:
                product['price'] = new_price
                changed = True
        except ValueError:
            print("Neplatná cena!")

    if changed:
        print("Produkt byl upraven.")
    else:
        print("Produkt nebyl změněn.")


def menu():
    print("VÍTEJ VE SKLADU\n")
    print("Vyber jednu z možností níže\n")
    print("1. Výpis položek")
    print("2. Přidání položky")
    print("3. Hledání položky")
    print("4. Cena všech produktů")
    print("5. Nejlevnější produkt")
    print("6. Nejdražší produkt")
    print("7. Průměrná cena produktů")
    print("8. Upravit produkt\n")

    choice = int(input("Volba: "))

    if choice == 1:
        print("Položky na skladě jsou:")
        print_products()
        print("")
        menu()

    elif choice == 2:
        print("Přidání položky")
        add_product()
        print("")
        menu()

    elif choice == 3:
        print("Hledání pooložky")
        search_product()
        print("")
        menu()

    elif choice == 4:
        print("Cena všech produktů")
        total_price()
        print("")
        menu()

    elif choice == 5:
        print("Nejlevnější produkt")
        cheapest_price()
        print("")
        menu()

    elif choice == 6:
        print("Nejdrařší produkt")
        most_expensive_price()
        print("")
        menu()

    elif choice == 7:
        print("Průměrná cena produktů")
        average_price()
        print("")
        menu()

    elif choice == 8:
        print("Upravit produkt")
        edit_product()
        print("")
        menu()

    else:
        print("Zadal jsi špatně!\n")
        menu()


menu()
