# Shopping Cart Program

foods=[]
prices=[]
total=0
print("Welcome To Shopping Cart Program")
while True:
    food=input("Enter Foods (E for Exit)>>>")
    if food.lower()=='e':
        break
    else:
        price=float(input(f"Enter Price of {food}: Rs."))
        foods.append(food)
        prices.append(price)


print("-----YOUR CART-----")
for food in foods:
    print(food)

for price in prices:
    total+=price
print(f"Your Total is: Rs.{total}")