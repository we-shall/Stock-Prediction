from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mod as s

#consumer key, consumer secret, access token, access secret.
ckey="WG6WMvY5QnoKgb52MG9MZFAmt"
csecret="2ZtKnXu1LjshjwNo6sgUV02vHQfr1wchosNRj68k0ARd1vrz7U"
atoken="1361391944-W2UVxbnbAt16XHit7F3XBMKPG9wuvGQZio9jQyV"
asecret="SzuZ2XhHEW2YQJGrQfbVtNslZyYr5m49hm5l776GXoXb3"


class listener(StreamListener):

    def on_data(self, data):
	all_data = json.loads(data)

	tweet = all_data["text"]
	sentiment_value, confidence = s.sentiment(tweet)
	print(tweet, sentiment_value, confidence)
	if confidence*100 >= 80:
	    output = open("twitter-out.txt","a")
	    output.write(sentiment_value)
	    output.write('\n')
	    output.close()

	    return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["happy"])
#instead happy you can add any other keyword you want to extract