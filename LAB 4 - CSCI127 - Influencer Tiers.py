#Name: Drew Zambelli
#Email: drew.zambelli04@myhunter.cuny.edu
#Date: October 1, 2021
#This program does Influencer Tiers

sheep = int(input("enter amount of social media followers:"))


if sheep <= 0:
    print("Your influencer tier is: Error")

elif sheep < 1000:
    print("Your influencer tier is: Hyper Influencer")

elif sheep < 10000:
    print("Your influencer tier is: Nano Influencer")

elif sheep < 100000:
    print("Your influencer tier is: Micro Influencer")

elif sheep < 500000:
    print("Your influencer tier is: Mid-Tier Influencer")

elif sheep < 1000000:
    print("Your influencer tier is: Macro Influencer")

elif sheep >= 1000000:
    print("Your influencer tier is: Celebrity Influencer")
