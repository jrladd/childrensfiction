#! /usr/bin/env python

import pronouncing as pr
import sys, glob
from textblob import TextBlob as tb
from random import choice

files = glob.glob(sys.argv[1]+"*.txt")

blobs = []
for file in files:
    with open(file, 'r') as f:
        text = f.read()
        blob = tb(text)
        blobs.append(blob)

def get_stresses(wordlist):
    stresses = []
    for word in wordlist:
        stress = pr.stresses_for_word(word)
        if len(stress) > 0:
            stress = stress[0]
            stresses.append(stress)
    stresses = ''.join(stresses)
    return stresses

def is_iambic(stress):
    if len(stress) == 10 and lev.distance(str(stress), "0101010101") <= 5:
        return True
    else:
        return False

def find_iambic(stress):
    if "0101010101" in stress:
        return True

# for s in blobs[0].ngrams(n=10):
#     stress = get_stresses(s)
#     if find_iambic(stress) == True:
#         print s, stress

for s in blobs[0].sentences:
    if len(s.words) <= 10:
        print s
# def create_dict(blob):
#     stress_dict = {}
#     for w in blob.tags:
#         stress = pr.stresses_for_word(w[0])
#         if len(stress) > 1:
#             stress = str(stress[0])
#         else:
#             stress = str(stress)
#         if stress not in stress_dict:
#             stress_dict[stress] = [w]
#         else:
#             stress_dict[stress].append(w)
#     return stress_dict
#
# def make_line(sd):
#     line = [choice(sd['0']), choice(sd['10']), choice(sd['1']), choice(sd['010']), choice(sd['10']), choice(sd['1'])]
#     return line
#
# stress_dict = create_dict(blobs[0])
#
# count = 0
# while count <= 14:
#     count += 1
#     print make_line(stress_dict)
