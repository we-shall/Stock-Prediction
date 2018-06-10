#### Tokenise data:

Tokenise means to convert long string of data into tokens i.e converting a string of sentence or paragraph to be stored 
as list of words. For tokenising we are using nltk tokeniser **word_tokenise** or **sent_tokenise** from nltk library

#### Stopwords Removal

Stop words are natural language words which have very little meaning, such as "and", "the", "a", "an", and similar words.
These stopwords are captured using stopword lib present in nltk.

#### Stemming

Stemming algorithms attempt to automatically remove suffixes (and in some cases prefixes) in order to find the “root word” 
or stem of a given word
**PorterStemmer** and **SnowBallStemmer** are stemming techinque which are present in the nltk.stem library.

#### Lemmatizing

lemmatizing means to convert a word in its noun or verb form.
In nltk it is implemented using **WordNetLemmatizer**

#### PartOfSpeech Tagging

The part of speech tagging is meant to tag a word so that word can be categorised as noun, verb, adverb etc.
various tags::
CC	coordinating conjunction,
CD	cardinal digit,
DT	determiner,
EX	existential there (like: "there is" ... think of it like "there exists"),
FW	foreign word,
IN	preposition/subordinating conjunction,
JJ	adjective	'big',
JJR	adjective, comparative	'bigger',
JJS	adjective, superlative	'biggest',
LS	list marker	1)
MD	modal	could, will,
NN	noun, singular 'desk',
NNS	noun plural	'desks',
NNP	proper noun, singular	'Harrison',
NNPS	proper noun, plural	'Americans',
PDT	predeterminer	'all the kids',
POS	possessive ending	parent's,
PRP	personal pronoun	I, he, she,
PRP$	possessive pronoun	my, his, hers,
RB	adverb	very, silently,,
RBR	adverb, comparative	better,
RBS	adverb, superlative	best,
RP	particle	give up,
TO	to	go 'to' the store.,
UH	interjection	errrrrrrrm,
VB	verb, base form	take,
VBD	verb, past tense	took,
VBG	verb, gerund/present participle	taking,
VBN	verb, past participle	taken,
VBP	verb, sing. present, non-3d	take,
VBZ	verb, 3rd person sing. present	takes,
WDT	wh-determiner	which,
WP	wh-pronoun	who, what,
WP$	possessive wh-pronoun	whose,
WRB	wh-abverb	where, when"""
