
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ").lower()
add_pepperoni = input("Do you want pepperoni? Y or N ").lower()
extra_cheese = input("Do you want extra cheese? Y or N ").lower()

bill = 0
if size == "l":
    bill = 25
    if add_pepperoni == "y":
        bill += 3
    if extra_cheese == "y":
        bill += 1
    print(f"Your final bill is: ${bill}")

if size == "m":
    bill = 20
    if add_pepperoni == "y":
        bill += 3
    if extra_cheese == "y":
        bill += 1
    print(f"Your final bill is: ${bill}")

if size == "s":
    bill = 15
    if add_pepperoni == "y":
        bill += 2
    if extra_cheese == "y":
        bill += 1
    print(f"Your final bill is: ${bill}")

