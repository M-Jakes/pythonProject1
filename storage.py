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
        "price": 60
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
    product_name = input("Název produktu:")
    product_price = input("Název cenu:")
    product2 = {
        'name': product_name,
        'price': product_price
    }
    products.append(product2)

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

def menu():
    print("Vítej ve skladu")
    print("###############\n")
    print("1. Výpis polože")
    print("2. Přidání položky")
    print("3. Hledání položky")
    print("4. Cena všech produktů")
    print("5. Nejlevnější produkt\n")

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

    else:
        print("Zadal jsi špatně!\n")
        menu()

menu()
