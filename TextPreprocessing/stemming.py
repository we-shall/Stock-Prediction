
#use of stemming
#steming means converting V3 to v1

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer

ps = PorterStemmer()
example_words = ["python","pythonely","pythoned","pythoner","pythoning","grows","leaves","fairly"]

for w in example_words:
    print (ps.stem(w))


print ("\n\n")
#using SnowBallStemmer
sb = SnowballStemmer('english')
for w in example_words:
    print (sb.stem(w))


#hunspeir which uses dictionary for stemming data

