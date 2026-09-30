def create_bill(cursor, con):
    print("Menu")
    cursor.execute("select * from menu")
    menu_items = cursor.fetchall()
    for item in menu_items:
        print(str(item[0]).ljust(43), item[1])

    choice = "y"
    total_bill = 0
    ordered_items = []
    ordered_amounts = []

    while choice == "y":
        name = input("Enter name of the item: ")
        qty = int(input("Enter quantity: "))
        found = 0
        for item in menu_items:
            if name.lower() == item[0].lower():
                total_bill += (item[1] * qty)
                ordered_items.append(name)
                ordered_amounts.append(item[1] * qty)
                sql = "insert into sales values(%s,%s,%s,%s,now())"
                cursor.execute(sql, [name, qty, item[1], item[1] * qty])
                con.commit()
                found = 1  
        if found == 0:
            print("Item is not available")
        choice = input("Do you wish to add a new item(y/n): ")

    print("Items ordered")
    for i in range(len(ordered_items)):
        print(ordered_items[i], ":", ordered_amounts[i])
    print("Total Amount:", total_bill)
    print("Thank You")
