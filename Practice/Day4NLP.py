from textblob import TextBlob 
import math 

def tfidf():
    doc1 = TextBlob('''TF-IDF stands for "Term Frequency, Inverse Document Frequency." It's a way to score the importance of words (or "terms") in a document based on how frequently they appear across multiple documents.''')

    doc2= TextBlob('''If a word appears frequently in a document, it's important. Give the word a high score.''')
    doc3 = TextBlob('''But if a word appears in many documents, it's not a unique identifier. Give the word a low score.''')

    docList = [doc1,doc2,doc3]

    wordtimes=0

    def wordmatch(word,doc):
        if wordList.count(word)>0:
            return 1
        else:
            return 0
    
    scores={}

    for i, doc in enumerate(docList):
        print('Important words from Doc {}'.format(i+1))
        wordList= doc.words
        for word in wordList:
            wordtimes = wordtimes + wordmatch(word,doc)
            tf = wordList.count(word)
            ntf = tf/len(wordList)
            sub = len(docList)/wordtimes
            idf = 1 + math.log(sub)
            tfidf = ntf*idf
            scores.update({word:tfidf})
            sorted_words = sorted(scores.items(),key=lambda x: x[1],reverse=True)
        for word,score in sorted_words[:4]:
            print('Word : {}, TF IDF: {}'.format(word,round(score,5)))
    
tfidf()