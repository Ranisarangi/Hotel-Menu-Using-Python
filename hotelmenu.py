"""
This project is a simple restaurant ordering system implemented in Python. It allows users to order food items from a predefined menu,
calculates the total bill, and displays the final amount to be paid. The system is interactive and ensures a smooth orderingprocess with
basic input validation.
"""
menu={
    'Pizza':40,
    'Pasta':50,
    'Burger':60,
    'Salad':70,
    'coffee':80,
}
print("welcome to PYTHON RESTURANT")
print("Pizza:Rs40\nPasta:Rs50\nBurger:Rs60\nSalad:Rs70\ncoffe:80")

order_total=0
item_1=input('Enter the name of item you want to order=')
if item_1 in menu:
    order_total+= menu[item_1]
    print(f"your item{item_1}has been added to your order")
else:
    print(f"ordered item{item-1} is not avaialable yet!")


another_order=input("Do you want to add another item?(Yes/No)")
if another_order=="Yes":
    item_2=input("Enter the name of second item=")
    if item_2 in menu:
        order_total+= menu[item_2]
        print(f"Item{item_2}has been added to order")
    else:
        print(f"Ordered item{item_2}is not available!")

print(f"The total amount of items to pay is {order_total}")



