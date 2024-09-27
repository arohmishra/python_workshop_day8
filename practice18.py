#Write a Python program to shuffle the elements of a given list.
#Use random.shuffle()

import random

num = [1,2,3,4,5]
print("original list :",num)
random.shuffle(num)
print("shuffled list :",num)

char = ["a","b","c","d","e"]
print("original list:",char)
random.shuffle(char)
print("shuffled list :",char)