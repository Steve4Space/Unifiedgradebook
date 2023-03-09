import json, os, time

print("New Account")

fname = input("What's your first name? ")
lname = input("What's your last name? ")
gen = input("What's your gender(male/female/other)?")
dname = input("What should your display name be? ")
password = input("Enter a password. ")
    
print('This data will be processed soon')

time.sleep(2)

os.system('clear') #cls for Windows(?)

print('Creating JSON')

data = {1: fname, 2: lname, 3: gen, 4: dname, 5: password}
print(data)

object = json.dumps(data, indent = 0)

with open('accounts/DirectServer/AccountData.json', "w") as outfile:
  outfile.write(object)

print("You will now be redirected to the log-in screen.")
os.system('python accounts/DirectServer/Logon.py')