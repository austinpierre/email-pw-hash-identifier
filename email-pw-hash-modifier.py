# str input can be email (with @email.com included) or a password
# program will need to take input, determine input type
# then create & return the SHA256 hashed identifier
import hashlib

input_type = ""
i = ""

def identifier(string):
    i = input_type + hashlib.sha256(string.encode('utf-8')).hexdigest()
    print(i)

identifier(input("Enter a password or email. Email must include '@email.com' "))

# WIP NOTES
# need to figure out how to determine input type between email and password,
# then add a tag to the hash
