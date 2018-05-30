from nltk.tokenize import sent_tokenize, word_tokenize

# tokenizing;
# lexicons : creation of dictionary
# corporas : body of texts
# investor speak and english speak
# investor speak : bulls and bears have different meaning
text = ''' Natural Language Processing is the task we give computers to read and
    understand (process) written text (natural language). By far, the most
    popular toolkit or API to do natural language processing is the Natural
    Language Toolkit for the Python programming language. 
    The NLTK module comes packed full of everything from trained algorithms to
    identify parts of speech to unsupervised machine learning algorithms to help
    you train your own machine to understand a specific bit of text. 
    NLTK also comes with a large corpora of data sets containing things like chat logs,
    movie reviews, journals, and much more!
    Bottom line, if you're going to be doing natural language processing,
    you should definitely look into NLTK!'''

#print (sent_tokenize(text))
#print (word_tokenize(text))

for t in word_tokenize(text):
    print (t)




