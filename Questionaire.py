
info = []
addinfo = []

print("Hello there, I'm going to ask you a few questions about yourself.")
info.append(input("What's your name: "))
info.append(input("Name your favourite colour: "))
info.append(input("Give me a country you'd like to visit: "))
addinfo.append(input("\nWould you like to add some additional information about yourself?\n\nWrite a short sentence about yourself here: "))
print(info,"\n",addinfo)
print("Is there anything you'd like to remove from the list?")
info.remove(input(""))
print("\n","Here is your updated list",info)






