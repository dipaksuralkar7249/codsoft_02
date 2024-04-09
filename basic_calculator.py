print("**** Basic Calculator ****")
while True:
    nam1 = int(input("Enter the Number :-"))
    nam2 = int(input("Enter the Number :-"))
    print("1.Addition"'\n'"2.Substraction"'\n'"3.Division"'\n'"4.Multiplication")
    choice = int(input("Enter the Choice :- "))
    if choice == 1:
        print(nam1 + nam2)
    elif choice == 2:
        print(nam1 - nam2)
    elif choice == 3:
        print(nam1 / nam2)
    elif choice == 4:
        print(nam1 * nam2)
    ch = input("Do you want to continue (yes/no)")
    if ch == "no":
        break

