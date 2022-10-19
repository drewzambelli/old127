#Name: Drew Zambelli
#Email: drew.zambelli04@myhunter.cuny.edu
#Date: September 14, 2021
#This program shifts the message by 5

myString = input("give me a sentence:")

print(myString)

for c in myString:
    oldLetter = c
    newNumber = ord(c)+5
    newLetter = chr(newNumber)
    print("{} shifted by 5 characters is:{}".format(oldLetter, newLetter))
