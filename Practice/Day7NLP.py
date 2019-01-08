from sklearn.feature_extraction.text import TfidfVectorizer
from textblob import Word
from textblob import TextBlob 
import matplotlib.pyplot as plt
import numpy as np 
from sklearn.cluster import KMeans



s1 ='State of Japan is an island country in East Asia.'
s2 ='Located in the Pacific Ocean, it lies off the eastern coast of the Asian continent and stretches from the Sea of Okhotsk in the north to the East China Sea and the Philippine Sea in the south'
s3= 'The kanji that make up Japans name mean sun origin, and it is often called the Land of the Rising Sun.'
s4='The Greater Tokyo Area is the most populous metropolitan area in the world with over 38 million people.'


documents =[s1,s2,s3,s4]

def count():
    model = TfidfVectorizer(stop_words='english')
    matrix = model.fit_transform(documents)
    dic = model.vocabulary_ 
    for key in dic.keys():
        print('{} {}'.format(key,dic[key]))
count()

tfidf = TfidfVectorizer(stop_words='english')
tfidf.fit(documents)
dict = tfidf.vocabulary_
print(tfidf.vocabulary_)
counts = dict.values()

length = len(dict.keys())
x_lab = []
for key in dict.keys():
	x_lab.append(key)

print('Length :', length)
words = np.arange(0,length)

model = KMeans(n_clusters=length);
X = list(zip(words, counts))
model.fit(X)

print(model.labels_)
print(dict.keys())

plt.scatter(words,counts,c=model.labels_)
plt.xlabel("Words")
plt.ylabel("Occurance")
plt.xticks(words, x_lab, rotation=90)
#plt.legend(loc="best", labels=x_lab)
plt.show()


def n71():
        from sklearn.feature_extraction.text import TfidfVectorizer 
        from sklearn.cluster import KMeans 

        tfidf = TfidfVectorizer(stop_words='english')


        s1 ='State of Japan is an island country in East Asia.'
        s2 ='Located in the Pacific Ocean, it lies off the eastern coast of the Asian continent and stretches from the Sea of Okhotsk in the north to the East China Sea and the Philippine Sea in the south'
        s3= 'The kanji that make up Japans name mean sun origin, and it is often called the Land of the Rising Sun.'
        s4='The Greater Tokyo Area is the most populous metropolitan area in the world with over 38 million people.'


        documents =[s1,s2,s3,s4]

        matrix = tfidf.fit_transform(documents)
        dic =tfidf.vocabulary_

        print(tfidf.vocabulary_)
        print(dic.values())

        counts=dic.values()

        length = len(dic.keys())

        words = np.arange(0,length)

        X = list(zip(words,counts))
        model = KMeans()
        model.fit(X)

        X_lab =[]

        for key in dic.keys():
                X_lab.append(key)
        
        plt.scatter(words,counts,c=model.labels_)
        plt.xlabel('word')
        plt.ylabel('occurance')
        plt.xticks(words,X_lab,rotation=90)
        plt.show()

n71()
