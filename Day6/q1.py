from textblob import TextBlob

s1= 'India is Country'

t1 =TextBlob(s1)

print(t1.sentiment)

def SenCheck(sen):
    sen = str(sen)
    t2 = TextBlob(sen)
    p =t2.sentiment
    global posCount
    global negCount
    global neutCount

    posCount =0
    negCount =0
    neutCount =0

    if p.polarity>0:
        print('positive')
        posCount+=1
    elif p.polarity <0:
        print('Negative')
        negCount+=1
    elif p.polarity==0:
        print('Neutral')
        neutCount+=1

SenCheck(s1)
print('Total Positive Tweets are :{0}'.format(posCount))
print('Total Negative Tweets are :{0}'.format(negCount))
print('Total Neutral Tweets are :{0}'.format(neutCount))

print('===============================================')
    
    

#------------------------------------------------

import tweepy
import re

consumer_token =''
consumer_secret =''

access_token =''
access_token_secret =''

auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

fifa_tweets = api.user_timeline('@aFIFAcom',count=10)


posCount =0
negCount =0
neutCount =0

def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split()) 

for tweet in fifa_tweets:
    
    print('=================')
    print(tweet.text)
    t2 = TextBlob(tweet.text)
    
    print('=================')
    
    print(t2+'\n')
    p =t2.sentiment

    if p.polarity>0:
        #print('positive')
        posCount+=1
    elif p.polarity <0:
        #print('Negative')
        negCount+=1
    elif p.polarity==0:
        #print('Neutral')
        neutCount+=1    
    
print('Total Positive Tweets are :{0}'.format(posCount))
print('Total Negative Tweets are :{0}'.format(negCount))
print('Total Neutral Tweets are :{0}'.format(neutCount))
  


