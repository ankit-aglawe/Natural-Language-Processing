from textblob import TextBlob 
import tweepy

def sentCheck():
    sent = input('enter a sentence : ')
    sent =str(sent)
    posCount=0
    negCount=0
    neutCount=0

    blob = TextBlob(sent)
    if blob.sentiment.subjectivity==0.0:
        print('This is fact')
    else:
        if blob.sentiment.polarity>0:
            print('positive')
            posCount +=1
        elif blob.sentiment.polarity <0:
            print('Negative')
            negCount +=1
        elif blob.sentiment.polarity==0.0:
            print('neutral')
            neutCount +=1
    print('Positve :',posCount)
    print('Negative : ',negCount)
    print('Neutral : ',neutCount)


def tweet():
    consumer_key =''
    consumer_secret =''

    access_token =''
    access_token_secret =''
    auth = tweepy.OAuthHandler(consumer_key,consumer_token_secret)
    auth.set_access_token(access_token,access_token_secret)

    api = tweepy.API(auth)

    fifa_tweets = api.user_timeline('@FIFAcom',counts=10)
    posCount=0
    negCount=0
    neutCount=0

    for tweet in fifa_tweets:
        tweet = tweet.text
        print(tweet) 
        blob = TextBlob(tweet)
        if blob.sentiment.polarity>0:
            print('positive')
            posCount+=0
        elif blob.sentiment.polarity<0:
            print('negative')
            negCount+=0
        elif blob.sentiment.polarity==0.0:
            print('neutral')
            neutCount+=1
        print('=====================')
    print('Positve :',posCount)
    print('Negative : ',negCount)
    print('Neutral : ',neutCount)   


def n63():
    consumer_key ='psPgtumegDQSQxNzjPdhH4vnc'
    consumer_secret ='GYcw7bDGbuzBL6air0Up41JVCXwFufvErMaaY6WCEYsAItbiyp'

    access_token ='382979839-nNfkNGqjKl9PuozFqeydRrmShwcmdBO5ISTQ9bkm'
    access_token_secret ='MItSLDoLVh6RjRvVRndiy6jAuzc3kzSZoArzpNsoizKQm'

    auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)

    api = tweepy.API(auth)

    fifa_tweets = api.user_timeline('@FIFAcom',counts=10)

    for tweet in fifa_tweets:
        tweet = tweet.text
        blob = TextBlob(tweet)
        if blob.sentiment.polarity>0:
            print('Positive')
            posCount+=1
        elif blob.sentiment.polarity<0:
            print('Negative')
            negCount+=0
        elif blob.sentiment.polarity==0.0:
            print('neutral')
            neutCount+=1
    print('positive ', posCount)
    print('negative ',negCount)
    print('Neutral 'neutCount)

    
