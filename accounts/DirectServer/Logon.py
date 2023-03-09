import os, json, time

def prnt(user, passw):
  os.system('clear')
  print("Logon")
  print("Enter your username: " + user)
  print("Enter your password: " + passw)

os.system('clear')

print("Logon")
username = input("Enter your username: ")
password = input("Enter your password: ")

loop = 0
prntpword = ""
while loop<(len(password)):
  prntpword = prntpword + "*"
  loop = loop+1

prnt(username, prntpword)

data = {1: username,2: password}
print(data)

object = json.dumps(data, indent = 0)
with open('accounts/DirectServer/RequestTokenLog.json', "w") as outfile:
  outfile.write(object)
  
time.sleep(1)

