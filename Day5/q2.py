from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob


data =  open('data.txt','r')

a=data.read()

para =TextBlob(a)

sent=para.sentences


s1=str(sent[0])
s2=str(sent[1])
s3=str(sent[2])
s4=str(sent[3])



query ='NLP sits at the intersection of computer science, artificial intelligence, and computational linguistics'

tfidf = TfidfVectorizer()

dataset= [query,s1,s2,s3,s4]

matrix = tfidf.fit_transform(dataset)

dic = tfidf.vocabulary_

for key in dic.keys():
    print('{0}   {1}'.format(key,dic[key]))

print(cosine_similarity(matrix[0:1],matrix))


