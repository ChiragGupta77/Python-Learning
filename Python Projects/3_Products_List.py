# Products List Manager
products = []
while True:
    print("\n-----ADD PRODUCT-----")
    add_name = input("Name of the product to be added:")
    try:
        add_price = float(input("Price of the product:"))
    except ValueError:
        print("Please enter float value only")
        continue
    try:
        add_quantity = int(input("Quantity of the product:"))
    except ValueError:
        print("Please enter integer value only")
        continue
    product_dict = {"name": add_name, "price": add_price,
                        "quantity": add_quantity}
    products.append(product_dict)
    print("\n-----INVENTORY-----")
    for i in products:
        print(f"{i}\n")
    grand_total = 0
    for items in products:
        total_value = items["price"] * items['quantity']
        grand_total += total_value
        print(f"Total value of product \"{items['name']}\" --- {total_value}")
    print(f"The Total inventory value --- {grand_total}")
    leave = input("\nType 'e' to exit or press enter to continue")
    if leave.upper() == 'E':
        break
