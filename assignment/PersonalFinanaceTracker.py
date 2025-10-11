from datetime import datetime, date

users = {}

CATEGORIES = ["Income", "Food", "Rent", "Entertainment", "Others"]

def createUser():
    username = input("enter username: ").strip()
    if not username:
        print("username cannot be empty!") # True because "" means False
        return
    if username in users:
        print("this user already exixts! choose another")
        return 
    password = input("enter password: ").strip()
    if not password:
        password = None
    users[username] = {"password": password, "transactions": []}
    print(f"{username} created successfully!")

def login():
    username = input("enter username: ").strip()
    if username not in users:
        print()
        print(f"{username} does not exist!")
        return None
    userPswd = users[username]["password"]
    pswd = input("enter password: ").strip()

    if userPswd is not None and userPswd != pswd:
        print("incorrect password!")
        return None
    print(f"logged in {username}")
    return username

def parse_date(input_str):
    #Parse date in YYYY-MM-DD format.
    #isoformat() method is used to return a string representation of a date, time, or datetime
    #strptime() is a method primarily found within the datetime module and also in the time module.
    if not input_str:
        return date.today().isoformat()
    try:
        dt = datetime.strptime(input_str, "%Y-%m-%d").date()
    except TypeError:
        print("invalid format!")
        return date.today().isoformat()

def add_transaction(username):
    #.title() capitalizes the first letter
    while True:
        amount_str = input("enter amount: ").strip()
        try:
            amount = float(amount_str)
            break
        except ValueError:
            print("invalid format!")

    transaction_type = input("enter transaction type(income / expense): ").strip().title()
    if transaction_type not in ("Income", "Expense"):
        print("invalid type!")
        transaction_type = "Expense"

    date_input = input("enter date(YYY-MM-DD) or leave empty: ").strip()
    if not date_input:
        date_input = date.today().isoformat()
    transaction_date = parse_date(date_input)

    category_input = input(f"Enter interested category from {CATEGORIES}: ").strip().title()
    if category_input not in CATEGORIES:
        print("suggested category not in our data! you can use others")
        category_input = "others"
    
    Description = input("enter description for transcation: ").strip().title()

    transaction = {
        'date': date_input,
        'type' : transaction_type,
        'amount' : amount,
        'category' : category_input,
        'description' : Description
    }
    users[username]['transactions'].append(transaction)
    print("Your transaction addedd!")

def view_transaction(username):
    tsx_summary = users[username]['transactions']
    if not tsx_summary:
        print("no transaction record")
        return
    print()
    print("Date     | Type | Amount | Category | Description")
    print("-" * 75)

    total_income = 0
    total_expense = 0

    for tsx in tsx_summary:
        display_amount = int(tsx['amount']) if tsx['amount'].is_integer() else tsx['amount']
        print(f"{tsx['date']} | {tsx['type']:<7} | {display_amount:<9} | {tsx['category']:<13} | {tsx['description']}")

        if tsx['type'] == "Income":
            total_income += tsx['amount']
        else:
            total_expense += tsx['amount']
    net = total_income - total_expense
    print("-" * 75)

    def format(x):
        return str(int(x)) if float(x).is_integer() else f"{x:.2f}"
    
    print(f"total income: {format(total_income)}")
    print(f"total expense: {format(total_expense)}")
    print(f"net balance: {format(net)}")

def user_menu(username):
    while True:
        print()
        print("-" * 25  + "USER MENU" + "-" * 25)
        print('''1. Add Transaction 
2. View Your Transaction
3. Logout
            ''')
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_transaction(username)
        elif choice == "2":
            view_transaction(username)
        elif choice == "3":
            print("logging out......")
            break
        else:
            print("invalid choice!")

def main():
    print()
    print("*" * 20 + "Welcome to finanace tracker" + "*" * 20)
    print()
    while True:
        print(''' 
            1. Create User
            2. Login
            3. Exit
        ''')

        choice = input("Enter your choice: ")

        match(choice):
            case '1':
                createUser()
            case '2':
                user = login()
                if user:
                    user_menu(user)
            case '3':
                print("existing finance tracker")
                break
            case _:
                print("Enter valid choice!")

if __name__ == "__main__":
    main()

