import random
from time import sleep
from datetime import date

####################### afrika micro finance bank ####################################

# user data
customers_data = {}

# banking system
def africaMFB():
    print("Welcome to Afrika MF Bank")

    # check if our customer is new or an old customer
    check_user = int(input("Do you have account with us: 1: (yes) 2: (no) \n"))

    if (check_user == 1):
        login()
    
    elif (check_user == 2):
        register()



### Login system
def login():
    print()
    print("********* Login ***********")

    accountNumberFromUser = int(input("What is your account number? \n"))
    password = input("What is your password \n")

    ########## Check if the string "user" is in our customer_data. if not return user not found, For new people that want
    # to lofin without registration #########
    if "user" not in  customers_data:
        print("User not found")
        login()

    else:
        for i, userDetails in customers_data.items():
            if (userDetails[4] == accountNumberFromUser):
                if(userDetails[2] == password):
                    bankOperation(userDetails)
                else:
                    print("incorrect password. try again")
                    login()
            else:
                print("account not found")
                register()



#### Register sectiopn #####
def register():
    print()
    print("****** Register *******")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("create a password for yourself \n")
    house_address = input("Your house address \n")

    account_number = generate_account_number()
    bvn = generate_bvn()
    account_bal = 0
    today = date.today()
    year_created = today.strftime("%b-%d-%Y")



    customers_data["user"] = [first_name, last_name, password, house_address, account_number,account_bal, year_created, bvn,email]
    
    print("Your Account Has been created")
    print(" == ==== ====== ===== ===")
    print("Your account number is: %d" % account_number)
    print("Your BVN is: %d" % bvn)
    print(f"Your account balance is: ₦ { account_bal} ")
    print("Make sure you keep it safe")
    print(" == ==== ====== ===== ===")

    

    login()

def generate_account_number():
    return random.randrange(1111111111,9999999999)

def generate_bvn():
    return random.randrange(11111111111,99999999999)

def bankOperation(user):
    print()
    print("Welcome %s %s " % ( user[0], user[1] ) )
    selectedOption = int(input("What would you like to do? (1) deposit (2) withdrawal (3) Logout (4) Profile (5) Exit \n"))
    

    if (selectedOption == 1 ):
        deposit_form(user)
    elif (selectedOption == 2):
        withdrawal(user)
    elif(selectedOption == 3):
        login()
    elif (selectedOption == 4):
        profile(user)
    elif(selectedOption == 5):
        print("Thank for banking with us.")
        
        exit()
    else:
        print("Invalid command!!!")
        

        


def deposit_form(user_data):
    print()
    print("Deposit")
    print(" == ==== ====== ===== ===")
    user_deposit = int(input("How much will you like to deposit?: \n"))

    user_data[5] += user_deposit
    
    sleep(0.5)
    print("Deposit successful ")
    print(f"your current balance is: ₦{user_data[5]}")
    print(" == ==== ====== ===== ===")
    
    # ask the customer if he/she wish to continue
    do_wish = int(input("Do you wish to continue this transaction: 1: (yes) 2: (no) \n"))

    if do_wish == 1:
        login()
    elif do_wish == 2:
        print("Thank for banking with us.")
        exit()
    else:
        print("Invalid command")
        login()



def withdrawal(user_data):
    print()
    print("Withdrawal")
    print(" == ==== ====== ===== ===")
    user_withdraw = int(input("How much do you want to withdraw ?: \n"))
    if user_data[5] < user_withdraw:
        sleep(0.7)
        print(" == ==== ====== ===== ===")
        print("insufficient fund")
        
        ask_wish = int(input("Do you wish to continue this transaction: 1: (yes) 2: (no) \n"))
        if ask_wish == 1:
            login()
        elif ask_wish == 2:
            print("Thank for banking with us.")
            exit()
        else:
            print("Invalid command")
            login()
    else:
        user_data[5]
        
        sleep(0.7)
        
        print("Withdrawal successful")
        user_data[5] - user_withdraw
        print(f"your new account balance is: ₦{user_data[5] - user_withdraw}")
        user_data[5] - user_withdraw
        print(" == ==== ====== ===== ===")

        ask_wish = int(input("Do you wish to continue this transaction: 1: (yes) 2: (no) \n"))
        if ask_wish == 1:
            login()
        elif ask_wish == 2:
            print("Thank for banking with us.")
            exit()
        else:
            print("Invalid command")
            login()





def profile(user_data):
    print()
    print(" == ==== ====== ===== ===")

    user_bvn = int(input("what's your BVN: \n"))
    if user_data[7] == user_bvn:
        print()
        print("Profile")
        print(" == ==== ====== ===== ===")
        print(f"Your names are: {user_data[0]} {user_data[1] }")
        print(f"Address: {user_data[3]}")
        print(f"Email: {user_data[8]}")
        print(f"Account balance: ₦{user_data[5]}")
        print(f"Your bank verification number is: {user_data[7]}")
        print(f"Your account number is: {user_data[4]}")
        print(f"Registered on: {user_data[6]}")

        print(" == ==== ====== ===== ===")
        ask_wish = int(input("Do you wish to continue this transaction: 1: (yes) 2: (no) \n"))
        if ask_wish == 1:
            login()
        elif ask_wish == 2:
            print("Thank for banking with us.")
            exit()
        else:
            print("Invalid command")
            login()

        
        
    else:
        print("User not found")
        bankOperation(user_data)

        
        
    



africaMFB()