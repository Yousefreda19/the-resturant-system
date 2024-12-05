from class_customerinfo import customer_info
from MainMeals import MainMeals
from sweets import sweets
from Appetizers import Appetizers
from Drink import Drinks
from order import order
from Bill import Bill

class Board:
    def __init__(self):
        self.order = order()
        self.new_order = customer_info()
        self.meals = MainMeals()
        self.sweet = sweets()
        self.drinks = Drinks()
        self.appetizer = Appetizers()
        self.bill = Bill()
        self.orders_list = []
        self.total=0

    def start_program(self):
        while True:  # Loop to handle multiple orders
            print("Main Meal ::")
            self.meals.display()
            print("Sweet ::")
            self.sweet.display()
            print("Drink ::")
            self.drinks.display()
            print("Appetizer ::")
            self.appetizer.display()

            # Ask user to make a selection
            self.des = int(input("1-New order / 0-Exit "))
            if self.des == 1:
                self.start_new_order()
            elif self.des == 0:
                break  # Exit loop when user chooses 0

        # Print all orders and the bill after exit
        self.print_all_orders_and_bill()

    def start_new_order(self):
        # Add new orders
        self.order.orders()
        self.order.Confirm_the_order()
        self.l = self.order.get_order_info()
        
        # Append the order to the orders list
        self.orders_list.append(self.l)
        
        # Print details of the new order
        print(f"New Order: {self.l[0][1]}  {self.l[0][0]}  {self.l[0][2]}")
        
      

   

    def print_all_orders_and_bill(self):
        # Print all the final orders
        self.bill.info()
        print("\nFinal Orders:")
        print("amount   name  price")
        x=0
        for order in self.orders_list:
            print(f"{order[x][1]}       {order[x][0]}        {order[x][2]}")
            self.total+=order[x][1]*order[x][2]
            x+=1
        print("-----------------------")
        print("the total price ::     ",self.total ,"EGP")
        print("discount        ::",self.order.discount,"%")
        print("Must be paid    ::",self.total-(self.total*self.order.discount/100))
        print("------------------------------------------------")
       
        
        print("\n    The bill has been printed successfully!   ")


x = Board()
x.start_program()
