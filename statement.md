# Problem Statement

Most small restaurants and food counters still run on manual registers, notebooks, or just memory when it comes to managing their menu, billing customers, and keeping track of sales. This causes a lot of avoidable problems — wrong prices being charged, sales records getting lost or never written down properly, and basically no easy way to look back and see how the business has been doing over time. What's needed is something simple: a lightweight, database-backed system that a cashier can run straight from a terminal to manage the menu, generate correct bills, and keep a proper sales history — without needing to invest in an actual POS hardware setup.

## Scope of the Project

This project focuses on three core things a small restaurant actually needs:

- **Menu management** — adding, deleting, updating, and viewing menu items and their prices
- **Billing** — taking an order, looking up prices, calculating the bill, and logging the sale
- **Sales reporting** — being able to see all past transactions in one place

To keep things realistic for the scope of this course project, it's built as a **single-outlet, single-user-at-a-time console application**. Things like inventory tracking, handling multiple branches, or a proper GUI/web interface are left out on purpose — those are mentioned as possible future improvements in the project report, but weren't part of what I was trying to solve here.

## Who This Is For

- Cashiers at small restaurants or cafes who take orders and bill customers at the counter
- Owners or managers who need to update prices on the menu or check how sales have been going
- Small food businesses that want a cheap, easy way to go digital instead of relying on manual registers

## What the System Actually Does

1. Lets you add, delete, and update the price of menu items, and view the current menu anytime
2. Generates a bill by picking items and quantities — it checks against the live menu automatically and calculates the total for you
3. Logs every billed item into a `sales` table, so there's a complete, searchable record of every transaction
4. Shows a full sales report of everything ever billed — item, quantity, price, amount, and date
5. Runs on a simple numbered menu in the terminal, so no technical knowledge is needed to use it
