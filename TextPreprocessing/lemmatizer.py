from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print (lemmatizer.lemmatize("better",pos = "a"))
print (lemmatizer.lemmatize("better",pos = "n"))
print (lemmatizer.lemmatize("better"))
