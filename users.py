# ------------------------
# IMPORTS
# ------------------------
import json
import bcrypt
import re

# ------------------------
# CONSTANTS
# ------------------------
json_user_file = 'metadata/users.json'
json_email_file = 'metadata/emails.json'

# ------------------------
# FUNCTINOS
# ------------------------
# ------------------------
# VALIDATION STUFF
# ------------------------
def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')

def verify_password(password, stored_hash):
    return bcrypt.checkpw(password.encode('utf-8'), stored_hash.encode('utf-8'))

def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None


# ------------------------
# ACCOUNT STUFF
# ------------------------
def make_account(username, password, email):
    if not is_valid_email(email):
        return False, "Invalid email format."

    try:
        # Load existing user data
        with open(json_user_file, "r") as file:
            users = json.load(file)

        with open(json_email_file, "r") as file:
            emails = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        return False, f"Error loading user data: {str(e)}"

    # Check for duplicate username and email
    if username in users: 
        return False, "Username already in use."

    if email in emails:
        return False, "Email already in use."

    # Hash password and create the new account
    users[username] = {
        "password": hash_password(password),
        "email": email,
        "admin": False
    }

    emails[email] = username

    try:
        # Save the new data back to the files
        with open(json_user_file, "w") as file:
            json.dump(users, file, indent=4)

        with open(json_email_file, "w") as file:
            json.dump(emails, file, indent=4)
    except (IOError, json.JSONDecodeError) as e:
        return False, f"Error saving user data: {str(e)}"

    return True, "Account created successfully."

def check_login(username, password):
    try:
        with open(json_user_file, "r") as file:
            users = json.load(file)
        
        # Check if the username exists
        if username not in users:
            return False, "Username not found."

        # Verify password
        if verify_password(password, users[username]['password']):
            return True, "Login successful."
        else:
            return False, "Incorrect password."

    except (FileNotFoundError, json.JSONDecodeError) as e:
        return False, f"Error loading user data: {str(e)}"


def turn_admin(username):
    try:
        with open(json_user_file, "r") as file:
            users = json.load(file)

        if username not in users:
            return False, "User not found."

        users[username]["admin"] = True

        with open(json_user_file, "w") as file:
            json.dump(users, file, indent=4)

        return True, "User is now an admin."

    except (FileNotFoundError, json.JSONDecodeError) as e:
        return False, f"Error loading user data: {str(e)}"


def turn_user(username):
    try:
        with open(json_user_file, "r") as file:
            users = json.load(file)

        if username not in users:
            return False, "User not found."

        users[username]["admin"] = False

        with open(json_user_file, "w") as file:
            json.dump(users, file, indent=4)

        return True, "User is no longer an admin."

    except (FileNotFoundError, json.JSONDecodeError) as e:
        return False, f"Error loading user data: {str(e)}"


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

