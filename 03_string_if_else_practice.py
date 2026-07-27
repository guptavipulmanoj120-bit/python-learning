# Admin Login
name = input("Enter your name: ")

if name.lower() == "admin":
    print("Welcome Admin!")
else:
    print("Access Denied")

# Favourite Language
language = input("Enter your favourite language: ")

if language.lower() == "python":
    print("Great choice!")
else:
    print("Keep Learning!")

# Password Checker
password = input("Enter your password: ")

if password == "123vipul":
    print("Login Successful")
else:
    print("Invalid Password")

# Gmail Checker
email = input("Enter your email: ")

if email.endswith("@gmail.com"):
    print("Valid Gmail Address")
else:
    print("Not a Gmail Address")

# Name Length
name = input("Enter your name: ")

if len(name) >= 5:
    print("Long Name")
else:
    print("Short Name")

# City Checker
city = input("Enter your city: ")

if city.lower() == "mumbai":
    print("You are from Maharashtra.")
else:
    print("You are from another city.")

# Username Validation
name = input("Enter your username: ")

if len(name) >= 5 and name.lower().startswith("v") and " " not in name:
    print("Valid Username")
else:
    print("Invalid Username")