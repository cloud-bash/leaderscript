import re
import random
from random import choice
# Two empty lists
principles = []
paragraphs = []
# open "aws.txt" in read mode
file = open("awslp.txt","r")
# this becomes useful during the "for" loop
count = 0
for line in file:
    if count % 2 == 0:
        newline = line.replace("\n", '')
        principles.append(newline)
    else:
        newline = line.replace("\n", '')
        paragraphs.append(newline)
    count+=1
# I was going to do this with a dictionary, 
# and found this cool method to create a dict from two lists
# awslp = dict(zip(principles, paragraphs))
listlen = len(principles)
rand = random.randint(0,listlen-1)
awslp = [principles,paragraphs]
response = input(awslp[1][rand]+"\n")
answer = awslp[0][rand]
if response == answer:
    print("you're good")
else:
    print("try again?")
# print(question)
# # Make a repeatable game
# def gameloop(response=0):
#   response = input("Do you want to play a game?" if response == 0 else "Do you want to play again?")
#   if response == "yes":
#     gameloop(response)
#   else:
#     print("GAME OVER")
# # Then be able to guess the answer
# gameloop()