import os 

os.system('clear')

print("Logon")
username = input("Enter your username: ")
password = input("Enter your password: ")

loop = 0
prntpword = ""
while loop<(len(password)):
  prntpword = prntpword + "*"
  loop = loop+1

os.system('clear')

print("Logon")
print("Enter your username: " + username)
print("Enter your password: " + prntpword)