import CakeCrud as c1

while True:
    print("\n========================================")
    print("          SWEET CAKE SHOP")
    print("========================================")
    print("1. Add Cake")
    print("2. Display Cakes")
    print("3. Update Cake")
    print("4. Search Cake")
    print("5. Delete Cake")
    print("6. Sort Cakes")
    print("7. Exit")
    print("========================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        c1.addCake()
    elif choice == "2":
        c1.displayCakes()
    elif choice == "3":
        c1.updateCake()
    elif choice == "4":
        c1.searchCake()
    elif choice == "5":
        c1.deleteCake()
    elif choice == "6":
        c1.sortCakes()
    elif choice == "7":
        print("Thank you for visiting Sweet Cake Shop.")
        break
    else:
        print("Please enter a valid choice.")
