from textblob import TextBlob
from textblob import Word
import math


s1 = "The Colt Python is a .357 Magnum caliber revolver formerly manufactured by Colts Manufacturing Company of Hartford, Connecticut.It is sometimes referred to as a Combat Magnum."

s2 = "Python is a 2000 made-for-TV horror movie directed by Richard Clabaugh. The film features several cult favorite actors, including William Zabka of The Karate Kid fame, Wil Wheaton, Casper Van Dien, Jenny McCarthy, Keith Coogan, Robert Englund (best known for his role as Freddy Krueger in the A Nightmare on Elm Street series of films), Dana Barron, David Bowe, and Sean Whalen."

doc1 = TextBlob(s1)

doc2 = TextBlob(s2)

doc = doc1

chooseWord = Word('Magnum')

docList=[doc1,doc2]


def wordmatch(doc, word):
    if wordList.count(word)>0:
        return 1
    else: return 0

scores ={}
wordtimes =0

for doc in docList :
    wordList =doc.words
    print('===============================================')
    print('Top words in Documents are:')
    for word in wordList:
        wordtimes = wordtimes + wordmatch(doc,word)
        tf = wordList.count(word)
        ntf = (float)(tf)/(float)(len(wordList))
        sub = (float)(len(docList))/(float)(wordtimes)
        idf = 1 + math.log(sub)
        tfidf = ntf*idf

        scores.update({word:tfidf})
        sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for word, score in sorted_words[:4]:
        print("Word: {}, TF-IDF: {}".format(word, round(score, 5)))












    
