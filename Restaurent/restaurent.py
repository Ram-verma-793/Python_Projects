class Menu:
    def welcome(self):
        print("Welcome to our Restaurant!😊😊")
        self.name = input("What's your name sir! : ")

    def __init__(self):
        self.total_cost = 0
        self.pizza = 200
        self.pasta = 120
        self.cold_drink = 90

    def price(self, amount):
        self.total_cost += amount
        print("Your order cost is: ", amount, "$")

   
    def order(self):

        print("Here's the menu..")
        print("1. PIZZA :",self.pizza,"$\n 2. PASTA : ",self.pasta,"$\n 3. COLD DRINKS : ",self.cold_drink,"$")
        order = int(input("What you want to order sir!.."))
        quantity = int(input(f"How many units you want, {self.name}? "))

        match order:
            case 1: 
                print("Here's your Pizza ", self.name,"!")
                self.price(self.pizza * quantity)
            case 2: 
                print("Here's your Pasta ",self.name, "!")
                self.price(self.pasta * quantity)
            case 3:
                print("Here's your Cold drink ",self.name, "!")
                self.price(self.cold_drink * quantity)
            case _: 
                print("Something wrong!")
    
    
        



    def payment(self):
        print("How you want to pay the bill ", self.name)
        payment_mod = int(input("1: Cash payment 2: Upi 3. Card "))
        print("Name: ", self.name)
        match payment_mod:
            case 1:
                print("Payment Mode: cash , Bill Amount:: ",self.total_cost)
            case 2:
                print("Payment Mode: Upi  , Bill Amount:: ", self.total_cost)
            case 3:
                print("Payment Mode: Card , Bill Amount:: ", self.total_cost)
            case _:
                print("Something went wrong!")


menu = Menu()    
menu.welcome()
while True:
        menu.order()
        confirmation = input("Anything else you want to order!: \n Y / N: ")
        if confirmation != 'y':
             break
      


menu.payment()
