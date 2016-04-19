#! /usr/bin/env python

import pronouncing as pr
import sys, glob
from textblob import TextBlob as tb
from random import choice, sample

files = glob.glob(sys.argv[1]+"*.txt")

blobs = []
for file in files:
    with open(file, 'r') as f:
        text = f.read()
        blob = tb(text)
        blobs.append(blob)

shorts = [s for s in blobs[0].sentences if len(s.words) <= 10]

def syllable_counts(sentence):
    count = 0
    for word in sentence.words:
        p = pr.phones_for_word(word)
        if len(p) > 0:
            sc = pr.syllable_count(p[0])
            count += sc
    return count



poem = sample(shorts, 10)

for p in poem:
    print p, syllable_counts(p)
