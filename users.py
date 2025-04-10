# ------------------------
# IMPORTS
# ------------------------
import json
import bcrypt

# ------------------------
# CONSTANTS
# ------------------------
json_user_file = 'metadata/users.json'
json_email_file = 'metadata/emails.json'

# ------------------------
# FUNCTINOS
# ------------------------
# ------------------------
# PASSWORD STUFF
# ------------------------
def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')

def verify_password(password, stored_hash):
    return bcrypt.checkpw(password.encode('utf-8'), stored_hash.encode('utf-8'))

# ------------------------
# ACCOUNT STUFF
# ------------------------
def make_account(username, password, email):
    with open(json_user_file, "r") as file:
        users = json.load(file)

    with open(json_email_file, "r") as file:
        emails = json.load(file)

    if username in users: 
        return (False, "username in use")

    if email in emails:
        return (False, "email in use")

    users[username] = {
        "password": hash_password(password),
        "email": email,
        "admin": False
    }

    emails[email] = username

    with open(json_user_file, "w") as file:
        json.dump(users, file, indent=4)

    with open(json_email_file, "w") as file:
        json.dump(emails, file, indent=4)

    # implement a way for the website to show the errors that occur

def check_login(username, password):
    with open(json_user_file, "r") as file:
        users = json.load(file)
    
    return verify_password(password, users[username]['password'])

def turn_admin(username):
    with open(json_user_file, "r") as file:
        users = json.load(file)

    users[username]["admin"] = True

    with open(json_user_file, "w") as file:
        json.dump(users, file, indent=4)

def turn_user(username):
    with open(json_user_file, "r") as file:
        users = json.load(file)

    users[username]["admin"] = False

    with open(json_user_file, "w") as file:
        json.dump(users, file, indent=4)

# ------------------------
# TESTING
# ------------------------

'''
    username: SuvidUser
    password: abcdef123456
    email: Suvid2004@gmail.com

    username: SuvidAdmin
    password: ABCDEF!@#$%^
    email: Suvid@outlook.com
'''

