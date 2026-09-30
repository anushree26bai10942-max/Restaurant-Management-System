def add_item(cursor, con):
    print("Add Item")
    name = input("Enter name of the product: ")
    price = int(input("Enter price of product: "))
    sql = "insert into menu values(%s,%s)"
    cursor.execute(sql, [name, price])
    con.commit()
    print("Successfully added item")

def delete_item(cursor, con):
    print("Delete Item")
    name = input("Enter name of the product: ")
    sql = "delete from menu where item=%s"
    cursor.execute(sql, [name])
    con.commit()
    print("Successfully deleted item")

def change_price(cursor, con):
    print("Change Item Price")
    name = input("Enter name of the product: ")
    price = int(input("Enter new price: "))
    sql = "update menu set price=%s where item=%s"
    cursor.execute(sql, [price, name])
    con.commit()
    print("Successfully changed item price")

def show_menu(cursor):
    print("Menu")
    cursor.execute("select * from menu")
    items = cursor.fetchall()
    for item in items:
        print(str(item[0]).ljust(43), item[1])
