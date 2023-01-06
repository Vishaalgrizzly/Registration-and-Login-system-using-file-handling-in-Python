import re
def email_validation(ea):
    if re.search(r'^(?![0-9])+[a-z|\d]+@[a-z]+\.[a-z]{2,}+$', ea):
        return True
    else:
        return False
def password_validation(pw):
    if re.search (r'[a-z]', pw) and re.search(r'[A-Z]', pw) and re.search(r'[0-9]', pw) and re.search(r'[^a-zA-Z0-9]', pw):
        return True
    else:
        return False
def email_verif(ea):
    with open("database.txt", "r") as db:
        if ea in db.read():
            print ("Email verified, enter the password")
            return True
        else:
            print ("User not registered, proceed with creating a new account")
            reg()
def pass_verif(ea, pw):
    db = open("database.txt", "r")
    for line in db:
        if ea in line and pw in line:
            print ("Login successful")
            return True
            break
    return ("Not found")
    db.close()
def pass_display(ea):
    with open("database.txt", "r") as db:
        lines = db.readlines()
        for line in lines:
            if ea in line:
                print ("Your password is - ", line.split(ea)[1])
                break
    return ("Not found")
def pass_change(ea, new_pass):
    if re.search(r'[a-z]', new_pass) and re.search(r'[A-Z]', new_pass) and re.search(r'[0-9]', new_pass) and re.search(r'[^a-zA-Z0-9]', new_pass):
        with open("database.txt", "r") as db:
            lines = db.readlines()
            for line in lines:
                string = line.split()
                if string[0] == ea:
                    old_name = string[0]
                    old_pass = string[1]
            with open(r'database.txt', 'r') as db:
                data = db.read()
                data = data.replace(old_pass, new_pass)
                with open(r'database.txt', 'w') as db:
                    db.write(data)
                    print ("Passwords successfully changed, here are the new credentials - ", ea, new_pass)
    else:
        print ("You have entered a weak password, redirecting to the login page")
        login()
def forget_password_email_ver(verify_email):
    with open("database.txt", "r") as db:
        if verify_email in db.read():
            print("Email is successfully verified")
            return True
        else:
            return False
def reg():
    ea = input("enter the email address - ")
    with open('database.txt') as db:
        if ea in db.read(): #To check if the user is already registered with the email address
            print("You have already registered, please enter a new email address")
            user_option = input("Enter your choice - Press 1 for registering new email address, 2 for login - ")
            homepage[user_option]()
        else:
            if email_validation(ea):
                pw = input("Enter the password - ")
                cpw = input ("Enter your password again to confirm - ")
                if pw == cpw:
                   if password_validation(pw):
                        db = open("database.txt", "a")
                        db.write(ea + "  " + pw + "\n")
                        db.close()
                        print("successfully registered")
                   else:
                     print("Weak password, restart the registration process")
                     reg()
                else:
                    print("Passwords don't match, re-enter your email address")
                    reg()
            else:
                #Statement block for entering wrong email address during registration
                print("invalid email address, Failed to register your email address")
                print("Begin your email address with a small letter and not with any special characters")
                reg()
def login():
    ea = input("Enter your registered email address - ")
    email_verif(ea)
    pw = input("Enter the password - ")
    if pass_verif(ea, pw) is True:
        print ("Welcome, user")
    else:
        user_option_1 = input("Enter 1 to retry"
                                      "Enter 2 if you have forgotten the password"
                                      " - ")
        if user_option_1 == "1":
            login()
        elif user_option_1 == "2":
            verify_email = input ("Enter your email address to proceed - ")
            if forget_password_email_ver(verify_email) is True:
                user_option_2 = input("Enter 1 if you want to display the password "
                                                       "Enter 2 if you want to change the password"
                                                       " - ")
                if user_option_2 == "1":
                    pass_display(ea)
                elif user_option_2 == "2":
                    new_pass = input("Enter the new password - ")
                    conf_new_pass = input ("Enter the new password again for confirmation - ")
                    if new_pass == conf_new_pass:
                        pass_change(ea, new_pass)
                    else:
                        print("The passwords entered do not match, redirecting to the login screen")
                        login()
                else:
                    print("Enter the right option, redirecting to login page")
                    login()
            else:
                print("The email address is incorrect")
        else:
            print("Enter a valid choice")
homepage = {
    "1":reg,
    "2":login
    }
user_option = input ("Enter your choice - "
                     "Press 1 for registration, 2 for login - ")
homepage[user_option]()
