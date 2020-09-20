from user import User

users = [
    User(1, 'jose', 'pass1'),
    User(2, 'fernando', 'pass2'),
    User(3, 'manolo', 'pass3'),
]

username_table = {u.username: u for u in users} # dictionary comprenhension
# username_table['Jose'] --> for call the username object
userid_table = {u.id: u for u in users}


def authenticate(username, password):
    # check if user exist, if so return user
    # this way cus if call ustable['name'] that not exist will return an error
    user = username_table.get(username, None)

    if user and password == user.password:
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)
