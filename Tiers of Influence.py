#Name: Drew Zambelli
#Email: drew.zambelli04@myhunter.cuny.edu
#Date: October 1, 2021
#This program does Influencer Tiers

sheep = int(input("enter amount of social media followers:"))


if sheep <= 0:
    print("Your influencer tier is: Error")

if sheep < 1000 and sheep > 0:
    print("Your influencer tier is: Hyper Influencer")

if sheep >= 1000 and sheep < 10000:
    print("Your influencer tier is: Nano Influencer")

if sheep >= 10000 and sheep < 100000:
    print("Your influencer tier is: Micro Influencer")

if sheep >= 100000 and sheep < 500000:
    print("Your influencer tier is: Mid-Tier Influencer")

if sheep >= 500000 and sheep < 1000000:
    print("Your influencer tier is: Macro Influencer")

if sheep >= 1000000:
    print("Your influencer tier is: Celebrity Influencer")
