# ----------------- G17 - GROCERY MANAGEMENT SYSTEM--------------------

# Define the user_data and inventory data txt file.
user_data = 'userdata.txt'
inventory_file = 'inventory.txt'

# Write the initial data into the inventory.txt file.
with open('inventory.txt','a')as file:
    pass

with open('userdata.txt','a')as file:
    pass

# Define the initial admin username and password.
ADMIN_USERNAME = 'ali'
ADMIN_PASSWORD = 'ali123'



# Function of add new user in userdata.txt .
def add_new_user():
    if current_user != 'admin':
        print("You do not have permission to add new users.")
        return

    username = input("Enter new username: ")
    while not username:
        print("Invalid input. Please enter a username.")
        username = input("Enter new username: ")

    with open("userdata.txt", "r") as f:
        existing_usernames = [line.split("\t")[0] for line in f]
        while username in existing_usernames:
            print("Username already exists. Please enter a different username.")
            username = input("Enter new username: ")

    while True:
        password = input("Enter new password: ")
        confirm_password = input("Confirm new password: ")
        if password == confirm_password:
            break
        else:
            print("Both passwords do not match. Please try again.")

    user_type = input("Enter user type (admin, inventory-checker, purchaser): ")
    while user_type not in ['admin', 'inventory-checker', 'purchaser']:
        print("Invalid user type. Please enter one of the following: admin, inventory-checker, purchaser.")
        user_type = input("Enter user type (admin, inventory-checker, purchaser): ")

    print(f"Username: {username}\nPassword: {password}\nUser type: {user_type}")

    with open("userdata.txt", "a") as f:
        f.write(f"{username}\t{password}\t{user_type}\n")
    print("New user added successfully.")


# Function of delete the whole user data from userdata.txt.
def delete_user():
    username = input('Enter the username to be deleted: ')
    with open('userdata.txt', 'r') as file:
        lines = file.readlines()
    new_lines = [line for line in lines if line.strip().split()[0] != username]
    if len(new_lines) == len(lines):
        print(f"User '{username}' not found.")
    else:
        with open('userdata.txt', 'w') as file:
            file.writelines(new_lines)
        print(f'User {username} has been deleted.')





# Function of add new item into the txt file. [Siew Sheng Yao(TP068174)]
def insert_new_item():
    items = []

    # Read existing items from inventory.txt
    with open("inventory.txt", "r") as f:
        for line in f:
            item_data = line.strip().split("\t")
            item_data[0] = int(item_data[0])  # Convert item code to integer
            items.append(item_data)

    while True:
        num_items = input('How many items would you like to insert? ')
        if num_items.isdigit():
            num_items = int(num_items)
            break
        else:
            print('Please enter a valid integer.')

    for i in range(num_items):
        while True:
            code = input("Enter item code: ")
            if code.isdigit():
                code = int(code)
                code_exists = any(int(item[0]) == code for item in items)
                if code_exists:
                    print("Item code already exists. Please enter a new code.")
                else:
                    break
            else:
                print("Please enter a valid integer.")

        description = input("Enter item description: ")
        category = input("Enter item category: ")
        unit = input("Enter item unit: ")
        while True:
            price = input("Enter item price: ")
            try:
                price = float(price)
                break
            except ValueError:
                print("Please enter a valid number.")

        while True:
            quantity = input("Enter item quantity: ")
            if quantity.isdigit():
                quantity = int(quantity)
                break
            else:
                print("Please enter a valid number.")

        while True:
            minimum = input("Enter item minimum threshold: ")
            if minimum.isdigit():
                minimum = int(minimum)
                break
            else:
                print("Please enter a valid number.")

        new_item = [code, description, category, unit, price, quantity, minimum]
        items.append(new_item)

    with open("inventory.txt", "w") as f:
        for item in items:
            f.write("\t".join(str(i) for i in item) + "\n")
    print(f'{num_items} item(s) added to inventory.')





# Function of changing the specific details of an item. [Sin Boon Leon(TP068552)]
def update_item():
    code = input("Enter item code to update: ")
    found = False
    for item in items:
        if item[0] == code:
            found = True
            break

    if found:
        print("Enter new details for the item (press Enter to keep current value)")
        description = input("Description: ")
        category = input("Category: ")
        unit = input("Unit: ")
        price = input("Price: ")
        quantity = input("Quantity: ")
        minimum = input("Minimum threshold: ")

        change_code = input("Do you want to change the item code? (Y/N): ")
        if change_code.lower() == "y":
            new_code = input("Enter the new item code: ")
            code = new_code.strip()

        # Update the item details
        if description:
            item[1] = description
        if category:
            item[2] = category
        if unit:
            item[3] = unit
        if price:
            item[4] = float(price)
        if quantity:
            item[5] = int(quantity)
        if minimum:
            item[6] = int(minimum)
        if code:
            item[0] = code

        with open("inventory.txt", "w") as f:
            for item in items:
                f.write("\t".join(str(i) for i in item) + "\n")
        print("Item updated successfully.")
    else:
        print("Item not found.")


# Function of removing the item data. [Sin Boon Leon(TP068552)]
def delete_item():
    code = input("Enter item code to delete: ")

    found = False
    for item in items:
        if item[0] == code:
            found = True
            break

    if found:
        items.remove(item)
        with open("inventory.txt", "w") as f:
            for item in items:
                f.write("\t".join(str(i) for i in item) + "\n")
        print("Item deleted successfully.")
    else:
        print("Item not found.")



# Function of tracking the item quantity available. [Siew Sheng Yao(TP068174)]
def stock_taking():
    code = int(input("Enter item code to stock-take: "))

    found = False
    for item in items:
        if int(item[0]) == code:
            found = True
            break

    if found:
        current_quantity = int(item[5])
        print(f"Current quantity: {current_quantity}")
        new_quantity = input("Enter new quantity (press Enter to keep current value): ")
        if new_quantity:
            new_quantity = int(new_quantity)
            if current_quantity >= new_quantity:
                stock_taken = current_quantity - new_quantity
                current_remaining_quantity = new_quantity
                print(f"This stock has taken :{stock_taken}")
                print(f"This stock now have  :{current_remaining_quantity}")
                print(f"This '{code}' inventory has been updated successfully !")
            else:
                current_remaining_quantity = current_quantity
                print(f"You can't put the quantity greater than the current, if you want add quantity please choose stock replenishment.")
                print(f"This stock now have  :{current_remaining_quantity}")
            item[5] = int(current_remaining_quantity)

        else:
            print("Stock-taking cancelled. Quantity remains unchanged.")
            current_remaining_quantity = item[5]
            print(f"This stock now have :{current_remaining_quantity}")

        with open("inventory.txt", "w") as f:
            for item in items:
                f.write("\t".join(str(i) for i in item) + "\n")
    else:
        print("Item not found.")





# Function of viewing the current item from the text file. [Chong Kah Jun(TP067165)]
def view_replenish_list():
    # Update the items list
    with open("inventory.txt", "r") as f:
        items.clear()
        for line in f:
            item = line.strip().split("\t")
            items.append(item)

    print("Items to replenish:")
    replenish_items_found = False
    for item in items:
        if int(item[5]) < int(item[6]):
            replenish_items_found = True
            print(f"{item[1]} - Quantity to replenish: {int(item[6]) - int(item[5])}")
    if not replenish_items_found:
        print("There is no stock to replenish, all items are sufficient.")



#Function of list out the that quantity lower than the minimum threshold. [Chong Kah Jun(TP067165)]
def stock_replenishment():
    code = input("Enter item code to replenish: ")

    found = False
    for item in items:
        if item[0] == code:
            found = True
            break

    if found:
        current_quantity = item[5]
        print(f"Current quantity of item code \"{code}\" : {current_quantity}")
        replenishment_quantity = input("Enter replenishment quantity: ")
        if replenishment_quantity:
            new_quantity = int(current_quantity) + int(replenishment_quantity)
            item[5] = new_quantity
            remaining_quantity = item[5]
            print(f"{replenishment_quantity} stocks of item code \"{code}\" has been added. {remaining_quantity} stocks now available. "
                  f"Quantity updated to {new_quantity}")
        else:
            print("Replenishment cancelled. Quantity remains unchanged.")
            remaining_quantity = item[5]
            print(f"{remaining_quantity} stocks available.")

        with open("inventory.txt", "w") as f:
            for i in items:
                f.write("\t".join(str(i) for i in i) + "\n")
        print(f"The inventory has been updated: {code} - {item[1]} ({item[2]}) now has {remaining_quantity} stocks.")
    else:
        print("Item not found.")



# Function of search_item menu. [Yong Lee Wai(TP068636)]
def search_items():
    print("1. Description")
    print("2. Code range")
    print("3. Category")
    print("4. Price range")
    print("5. Exit")

    while True:
        option = input("Enter your option >> ")
        if option == "1":
            des()
        elif option == "2":
            code_range()
        elif option == "3":
            category()
        elif option == "4":
            price_range()
        elif option == "5":
            break
        else :
            print('Please enter a valid integer.')


# Function of search description. [Yong Lee Wai(TP068636)]
def des():
    f = open("Inventory.txt", "r")
    x = f.readlines()
    description = input("Enter the description >> ")
    all_item = []
    for i in x:
        temp = i.split("\t")
        if (description.lower() in temp[1].lower()):
            all_item.append(temp)
    print("found ", len(all_item), "items")
    for item in all_item:
        print(f"Code: {item[0]}, Description: {item[1]}, Category: {item[2]}, Unit: {item[3]}, "
              f"Price: RM{float(item[4]):.2f}, Quantity: {item[5]}, Minimum threshold: {item[6]}")

# Function of search Code range. [Yong Lee Wai(TP068636)]
def code_range():
    f = open("Inventory.txt", "r")
    x = f.readlines()
    start = int(input("Begin from >>= "))
    end = int(input("End with >>= "))
    all_item = []
    for i in x:
        temp = i.split("\t")
        code = int(temp[0])
        if (code >= start and code <= end):
            all_item.append(temp)
    print("found ", len(all_item), "items")
    for item in all_item:
        print(f"Code: {item[0]}, Description: {item[1]}, Category: {item[2]}, Unit: {item[3]}, "
              f"Price: RM{float(item[4]):.2f}, Quantity: {item[5]}, Minimum threshold: {item[6]}")


# Function of search category. [Yong Lee Wai(TP068636)]
def category():
    f = open("inventory.txt", "r")
    x = f.readlines()
    target = input("Category >> ")
    all_item = []
    for i in x:
        temp = i.split("\t")
        cate = temp[2]
        if (cate.lower() == target.lower()):
            all_item.append(temp)
    print("found ", len(all_item), "items")
    for item in all_item:
        print(f"Code: {item[0]}, Description: {item[1]}, Category: {item[2]}, Unit: {item[3]}, "
            f"Price: RM{float(item[4]):.2f}, Quantity: {item[5]}, Minimum threshold: {item[6]}")

# Function of search price range. [Yong Lee Wai(TP068636)]
def price_range():
    f = open("inventory.txt", "r")
    x = f.readlines()
    start = float(input("Price min >>= "))
    end = float(input("Price max >>= "))
    all_item = []
    for i in x:
        temp = i.split("\t")
        code = float(temp[4])
        if (code >= start and code <= end):
            all_item.append(temp)
    print("found ", len(all_item), "items")
    for item in all_item:
        print(f"Code: {item[0]}, Description: {item[1]}, Category: {item[2]}, Unit: {item[3]}, "
            f"Price: RM{float(item[4]):.2f}, Quantity: {item[5]}, Minimum threshold: {item[6]}")


# Function to prints out the current inventory. [Sin Boon Leon(TP068552)] & [Yong Lee Wai(TP068636)]
def view_inventory():
    print("Current inventory:")
    with open(inventory_file) as f:
        items = [(line.strip().split('\t')) for line in f]

    for item in items:
        print(f"Code: {item[0]}, Description: {item[1]}, Category: {item[2]}, Unit: {item[3]}, "
              f"Price: RM{float(item[4]):.2f}, Quantity: {item[5]}, Minimum threshold: {item[6]}")


# Function to authentical the user.  [Siew Sheng Yao(TP068174)] & [Chong Kah Jun(TP067165)]
def user_authentication():
    username = ''
    password = ''

    while not (username and password):
        username = input("Enter username: ")
        password = input("Enter password: ")
        if not (username and password):
            print("Please enter both username and password.")

    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        print(f"Welcome, {username}!")
        return 'admin'

    with open("userdata.txt", "r") as f:
        for line in f:
            line = line.strip().split("\t")
            if username == line[0] and password == line[1]:
                print(f"Welcome, {username}!")
                return line[2]

    print("Incorrect password or username.")



# main program
items = []

with open("inventory.txt", "r") as f:
    for line in f:
        item = line.strip().split("\t")
        items.append(item)

current_user = None
while True:
    if current_user is None:
        print("------G17 - GROCERY STORE INVENTORY SYSTEM-------")
        print("Please log in your credentials.")
        user_type = user_authentication()
        if user_type is not None:
            current_user = user_type
    else:
        if current_user == 'admin':
            print("Menu:")
            print("1. add_new_user")
            print("2. delete_user")
            print("3. Insert new item")
            print("4. Update existing item")
            print("5. Delete item")
            print("6. stock_taking")
            print("7. view_replenish_list")
            print("8. stock_replenishment")
            print("9. search_items")
            print("10. view_inventory")
            print("11. logout")
            print("12. exit")

        elif current_user == 'inventory-checker':
            print("1. stock_taking")
            print("2. search_items")
            print("3. view_inventory")
            print("4. logout")
            print("5. exit")

        elif current_user=='purchaser':
            print("1. view_replenish_list")
            print("2. stock_replenishment")
            print("3. search_items")
            print("4. view_inventory")
            print("5. logout")
            print("6. exit")


        choice = input("Enter choice: ")

        if current_user == 'admin':
            if choice == '1':
                add_new_user()
            elif choice == '2':
                delete_user()
            elif choice == "3":
                insert_new_item()
            elif choice == "4":
                update_item()
            elif choice == "5":
                delete_item()
            elif choice == "6":
                stock_taking()
            elif choice == "7":
                view_replenish_list()
            elif choice == "8":
                stock_replenishment()
            elif choice == "9":
                search_items()
            elif choice == "10":
                view_inventory()
            elif choice == '11':
                current_user = None
                print("Logged out successfully.")
            elif choice == '12':
                break
            else:
                print("Invalid choice. Please try again.")

        if current_user == 'inventory-checker':
            if choice == "1":
                stock_taking()
            elif choice== "2":
                search_items()
            elif choice=="3":
                view_inventory()
            elif choice== "4":
                current_user = None
                print("Logged out successfully.")
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")

        if current_user == 'purchaser':
            if choice == "1":
                view_replenish_list()
            elif choice== "2":
                stock_replenishment()
            elif choice== "3":
                search_items()
            elif choice=="4":
                view_inventory()
            elif choice == "5":
                current_user = None
                print("Logged out successfully.")
            elif choice == "6":
                break
            else:
                print("Invalid choice. Please try again.")

