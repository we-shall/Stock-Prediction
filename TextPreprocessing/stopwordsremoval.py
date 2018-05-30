from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


#learn more about corpus library
text = "This an example of tokenize and stop words stop words are those words which has no role in analysing sentiment of text"

stop_words = set(stopwords.words("english"))
#print stop_words
text_token = word_tokenize(text)

#filter tokenized sentence
filtered_text = []
'''for text in text_token:
    if text not in stop_words:
        filtered_text.append(text)
print ("filtering done!") '''

filtered_text = [w for w in text_token if w not in stop_words]
print (filtered_text)


