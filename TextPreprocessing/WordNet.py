from nltk.corpus import wordnet

syns = wordnet.synsets("program")

print (syns[0].lemmas()[0].name())
print (syns[0].name())
print (syns[0].definition())
print (syns[0].examples())

synonyms = []
antonyms = []
for syn in wordnet.synsets("good"):
    for i in syn.lemmas():
        synonyms.append(i.name())
        if i.antonyms():
            antonyms.append(i.antonyms()[0].name())

print (set(synonyms))

print (set(antonyms))

word1 = wordnet.synset("ship.n.01")
word2 = wordnet.synset("boat.n.01")

print (word1.wup_similarity(word2))
