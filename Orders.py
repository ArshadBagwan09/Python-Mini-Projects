foods = []
prices = []
total = 0

while True:
    food = input("Enter the foods = ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Ener the foods prices of a {food} :$"))
        foods.append(food)
        prices.append(price)

print("----Your Catrs----")
for food in foods:
    print(food, end=" ")
print()
for price in prices:
    print(price, end=" ")

print()
print("---Total Bills----")
for price in prices:
    total += price
print()
print(f"Your Total Bills in Order {total} $")
