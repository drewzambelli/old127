#Name: Drew Zambelli
#Email: drew.zambelli04@myhunter.cuny.edu
#Date: September 14, 2021
#This program does Reversed Acronym

phrase = input("Enter a phrase: ")

print("Reversed phrase:", phrase[::1])

reversed = phrase[::-1]

backwards = reversed.split()

initial = ""
for aWord in backwards:
    initial = initial + aWord[-1]

print("Last letters of reversed words: " + initial.upper())
