import nltk
from nltk.corpus import gutenberg
from nltk.tokenize import sent_tokenize


#print nltk.__file__ #for getting the filw location

sample = gutenberg.raw("bible-kjv.txt")

tok = sent_tokenize(sample)

print (tok[5:15])




