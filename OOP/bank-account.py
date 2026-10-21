class Account:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def add_money(self, amount):
        if amount > 0:
            self.money = self.money + amount
            print("Money added successfully")
        else:
            print("Enter a valid amount")

    def show_details(self):
        print("Name:", self.name)
        print("Balance:", self.money)

obj = Account("Amit", 2000)
obj.add_money(300)
obj.show_details()
