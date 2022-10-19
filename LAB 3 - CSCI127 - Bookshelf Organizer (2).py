#Name: Drew Zambelli
#Email: drew.zambelli04@myhunter.cuny.edu
#Date: September 21, 2021
#This program organizes a list of books and authors

mess = input("Enter a list of books and their authors: ")

myList = mess.split("; ")

firstEntry = myList[0]

firstEntrySplit = firstEntry.split("-")

firstTitle = firstEntrySplit[0]
firstName = firstEntrySplit[1].split()

firstInitials = ""

for aname in firstName:
    firstInitials = firstInitials + aname[0] + "."

secondEntry = myList[1]
secondEntrySplit = secondEntry.split("-")
secondTitle = secondEntrySplit[0]
secondName = secondEntrySplit[1].split()

secondInitials = ""
for aname in secondName:
    secondInitials = secondInitials + aname[0] + "."

thirdEntry = myList[2]
thirdEntrySplit = thirdEntry.split("-")
thirdTitle = thirdEntrySplit[0]
thirdName = thirdEntrySplit[1].split()

thirdInitials = ""
for aname in thirdName:
    thirdInitials = thirdInitials + aname[0] + "."
    
if len(myList) < 4:
    
        print(firstTitle + "by " + firstInitials + "\n"
      + secondTitle + "by " + secondInitials + "\n"
      + thirdTitle + "by " + thirdInitials + "\n"
      + "Thank you for using my book organizer!")

elif len(myList) == 4:
    fourthEntry = myList[3]
    fourthEntrySplit = fourthEntry.split("-")
    fourthTitle = fourthEntrySplit[0]
    fourthName = fourthEntrySplit[1].split()

    fourthInitials = ""
    for aname in fourthName:
        fourthInitials = fourthInitials + aname[0] + "."
        
    print(firstTitle + "by " + firstInitials + "\n"
    + secondTitle + "by " + secondInitials + "\n"
    + thirdTitle + "by " + thirdInitials + "\n"
    + fourthTitle + "by " + fourthInitials + "\n"
    + "Thank you for using my book organizer!")
