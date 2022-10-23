# str input can be email (with @email.com included) or a password
# program will need to take input, determine input type
# then create & return the SHA256 hashed identifier
import hashlib

input_type = ""
i = ""

def user_input(string):
    # determine and set user input type
    if "@" or ".com" in string:
        input_type = "E"
        return input_type
    else:
        input_type = "P"
        return input_type

def identifier(string):
    i = input_type + hashlib.sha256(string.encode('utf-8')).hexdigest()
    print(i)

identifier(user_input(input("Enter a password or email. Email must include '@email.com' ")))

# WIP NOTES
# successfully returning hash identifier itself, but needs to have user input determined (email or password)
# and added to the beginning of the returned identifier.
# the hash identifier is not changing despite different inputs?