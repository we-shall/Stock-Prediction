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
various tags:

| Tags | Meaning With Example|
| ---- |:-------:|
| CC	| Coordinating conjunction |
| CD |	Cardinal digit |
| DT	| Determiner |
| EX |	Existential there (like: "there is", think of it like "there exists") |
| FW	| Foreign word |
| IN |	Preposition/subordinating conjunction |
| JJ	| Adjective	'big' |
| JJR |	Adjective, comparative	'bigger' |
| JJS	| Adjective, superlative	'biggest' |
| LS	| List marker	1) |
| MD	| Modal	could, will |
| NN	| Noun, singular 'desk' |
| NNS |	Noun, plural	'desks' |
| NNP	| Proper noun, singular	'Harrison' |
| NNPS	| Proper noun, plural	'Americans' |
| PDT |	Predeterminer	'all the kids' |
| POS	| Possessive ending	parent's |
| PRP |	Personal pronoun	I, he, she |
| PRP$	| Possessive pronoun	my, his, hers |
| RB |	Adverb	very, silently |
| RBR | Adverb, comparative	better |
| RBS	| adverb, superlative	best |
| RP	| Particle	give up |
| TO	| To	go 'to' the store |
| UH	| Interjection	errrrrrrrm |
| VB	| Verb, base form	take |
| VBD	| Verb, past tense	took |
| VBG	| Verb, gerund/present participle	taking |
| VBN	| Verb, past participle	taken |
| VBP	| Verb, sing. present, non-3d	take |
| VBZ	| Verb, 3rd person sing. present	takes |
| WDT	| Wh-determiner	which |
| WP	| Wh-pronoun	who, what |
| WP$	| Possessive wh-pronoun	whose |
| WRB	| Wh-abverb	where, when |
