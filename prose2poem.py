#! /usr/bin/env python

import pronouncing as pr
import sys, glob, codecs
from textblob import TextBlob as tb

files = glob.glob(sys.argv[1]+"*.txt")

def syllable_counts(sentence):
    count = 0
    for word in sentence.words:
        word = word.lower()
        p = pr.phones_for_word(word)
        if len(p) > 0:
            sc = pr.syllable_count(p[0])
            count += sc
    return count

def create_dict(shorts):
    syl_dict = {}
    for sent in shorts:
        count = syllable_counts(sent)
        if count not in syl_dict:
            syl_dict[count] = [sent]
        else:
            syl_dict[count].append(sent)
    return syl_dict

count = 0
for file in files:
    count += 1
    with codecs.open(file, 'r', 'utf-8', errors='ignore') as f:
        text = f.read()
    blob = tb(text)
    shorts = [s for s in blob.sentences if len(s.words) <= 10]
    syl_dict = create_dict(shorts)
    poem = [str(s)+'\n' for s in syl_dict[7]]
    with open('seven_syllables.md', 'a') as wf:
        wf.write('## '+file[6:]+'\n')
        wf.write('\n')
        wf.writelines(poem)
        wf.write('\n')
    print 'Wrote poem '+str(count)+'!'
