# A script to take a dictionary and allow the user to match their knowledge against a dictionary
# So far I've got the leadership principles to work with, but it could be made more generic.

import re

principles = []
details = []

file = open("awslp.txt","r")
count = 0
for line in file:
    if count % 2 == 0:
        newline = line.replace("\n", '')
        principles.append(newline)
    else:
        newline = line.replace("\n", '')
        details.append(newline)
    count+=1

lpdict = dict(zip(principles, details))    

print(lpdict)
