# PART 2: DATA STRUCTURES - RESTAURANT MENU & ORDER MANAGEMENT SYSTEM

# Given:
menu = {
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price":  40.0, "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price":  90.0, "available": True},
    "Rasgulla":       {"category": "Desserts",  "price":  80.0, "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}

inventory = {
    "Paneer Tikka":   {"stock": 10, "reorder_level": 3},
    "Chicken Wings":  {"stock":  8, "reorder_level": 2},
    "Veg Soup":       {"stock": 15, "reorder_level": 5},
    "Butter Chicken": {"stock": 12, "reorder_level": 4},
    "Dal Tadka":      {"stock": 20, "reorder_level": 5},
    "Veg Biryani":    {"stock":  6, "reorder_level": 3},
    "Garlic Naan":    {"stock": 30, "reorder_level": 10},
    "Gulab Jamun":    {"stock":  5, "reorder_level": 2},
    "Rasgulla":       {"stock":  4, "reorder_level": 3},
    "Ice Cream":      {"stock":  7, "reorder_level": 4},
}

sales_log = {
    "2025-01-01": [
        {"order_id": 1,  "items": ["Paneer Tikka", "Garlic Naan"],          "total": 220.0},
        {"order_id": 2,  "items": ["Gulab Jamun", "Veg Soup"],              "total": 210.0},
        {"order_id": 3,  "items": ["Butter Chicken", "Garlic Naan"],        "total": 360.0},
    ],
    "2025-01-02": [
        {"order_id": 4,  "items": ["Dal Tadka", "Garlic Naan"],             "total": 220.0},
        {"order_id": 5,  "items": ["Veg Biryani", "Gulab Jamun"],           "total": 340.0},
    ],
    "2025-01-03": [
        {"order_id": 6,  "items": ["Paneer Tikka", "Rasgulla"],             "total": 260.0},
        {"order_id": 7,  "items": ["Butter Chicken", "Veg Biryani"],        "total": 570.0},
        {"order_id": 8,  "items": ["Garlic Naan", "Gulab Jamun"],           "total": 130.0},
    ],
    "2025-01-04": [
        {"order_id": 9,  "items": ["Dal Tadka", "Garlic Naan", "Rasgulla"], "total": 300.0},
        {"order_id": 10, "items": ["Paneer Tikka", "Gulab Jamun"],          "total": 270.0},
    ],
}
print()
print()
# TASK 1: Explore the Menu
print(" MENU ")
print()
category = ["Starters", "Mains", "Desserts"]
for grp in category:
    print(f" {grp} ")
    for item, info in menu.items():
        if info["category"] == grp:
            status = "Available" if info["available"] else "Unavailable"
            print(f"{item:<18} ₹{info['price']:.2f}   [{status}]")
    print()
    print()

# Find Details regarding Menu using dictionary methods
# TOTAL number of items available on the Menu:
print("Total no. items on the Menu: ", len(menu))
print()
#Total number of items available:
count = sum(1 for item in menu if menu[item]["available"])
print("No. of available items: ",count)
print()
#The most expensive item (name + price)
item = max(menu, key=lambda x: menu[x]["price"])
print("The most expensive item: ",item, "₹",menu[item]["price"])
print()
#All items priced under ₹150 (name + price)
print("All items under ₹150: ")
for items, details in menu.items():
    if details["price"] < 150:
        print(items, ":", "₹",details["price"])    
print()
print()
print()
# TASK 2: Cart Operations 
print(" CART OPERATIONS ")
print()
cart = []
def add_item(name, qty):
    if name not in menu:
        print("Invalid! Item not found in menu.")
        return
    if not menu[name]["available"]:
        print("Item is unavailable.")
        return
    for item in cart:
        if item["item"] == name:
            item["quantity"] += qty
            return
    cart.append({"item": name, "quantity": qty, "price": menu[name]["price"]})

def remove_item(name):
    for item in cart:
        if item["item"] == name:
            cart.remove(item)
            return
    print("Item not in cart.")

# Requirements
add_item("Paneer Tikka",2)
print(cart)
print()
add_item("Gulab Jamun",1)
print(cart)
print()
add_item("Paneer Tikka",1)
print(cart)
print()
add_item("Mystery Burger",1)
print()
add_item("Chicken Wings",1)
print()
remove_item("Gulab Jamun")
print(cart)
print()
# Order Summary
print(" Order Summary ")
total= 0
for item in cart:
    total_price = item["quantity"] * item["price"]
    total += total_price
    print(f"{item['item']:<18} x{item['quantity']}    ₹{total_price:.2f}")
gst = total * 0.05
total_amt = total + gst

print("------------------------------------")
print(f"Subtotal:                ₹{total:.2f}")
print(f"GST:                     ₹ {gst:.2f}")
print(f"Total:                   ₹{total_amt:.2f}")
print("====================================")
print()
print()
print()
# TASK 3: Inventory Tracker with Deep Copy
print(" INVENTORY TRACKER ")
print()
import copy
inventory_backup = copy.deepcopy(inventory)
# change one stock value
inventory["Dal Tadka"]["stock"] = 13
print("Modification of original inventory:", inventory["Dal Tadka"])
print()
print("Backup inventory:", inventory_backup["Dal Tadka"])
print()
# Deduct the quantities from the final cart in Task 2
for items in cart:
    name = items["item"]
    qty = items["quantity"]
    if inventory[name]["stock"] < qty:
        print(f"Low in stock for: ", name)
        inventory[name]["stock"] = 0
    else:
        inventory[name]["stock"] -= qty
print()
# Reorder alert
for items, data in inventory.items():
    if data["stock"] <= data["reorder_level"]:
        print(f"⚠ Reorder Alert: ,{items}, — Only {data['stock']} left")
print()
print("Checking if the backup has remained unchanged:")
print(inventory_backup["Paneer Tikka"])
print()
# Print both inventory and inventory_backup at the end to confirm they differ
# To prove the deep copy protected the original.
print("Checking if there has been a change in Original Inventory")
print(inventory)
print()
print("Checking if the Backup Inventory has remained unchanged:")
print(inventory_backup)
print()
print()
print()
# TASK 4: Daily Sales Log Analysis
print(" Daily Sales Log Analysis ")
print()
# Total revenue per day
daily_rev = {}
for date, orders in sales_log.items():
    total = sum(order["total"] for order in orders)
    daily_rev[date] = total
    print(date, ":", total)
print()
# The best-selling day (date with the highest total revenue)
day = max(daily_rev, key=daily_rev.get)
print("The best selling day is:",day)
print()
# The most ordered item across all days
ct_items = {}
for orders in sales_log.values():
    for order in orders:
        for item in order["items"]:
            ct_items[item] = ct_items.get(item, 0) + 1
most_ordered = max(ct_items, key=Ct_items.get)
print("The most ordered item is:", most_ordered)
print()
# Adding New Day to Sales Log
sales_log["2025-01-05"] = [{"order_id": 11, "items": ["Butter Chicken", "Gulab Jamun", "Garlic Naan"], "total": 490.0},
    {"order_id": 12, "items": ["Paneer Tikka", "Rasgulla"], "total": 260.0},]
print("New Revenue=")
for date, orders in sales_log.items():
    tot = sum(order["total"] for order in orders)
    print(date, ":", tot)
print()
# Print a numbered list of all orders across all dates (including the new day)
print("List of all orders:")
count = 1
for date, orders in sales_log.items():
    for order in orders:
        it = ", ".join(order["items"])
        print(f"{count}. [{date}] Order #{order['order_id']} — ₹{order['total']} — Items: {it}")
        count += 1
