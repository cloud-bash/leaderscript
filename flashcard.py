# A script to take a dictionary and allow the user to match their knowledge against a dictionary
# So far I've got the leadership principles to work with, but it could be made more generic.

import re
from random import choice
principles = []
paragraphs = []
file = open("awslp.txt","r")
count = 0
for line in file:
    if count % 2 == 0:
        newline = line.replace("\n", '')
        principles.append(newline)
    else:
        newline = line.replace("\n", '')
        paragraphs.append(newline)
    count+=1
awslp = dict(zip(principles, paragraphs))
   
print(choice(paragraphs))