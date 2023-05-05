def greetUser():
    print("Welcome to the Jotter Application")
    username = input("Please enter your username: ")
    password = input("Enter your password: ")

    return {
        "user_username": username,
        "user_password": password
    }
