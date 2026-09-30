# Restaurant Management System


This is a simple console-based Restaurant Management System I built using Python and MySQL. It's a project for my VITyarthi "Build Your Own Project" flipped-course evaluation.

The idea came from thinking about how small restaurants (like the ones near my hostel/campus) still manage their menu and billing on paper or in random notebooks. That means a lot of manual work — pricing mistakes, no record of what was sold, no proper sales history. So I decided to make a small terminal-based application that handles the whole thing: menu, billing, and sales tracking, all connected to a MySQL database.

## What it does

- **Menu Management** — you can add new items with a price, delete items you don't want anymore, update the price of an existing item, or just view the whole menu.
- **Billing** — pick items and quantities, and the system generates a bill for you. It checks against the current menu so you can't accidentally bill something that doesn't exist. Every item billed gets stored in a `sales` table so nothing is lost.
- **Sales Report** — shows every transaction that has ever been billed, with item name, quantity, price, amount, and date, all lined up nicely.

## Tools used

- Python 3
- MySQL 8.x
- `mysql-connector-python` for connecting Python to the database
- Plain command-line interface (no GUI, kept it simple)

## Files in the project

```
restaurant-management-system/
├── main.py               → connects to DB, sets up tables, runs the main menu
├── menu_management.py    → add / delete / update price / show menu
├── billing.py             → generates bills and logs sales
├── sales_report.py        → shows the sales report
├── README.md
└── statement.md            → problem statement (required for VITyarthi submission)
```

## How to run it

First install the MySQL connector:

```bash
pip install mysql-connector-python
```

Make sure MySQL server is running on your machine, and you know your root password.

In `main.py`, update the connection line with your own credentials if needed:

```python
con = mysql.connector.connect(host="localhost", user="root", password="YOUR_PASSWORD")
```

Then just run:

```bash
python main.py
```

The database and tables (`menu`, `sales`) get created automatically the first time you run it, so you don't need to set anything up manually in MySQL.

## Menu options

When you run it, this is what shows up:

```
1.Add Item
2.Delete Item
3.Change price of an item
4.Show Menu
5.Generate Bill
6.Display Sales
7.Exit
Enter your choice:
```

Just type the number and follow the prompts.

## How I tested it

1. Added a couple of items through option 1, e.g. `Biriyani` priced at `180`.
2. Checked option 4 to make sure they actually got added.
3. Used option 5 to generate a bill, entered an item and quantity, and checked the total came out right.
4. Tried billing something that wasn't on the menu on purpose — it correctly says "Item is not available" instead of throwing an error.
5. Checked option 6 to see if that transaction showed up with the right date.
6. Changed the price of an item with option 3, then checked option 4 again to confirm it updated.
7. Deleted an item with option 2 and confirmed it disappeared from the menu.
8. Exited using option 7 — it prints a "Thank You" message and closes properly.

## Screenshots

Screenshots of the terminal (Show Menu, Generate Bill, etc.) along with the diagrams — architecture, use case, workflow, sequence, component and ER — are in the project report PDF submitted alongside this.

## Author

Made individually for the VITyarthi "Build Your Own Project" flipped-course evaluation.

