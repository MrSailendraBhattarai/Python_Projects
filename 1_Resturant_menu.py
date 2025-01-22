menu={
    'pizza':50,
    'pasta':80,
    'momo':100,
    'chowmein':70,
    'burger':100
}
next=True
total=0
print("***Welcome to Resturant***")
print("Our Menu")
# print("Pizza: Rs 50\npasta: Rs 80\nMoMo: Rs 100\nChowmein: Rs 70\nBurger: 100\n")

for item, price in menu.items():
    print(f"{item}: Rs {price}")


while next:
    item_1=input("What Do You Want To Order ?..")
    if item_1 in menu:
        total+=menu[item_1]
        print(f"Your Order {item_1} has been placed")
    else:
        print("Order According to menu...")

    next=input("Do You Want to Order next Item yes/No>>").lower()
    if next=='yes':
        next=True
    else:
        next=False

print("Your Total Bill is>>",total)