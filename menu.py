import os
import time
os.system('cls')
print()
print()
print(10*"-","WELCOME TO FANCYUNICORN.DK",10*"-")
print()
print()
print("Press Enter key to continue")
key = input()
if key == True:
    os.system('cls')
def print_menu():
    print (15*"-", "MENU", 15*"-")
    print("1. Trial balance")
    print("2. Balancing the accounts")
    print("3. Profit for each month")
    print("4. Graff")
    print("5. Exit")
    print(37* "-")

loop = True

while loop == True:
    print_menu()
    choice = str(input("Enter your choice [1-5]: "))
    if choice == "1":
        os.system('cls')
        print("Trial balance has been selected")
    elif choice == "2":
        os.system('cls')
        print("Balancing the accounts has been selected")
    elif choice == "3":
        os.system('cls')
        print("Profit for each month  has been selected")
    elif choice == "4":
        os.system('cls')
        print("Graff has been selected")
    elif choice == "5":
        os.system('cls')
        print("Menu  has been selected")
        loop = False
        os.system('cls')

print("THE END")
