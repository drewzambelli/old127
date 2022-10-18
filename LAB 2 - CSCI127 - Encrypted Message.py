#Name: Drew Zambelli
#Email: drew.zambelli04@myhunter.cuny.edu
#Date: September 14, 2021
#This program does Encrypted Message

message = input("Enter a word:")

codedWord = ""
for c in message:
    offset = ord(c) - ord("A") + 13
    wrap = offset % 26
    newLetter = chr(ord("A")+wrap)
    codedWord = codedWord + newLetter

print("Your word in code is {}".format(codedWord))
