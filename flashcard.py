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

## pattern: Starts with upercase letter, then anything that is not puctuation (.!?), then ends with punctuation
pat = re.compile(r'([A-Z][^\.!?]*[\.!?])', re.M)

def gameloop(response=0):
    # TODO: Decouple the lists from the function, have the function accept two lists as arguments
  response = input("Welcome to the AWS Leadership Principle Quiz\nGiven the paragraph, enter the matching Leadership Principle. Press any key to continue\n" if response == 0 else "To quit enter 'q' or any key to continue.\n")
  if response != "q":
    rand = random.randint(0,listlen-1)
    paragraph = awslp[1][rand]
    # Take a random sentence from the paragraph to make it harder
    sentences = pat.findall(paragraph)
    prompt = choice(sentences)
    response = input(prompt+"\n")
    # Take a random sentence from the paragraph to make it harder
    answer = awslp[0][rand]
    if response == answer:
        print("you're good")
        # TODO: Allow a varying level of accuracy and response based on number of matching words
    else:
        print("That's not what what we were looking for, the answer is " + answer)
    gameloop(response)
  else:
    print("GAME OVER")

gameloop()