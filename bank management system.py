print("WELCOME TO XYZ BANK")
def admin(id="admin", password="admin"):
    """ ADMIN LOGIN VERIFICATION """
    if(id=="admin" and password=="admin"):
        print("WELCOME ADMIN!")
        print("If you want to exit press 3")
    else:
        print("Invalid entry")

def complaint():
    """ Customer Complaints..... """
    print("1. difficult to perform transactions smoothly?")
    print("2. Account related problems?")
    print("3. Did not get FD certificate?")
    print("4. Did not get checkbook delivery sms?")

print("1. Admin")
print("2. Customer")
print("3. Exit")
ch = 1
while ch != 3:
    ch = int(input("Enter your choice :"))
    if ch == 1:
        u = input("Enter userid")
        p = input("Enter password")
        admin(u,p)
    if ch == 2:
        print("1: New register")
        print("2: Login")
        print("3: Complaint")
        print("4: Exit")
        cu = 1
        while cu != 4:
            cu = int(input("Enter choice: "))
            if cu == 1:
                n = input("Enter your name")
                m = input("Enter mobile number")
                a = input("Enter address")
                f = input("Enter father's name")
                print("Account Created")
            if cu == 2:
                u = input("Enter userid")
                p = input("Enter password")
                print("Login Successful")
                print("1: Deposit")
                print("2: Withdraw")
                print("3: FD")
                print("4: Exit")
                x = 1
                while x != 4:
                    x = int(input("Enter choice:"))
                    if x == 1:
                        a = int(input("Enter account no."))
                        amt = int(input("Enter amount to be deposit"))
                        print(amt, "is successfully deposited")
                    if x == 2:
                        a = int(input("Enter account no."))
                        amt = int(input("Enter amount to be withdrawn"))
                        print(amt, "is successfully withdrawn")
                    if x == 3:
                        a = int(input("Enter account no."))
                        m = int(input("Enter amount"))
                        t = int(input("Enter duration"))
                        print("Your FD will confirm soon")
                    if x == 4:
                        print("You are logged out")
            if cu == 3:
                complaint()
                comp = int(input("Select option: "))
                print("We'll look into the problem soon")
    if ch==3:
        print("THANK YOU FOR VISITING")