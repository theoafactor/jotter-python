def checkUserExists(username, password):
    ## check our database if the user exists
    from auth import database
    registeredUsers = database.registeredUsers
    for user in registeredUsers:
        if user["email"] == username and user["password"] == password:
            ## the user is registered 
            return user
    else:
        return None