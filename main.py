from functions import COFFEES,QUARTERS,PENNIES,NICKLES,DIMES,coin_list,calculate,get_coin,resources,change_resources,prepare_coffee,enough_resources,refill
from art import logo
import os
import time

cls=lambda: os.system('cls')
machine="on"
resources_left=resources
make_time=5
balance=0
while not machine==str.lower("off"):
    print(logo)
    print(f"\nResources:\nCoffee:{resources_left["Coffee"]}gr\nWater:{resources_left["Water"]}ml\nMilk:{resources_left["Milk"]}ml\n")
    coffee_choice=int(input("Choose your coffee\n1.Espresso:$1.5\n2.Latte:$2.5\n3.Cappuccino:$3\n"))
    if balance<1.5:
            print("Insert coins:")
            balance+=calculate(get_coin())
    print(f'Balance:${balance}')
    
    
    
    
    
    if coffee_choice==1:
        coffee_choice="Espresso"
        if enough_resources(coffee_choice,resources_left):
            print(f"Price:${COFFEES[coffee_choice]["Price"]}")
            if balance>=COFFEES[coffee_choice]["Price"]:
                resources_left=change_resources(resources_left,coffee_choice)
                balance-=COFFEES[coffee_choice]["Price"]
                
                for i in range(1,6):
                    print(i)
                    time.sleep(1)
                    
                print(f"Your {coffee_choice} is ready!") 
            else:
                print("\nNot enough balance! Insert more coins")
                print("\n1.Espresso:$1.5\n2.Latte:$2.5\n3.Cappuccino:$3")
                
                print("Insert coins:")
                balance+=calculate(get_coin())
               
    
    
    
    
    if coffee_choice==2:
        coffee_choice="Latte"
        if enough_resources(coffee_choice,resources_left):
            print(f"Price:${COFFEES[coffee_choice]["Price"]}")


            if balance>=COFFEES[coffee_choice]["Price"]:
                resources_left=change_resources(resources_left,coffee_choice)
                balance-=COFFEES[coffee_choice]["Price"]
                
                for i in range(1,6):
                    print(i)
                    time.sleep(1)
                print(f"Your {coffee_choice} is ready!") 
            else:
                print("\nNot enough balance! Insert more coins")
                print("\n1.Espresso:$1.5\n2.Latte:$2.5\n3.Cappuccino:$3")
                
                print("Insert coins:")
                balance+=calculate(get_coin())
   
    
    

    
    
    if coffee_choice==3:
        coffee_choice="Cappuccino"
        if enough_resources(coffee_choice,resources_left):
            print(f"Price:${COFFEES[coffee_choice]["Price"]}")
            if balance>=COFFEES[coffee_choice]["Price"]:
                resources_left=change_resources(resources_left,coffee_choice)
                balance-=COFFEES[coffee_choice]["Price"]
                
                for i in range(1,6):
                    print(i)
                    time.sleep(1)
                print(f"Your {coffee_choice} is ready!")    
            else:
                
                print("\nNot enough balance! Insert more coins")
                print("\nEspresso:$1.5\nLatte:$2.5\nCappuccino:$3\n")
                print(f"Balance:{balance}")
                print("Insert coins:")
                balance+=calculate(get_coin())
    
    
    
    
    
                        
    if not enough_resources(coffee_choice,resources_left):
        if refill():
            resources_left=resources
        else:
            print("\nCoffee machine is not working!")
            break
        
    
    
    
    print(f"\nResources:\nCoffee:{resources_left["Coffee"]}gr\nWater:{resources_left["Water"]}ml\nMilk:{resources_left["Milk"]}ml")
    print(f'Balance:${balance}\n')
    
    
    
    get_change=int(input("1.Get change\n2.Buy another coffee\n"))
    if get_change==1:
        cls()
        print(f"Here is your change:${balance}")
        balance=0
    machine=input("\n\ntype 'off' to turn off machine or 'press enter':")
    cls()
        
