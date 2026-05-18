# class BrandsNames:
#     def __init__(self, names, colors, speed):
#         self.names = names
#         self.colors = colors
#         self.speed = speed

#     def printDetailed(self)
#         print(f"My cars companys {}")

# class ShoppingEnganment:
#     def __init__(self):
#         self.balance = 20000
#         self.item= []
#         self.statnment =[]

# # Method for


class ShoppingEngagement:

    def __init__(self):
        self.balance = 20000
        self.items = []
        self.statement = []

    # METHOD FOR PURCHASING
    def purchase(self):

        try:
           =-P0OI
            print("You are about to make a Purchase of 5 items")

            numb = 0
            position = ["1st", "2nd", "3rd", "4th", "5th"]

            data = []

            while numb < 5:

                print()
                print(f"Enter the {position[numb]} item's")

                nameItem = input("Enter the Item's name: ")

                while True:

                    try:
                        costItem = float(input(f"Enter the cost of {nameItem}: "))
                        break

                    except:
                        print("Please input the right value")

                item = {
                    "name": nameItem,
                    "cost": costItem
                }

                data.append(item)

                numb = numb + 1

            totalCost = sum(i["cost"] for i in data)

            if self.balance >= totalCost:

                self.items.extend(data)

                self.balance -= totalCost

                self.statement.append(
                    f"Purchased items worth ₦{totalCost}"
                )

                print()
                print("Purchase Successful")

            else:
                print()
                print("Insufficient Balance")

        except ValueError as e:
            print("Error caught here!", e)

    # METHOD TO SEE PURCHASED ITEMS
    def viewItems(self):

        print()
        print("Purchased Items")

        for item in self.items:
            print(f"{item['name']} - ₦{item['cost']}")

    # METHOD TO CHECK BALANCE
    def checkBalance(self):

        print()
        print(f"Your Account Balance is ₦{self.balance}")

    # METHOD FOR ACCOUNT STATEMENT
    def accountStatement(self):

        print()
        print("Account Statement")

        for data in self.statement:
            print(data)

    # METHOD FOR SENDING MONEY
    def sendMoney(self):

        print()

        receiver = input("Enter Receiver Name: ")

        try:
            amount = float(input("Enter Amount to Send: "))

            if amount <= self.balance:

                self.balance -= amount

                self.statement.append(
                    f"Transferred ₦{amount} to {receiver}"
                )

                print()
                print(f"₦{amount} sent to {receiver} successfully")

            else:
                print()
                print("Insufficient Balance")

        except:
            print("Invalid Amount")


# OBJECT
shopping = ShoppingEngagement()

# FIRST PURCHASE
shopping.purchase()

# SECOND PURCHASE
shopping.purchase()

# SEND MONEY
shopping.sendMoney()

# VIEW ITEMS
shopping.viewItems()

# VIEW BALANCE
shopping.checkBalance()

# VIEW STATEMENT
shopping.accountStatement()