from sklearn.feature_extraction.text import TfidfVectorizer
from textblob import Word
from textblob import TextBlob 



s1 ='State of Japan is an island country in East Asia.'
s2 ='Located in the Pacific Ocean, it lies off the eastern coast of the Asian continent and stretches from the Sea of Okhotsk in the north to the East China Sea and the Philippine Sea in the south'
s3= 'The kanji that make up Japans name mean sun origin, and it is often called the Land of the Rising Sun.'
s4='The Greater Tokyo Area is the most populous metropolitan area in the world with over 38 million people.'

t1 =TextBlob(s1)
t2 =TextBlob(s2)
t3 =TextBlob(s3)
t4 =TextBlob(s4)

document = [t1,t2,t3,t4]
print(document)
doclist=[]
for doc in document:
    WordList = doc.words
    for word in WordList :
        doclist.append(word)
        
doclist = WordList(doclist)
print(doclist)

tflist=[]
for word in doclist:
    tf = doclist.words.count(word)
    tflist.append(tf)
    
print(tflist)

'''

for doc in document:
    WordList = doc.words
    for word in WordList :
        tf = doc.words.count(word)
        tflist.append(tf)
        print('{0} -- {1} '.format(word,str(tf)))
        
print('=============================')        

dataset =[s1,s2,s3,s4]

print(dataset)
print(tflist)

tfidf = TfidfVectorizer(stop_words='english')

tfidf.fit(dataset)
#print(tfidf.vocabulary_)

data = tfidf.vocabulary_

#print(data.keys())
#print(data.values())
datalist =[]
for key in data.keys():
    print('{0}   {1}'.format(key,data[key]))
    datalist.append(data[key])

print(datalist)
from sklearn.cluster import KMeans

print(len(tflist))
print(len(datalist))

#x = list(zip(tflist,datalist))
model = KMeans(n_clusters=3)

model.fit_transform(tfidf)
import matplotlib.pyplot as plt

plt.scatter(tfidf,datalist,c =tflist)
plt.show()

'''
