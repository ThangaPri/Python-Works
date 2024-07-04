# Generate Randon password based on user inputs
# import random library
import random

print("Welcome to Random password generation")

# Get the number of password and length of the password
pass_num = int(input("Please enter the number of password to be generated:"))
pass_len = int(input("Please length of password should be:"))

# Assign the random characters
randomchars = "ABCDEFGHIJKLMOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()"

# create random password using random.choice method
print("Here the passowrd outcomes:")
for x in range(pass_num):
    pwd = ""
    for chars in range(pass_len):
        pwd = pwd+random.choice(randomchars)
    print(pwd)
