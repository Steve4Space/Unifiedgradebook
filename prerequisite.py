import os

howtocont = ""

cont = True

while cont == True:
  howtocont = input("Are you a new or returning future?(New/Returning)")
  if howtocont == 'New':
    break
  if howtocont == 'Returning':
    break
  print("Whoops! I can't understand you. Please ensure you're using proper and exact typing.")

if howtocont == 'New':
  os.system('python accounts/DirectServer/NewCreateAccount.py')
else:
  os.system('python accounts/DirectServer/Logon.py')