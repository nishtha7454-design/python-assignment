cakes = []

def addCake():
    cake_id = int(input("Enter Cake ID: "))
    name = input("Enter Cake Name: ")
    cake_type = input("Enter Cake Type: ")
    price = int(input("Enter Cake Price: "))
    size = input("Enter Cake Size: ")
    stock = int(input("Enter Available Stock: "))

    cake = {"ID": cake_id, "Name": name, "Type": cake_type,
            "Price": price, "Size": size, "Stock": stock}
    cakes.append(cake)
    print("Cake added successfully.")


def displayCakes():
    if len(cakes) == 0:
        print("No cakes available.")
        return

    print("\n---------------------------------------------------------------")
    print("ID\tCake Name\tType\t\tPrice\tSize\tStock")
    print("---------------------------------------------------------------")
    for cake in cakes:
        print(cake["ID"], "\t", cake["Name"], "\t\t",
              cake["Type"], "\t\t", cake["Price"],
              "\t", cake["Size"], "\t", cake["Stock"])


def searchCake():
    value = input("Enter Cake ID or Cake Name to search: ")
    found = False

    for cake in cakes:
        if str(cake["ID"]) == value or cake["Name"].lower() == value.lower():
            print("\nCake Found")
            print("-------------------------")
            print("Cake ID     :", cake["ID"])
            print("Cake Name   :", cake["Name"])
            print("Cake Type   :", cake["Type"])
            print("Price       :", cake["Price"])
            print("Size        :", cake["Size"])
            print("Stock       :", cake["Stock"])
            found = True

    if found == False:
        print("Cake not found.")


def updateCake():
    cake_id = int(input("Enter Cake ID to update: "))
    found = False

    for cake in cakes:
        if cake["ID"] == cake_id:
            found = True
            print("1. Change Cake Name")
            print("2. Change Cake Type")
            print("3. Change Price")
            print("4. Change Size")
            print("5. Change Stock")

            choice = input("Enter your choice: ")

            if choice == "1":
                cake["Name"] = input("Enter new cake name: ")
            elif choice == "2":
                cake["Type"] = input("Enter new cake type: ")
            elif choice == "3":
                cake["Price"] = int(input("Enter new price: "))
            elif choice == "4":
                cake["Size"] = input("Enter new size: ")
            elif choice == "5":
                cake["Stock"] = int(input("Enter new stock: "))
            else:
                print("Invalid choice.")
                return

            print("Cake details updated successfully.")
            break

    if found == False:
        print("Cake ID not found.")


def deleteCake():
    cake_id = int(input("Enter Cake ID to delete: "))
    found = False

    for cake in cakes:
        if cake["ID"] == cake_id:
            cakes.remove(cake)
            found = True
            print("Cake deleted successfully.")
            break

    if found == False:
        print("Cake ID not found.")


def sortCakes():
    if len(cakes) == 0:
        print("No cakes available for sorting.")
        return

    print("1. Sort by Cake Name")
    print("2. Sort by Price")
    print("3. Sort by Stock")
    choice = input("Enter your choice: ")

    if choice == "1":
        cakes.sort(key=lambda x: x["Name"].lower())
    elif choice == "2":
        cakes.sort(key=lambda x: x["Price"])
    elif choice == "3":
        cakes.sort(key=lambda x: x["Stock"])
    else:
        print("Invalid choice.")
        return

    print("Cake records sorted successfully.")
    displayCakes()
