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
#
#Some necessary globals for the game to work
listlen = len(principles)
awslp = [principles,paragraphs]

def gameloop(response=0):
  response = input("Welcome to the AWS Leadership Principle Quiz\nGiven the paragraph, enter the matching Leadership Principle. Press any key to continue\n" if response == 0 else "Press ""q"" to exit or any key to continue.")
  if response != "q":
    rand = random.randint(0,listlen-1)
    response = input(awslp[1][rand]+"\n")
    answer = awslp[0][rand]
    if response == answer:
        print("you're good")
    else:
        print("That's not what what we were looking for, the answer is " + answer)
    gameloop(response)
  else:
    print("GAME OVER")

gameloop()