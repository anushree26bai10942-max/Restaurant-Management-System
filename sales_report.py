def display_sales(cursor):
    print("Sales")
    cursor.execute("select * from sales")
    records = cursor.fetchall()
    print("Item".ljust(20) + "Qty".ljust(20) + "Price".ljust(20) + "Amount".ljust(20) + "Date")
    for record in records:
        for value in record:
            print(str(value).ljust(20), end="")
        print()
