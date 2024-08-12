COFFEES={
    "Espresso":{
        "Water":50,
        "Coffee":18,
        "Milk":0,
        "Price":1.5   
    },
    "Latte":{
        "Water":200,
        "Coffee":24,
        "Milk":150,
        "Price":2.5 
    },
    "Cappuccino":{
        "Water":250,
        "Coffee":24,
        "Milk":100,
        "Price":3.0 
    }
}

QUARTERS=0.25
DIMES=0.10
NICKLES=0.05
PENNIES=0.01

coin_list=[QUARTERS,DIMES,NICKLES,PENNIES]



def calculate(money):
    """Calculate the value off all inserted coins"""
    total=0
    i=0
    for coin in money:
        money[coin]*=coin_list[i]
        total+=money[coin]
        i+=1
        
    return float("{:.2f}".format(total))

def get_coin():
    """Get coins from user"""
    money={"quarters":0,"dimes":0,"nickles":0,"pennies":0}
    for i in money:
        money[i]=int(input(f"Insert {i}:"))
    return money

resources={
    "Water":1000,
    "Milk":1000,
    "Coffee":150
    
}


def change_resources(resources_left,coffee_choice):
        resources_left["Milk"]-=COFFEES[coffee_choice]["Milk"]
        resources_left["Water"]-=COFFEES[coffee_choice]["Water"]
        resources_left["Coffee"]-=COFFEES[coffee_choice]["Coffee"]
        return resources_left
    
def prepare_coffee(coffee_choice):
    import time
    make_time=0
    while make_time>0:
            print(make_time)
            time.sleep(1)
            make_time-=1
    return print(f"Your {coffee_choice} is ready!") 

def refill():
    refill=int(input("Do you wish to refill?\n1.Yes\n2.No\n"))
    if refill==1:
        return True
    elif refill==2:
        return False

def enough_resources(coffee_choice,resources_left):
    enough=True
    if COFFEES[coffee_choice]["Milk"]>resources_left["Milk"]:
        print("Not enough milk!")
        enough=False
    if COFFEES[coffee_choice]["Water"]>resources_left["Water"]:
        print("Not enough water!")
        enough=False
    if COFFEES[coffee_choice]["Coffee"]>resources_left["Coffee"]:
        print("Not enough coffee!")
        enough=False
    return enough

