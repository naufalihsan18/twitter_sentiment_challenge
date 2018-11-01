import tweepy
from textblob import TextBlob

# Step 1 - Authenticate
consumer_key= 'gQBkb3Z1EeujprczFfhRJMWue'
consumer_secret= 'jhRx0XD1pXYb34wNc253r3x4n8wPSSatUyvHH2foqsN1alguN4'

access_token='1011975360274051073-rB9UBFwljXAt75SQaqhOO4HCoPiW8z'
access_token_secret='TiPW1ASS0ZK6BVIcs4RXZDgPhKh8Pr6ZcQvqi8Xn8UkRJ'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search('Bohemian Rhapsody')



#CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
#and label each one as either 'positive' or 'negative', depending on the sentiment 
#You can decide the sentiment polarity threshold yourself


for tweet in public_tweets:
    print(tweet.text)
    
    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")
