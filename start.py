from greetings import welcome
from auth import checkUser

feedback = welcome.greetUser()


username = feedback["user_username"]
password = feedback["user_password"]

result = checkUser.checkUserExists(username, password)

if result == None:
    print("User not found")
else:
    print("Welcome " + result["firstname"])








