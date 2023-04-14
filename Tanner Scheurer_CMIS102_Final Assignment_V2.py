def Credit():
  name = "Tanner Scheurer"
  course = "CMIS102"
  submission = "11 April 2023"
  out = "\n Submitted by: {} \n Course: {} \n Submitted on: {} \n ".format(name,course,submission)
  print(out)

#Create a cool logo for the main menu
logo = ''' 
 _______   _______    _____   _____
|__   __| |__   __|  / ___|  / ____|
   | |       | |    | |     |  (__
   | |       | |    | |      \__  \ 
   | |       | |    | |__    ___) |
   |_|       |_|    \____|  |____/

'''

def Welcome(*kwargs):
    print("\nWelcome to Tidy Tanner's Cleaning Service!")
    print("***Please select the services you desire***\n")
    print(logo)

#NOTE MN Sales tax = 6.875%; 

#Create a list for the menu
nav = {"m_nav": ["MAIN MENU","HOUSE CLEANING","YARD SERVICES","CHECK OUT",],
"h_nav": ["House Menu"],
"y_nav": ["Yard Menu"]
          }

def m_nav(nav, price, current):
    display = f"\n"
    for i, page in enumerate(nav["m_nav"]):
        if i == current:
            display += f"|** {i+1}: {page} **"
        else:
            display += f"| {i+1}: {page} "
    display += f"| 5. CART: ${price} |"
    print(display)

def h_nav(nav, price, current):
    display = f"\n"
    for i, page in enumerate(nav["h_nav"]):
        if i == current:
            display += f"|** {i+1}: {page} **"
        else:
            display += f"| {i+1}: {page} "
    display += f"| 2. CART: ${price} |"
    print(display)

def y_nav(nav, price, current):
    display = f"\n"
    for i, page in enumerate(nav["y_nav"]):
        if i == current:
            display += f"|** {i+1}: {page} **"
        else:
            display += f"| {i+1}: {page} "
    display += f"| 2. CART: ${price} |"
    print(display)

nav_options = [m_nav,h_nav,y_nav]
price = 0
current = 0
#Create a shopping cart, which will be a dictionary with all with 2 inner lists
cart = {
    "home": [],
    "yard": []
    }

prices_yard = {
    "mow_small_lawn":30,
    "mow_medium_lawn":50,
    "mow_large_lawn":80,
    "mow_very_large_lawn":150,#+$5/200 square feet

    "edge_small_lawn":20,
    "edge_medium_lawn":30,
    "edge_large_lawn":50,
    "edge_very_large_lawn":80,#+$5/200 square feet

    "shrubs":15
}

#create various functions that I will need to call from within the menu
def home_page(*kwargs):
    Welcome()

#create a house cleaning check out function with a basic menu
def house_cleaning(*args):
    nav, nav_options, cart, current, price = args
    nav_options[1](nav, price, current=0)

    prices_home = { "Standard Cleaning": 30,
                    "Deep Cleaning" : 75,
                    "Upholstery" : 50,
                    "Window Cleaning" : 10,
                    "Move Out": 300,
                    "Laundry": 20,
                    "Pet Hair": 30,
                    }

    print("\nPlease select the house cleaning services you need:")

    for i, service in enumerate(prices_home):
        print(f"{i+1}: {service} - ${prices_home[service]}")
    print("\n0: Go back to main menu")

    choice = input("\nEnter your choice: ")

    if choice.isdigit() and int(choice) in range(len(prices_home) + 1):
        choice = int(choice)
        if choice == 0:
            main(nav, nav_options, cart, current=0, price=price)
        else:
            selected_service = list(prices_home.keys())[choice - 1]

            if selected_service == "Standard Cleaning":
                num_rooms = int(input("Enter the number of rooms: "))
                cart["home"].append({selected_service: prices_home[selected_service] * num_rooms})
            elif selected_service == "Deep Cleaning":
                num_rooms = int(input("Enter the number of rooms for deep cleaning: "))
                cart["home"].append({selected_service: prices_home[selected_service] * num_rooms})
            elif selected_service == "Upholstery":
                num_rooms = int(input("Enter the number of rooms for upholstery cleaning: "))
                cart["home"].append({selected_service: prices_home[selected_service] * num_rooms})
            elif selected_service == "Move Out":
                cart["home"].append({selected_service: prices_home[selected_service]})
            elif selected_service == "Laundry":
                num_loads = int(input("Enter the number of laundry loads: "))
                cart["home"].append({selected_service: prices_home[selected_service] * num_loads})
            elif selected_service == "Pet Hair":
                num_rooms = int(input("Enter the number of rooms for pet hair cleaning: "))
                cart["home"].append({selected_service: prices_home[selected_service] * num_rooms})

            print(f"\n{selected_service} added to the cart!")

            # Recalculate the cart total and update the price variable
            updated_price = calc_bill(cart)
            house_cleaning(nav, nav_options, cart, current, updated_price)
    else:
        print("\nInvalid selection, please try again.")
        house_cleaning(nav, nav_options, cart, current, price)
#create a yard cleaning check out function with a basic menu
def yard_services(*args):
    nav, nav_options, cart, current, price = args
    nav_options[2](nav, price, current=0)

    prices_yard = {"Mowing": None,
                   "Edging": None,
                   "Shrubs": 15}

    yard_size = None
    yard_size_prices = {"Small": {"Mowing": 25, "Edging": 20},
                        "Medium": {"Mowing": 50, "Edging": 40},
                        "Large": {"Mowing": 100, "Edging": 80},
                        "Very Large": {"Mowing": 150, "Edging": 100}}
#classify the yard size
    def classify_yard_size(square_feet):
        if square_feet <= 1000:
            return "Small"
        elif 1000 < square_feet <= 5000:
            return "Medium"
        elif 5000 < square_feet <= 10000:
            return "Large"
        else:
            return "Very Large"

    print("\nPlease select the yard care services you need:")

    for i, service in enumerate(prices_yard):
        print(f"{i + 1}: {service}")
    print("\n0: Go back to main menu")

    choice = input("\nEnter your choice: ")

    if choice.isdigit() and int(choice) in range(len(prices_yard) + 1):
        choice = int(choice)
        if choice == 0:
            main(nav, nav_options, cart, current=0, price=calc_bill(cart))
        else:
            selected_service = list(prices_yard.keys())[choice - 1]

            if selected_service in ["Mowing", "Edging"] and yard_size is None:
                square_feet = int(input("Enter your yard's square footage: "))
                yard_size = classify_yard_size(square_feet)

            if selected_service == "Shrubs":
                num_shrubs = int(input("Enter the number of shrubs: "))
                cart["yard"].append({selected_service: prices_yard[selected_service] * num_shrubs})
            else:
                cart["yard"].append({selected_service: yard_size_prices[yard_size][selected_service]})

            print(f"\n{selected_service} added to the cart!")
            updated_price = calc_bill(cart)
            yard_services(nav, nav_options, cart, current, updated_price)
    else:
        print("\nInvalid selection, please try again.")
        yard_services(nav, nav_options, cart, current, price)
#create a check out function
def check_out(*args):
    nav, nav_options, cart, current, price = args
    tax_rate = 0.06875
    tax = price * tax_rate
    total = price + tax

    # Check for discounts
    print("\nAre you a  Senior Citizen/Active Duty Military/Veteran/First Responder or educator? (proof will be required on payment)")
    print("1: Yes")
    print("2: No")
    discount_choice = input("Enter your choice: ")

    discount_rate = 0
    if discount_choice == "1":
        discount_rate = 0.1  # Apply a 10% discount
        total = total * (1 - discount_rate)

    print(f"\nTotal before tax: ${price:.2f}")
    print(f"Tax (6.875%): ${tax:.2f}")
    print(f"Total: ${total:.2f}")

    # Confirmation of purchase
    print("\nPlease confirm your purchase:")
    print("1: Confirm")
    print("2: Cancel")
    confirmation_choice = input("Enter your choice: ")

    if confirmation_choice == "1":
        # Receipt
        print("\nReceipt:")
        print("Services:")
        print("Home Services:")
        for service in cart["home"]:
            print(f"{list(service.keys())[0]} - ${list(service.values())[0]}")
        print("\nYard Services:")
        for service in cart["yard"]:
            print(f"{list(service.keys())[0]} - ${list(service.values())[0]}")

        if discount_rate > 0:
            print(f"\nDiscount (10%): ${price * discount_rate:.2f}")

        print(f"\nTotal before tax: ${price:.2f}")
        print(f"Tax (6.875%): ${tax:.2f}")
        print(f"Total: ${total:.2f}")
        print("\nThank you for using Tidy Tanner's Cleaning Service!")
    else:
        print("\nPurchase canceled.")
        main(nav, nav_options, cart, current=0, price=calc_bill(cart))
#exit the program, call the credits function on the way out
    exit(Credit())
#get a detailed list of whats in the cart
def view_cart(*args):
    nav, nav_options, cart, current, price = args
#display function of the cart, I can't get this working properly (should be more detailed) and its 1 hour before submission time :(
    def display_services(service_list):
        services_dict = {}
        for service in service_list:
            key = list(service.keys())[0]
            value = list(service.values())[0]
            if key in services_dict:
                services_dict[key]["count"] += 1
                services_dict[key]["total"] += value
            else:
                services_dict[key] = {"count": 1, "total": value, "price": value}

        for idx, (key, details) in enumerate(services_dict.items(), 1):
            if details["count"] > 1:
                print(f"{idx}: {key} (${details['price']}) x{details['count']}: ${details['total']}")
            else:
                print(f"{idx}: {key}: ${details['total']}")

    print("\nYour Cart:")
    print("\n--Home Services--")
    display_services(cart["home"])

    print("\n--Yard Services--")
    display_services(cart["yard"])

    print(f"\nSubtotal: ${price:.2f}")

    print("\nEnter the number of the item you want to remove, 0 to go back to the main menu, or 'C' to check out.")
    choice = input("Enter your choice: ")
#determine what to do based on input (delete item, main menu or check out)
    if choice.isdigit():
        choice = int(choice)
        if choice in range(1, len(cart["home"]) + len(cart["yard"]) + 1):
            if choice <= len(cart["home"]):
                removed_item = cart["home"].pop(choice - 1)
            else:
                removed_item = cart["yard"].pop(choice - 1 - len(cart["home"]))

            print(f"\nRemoved {list(removed_item.keys())[0]} from the cart.")
            updated_price = calc_bill(cart)
            view_cart(nav, nav_options, cart, current, updated_price)
        elif choice == 0:
            main(nav, nav_options, cart, current=0, price=calc_bill(cart))
        else:
            print("\nInvalid selection, please try again.")
            view_cart(nav, nav_options, cart, current, price)
    elif choice.upper() == 'C':
        check_out(nav, nav_options, cart, current, price)
    else:
        print("\nInvalid selection, please try again.")
        view_cart(nav, nav_options, cart, current, price)



#function to calculate the bill ezpz
def calc_bill(cart):
    total = 0
    for service in cart["home"]:
        total += list(service.values())[0]
    for service in cart["yard"]:
        total += list(service.values())[0]
    return total


menu_options = {
    "1": home_page,
    "2": house_cleaning,
    "3": yard_services,
    "4": check_out,
    "5": view_cart
}

#define main and call arguments
def main(nav, nav_options, cart, current, price):
    # Call the homepage initially
    price = price 

    # Move the Welcome() call outside the while loop
  
    while True:
        nav_options[0](nav, price, current)
        Welcome()
        
        while True:
            
            

            choice = input("\nPlease select an option: ")
            if choice.isdigit() and int(choice) in range(1, len(menu_options) + 1):
                if int(choice) == current + 1:
                    print("You are already on the home page!\n")
                else:
                    current = int(choice) - 1
                    menu_options[str(current + 1)](nav, nav_options, cart, current, price)
            else:
                print("Invalid selection, please try again.")

#I still don't understand why we do this, but every tutorial I watch has it so I'm making it a habit
if __name__ == "__main__":
    main(nav, nav_options, cart, current, price,)
    
#****************to do***************
#go to cart from yard/home services menu
#fix cart display
#create wrapper for fancy receipt
#If time, "print" the receipt by writing a word file (unlikely to have time)
#triple check consistancy in nameing variables and all variables and functions names make sense