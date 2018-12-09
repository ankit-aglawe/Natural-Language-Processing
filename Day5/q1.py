from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.metrics.pairwise import cosine_similarity

s1 ='The field of study that focuses on the interactions between human language and computers is called Natural Language Processing, or NLP for short'
s2 ='Natural Language Processing is a field that covers computer understanding and manipulation of human language, and its ripe with possibilities for new gathering'
s3 ='NLP is a way for computers to analyze, understand, and derive meaning from human language in a smart and useful way'
s4 ='NLP is characterized as a hard problem in computer science.'
s5 ='NLP algorithms are typically based on machine learning algorithms. Instead of hand-coding large sets of rules'


query ='NLP sits at the intersection of computer science, artificial intelligence, and computational linguistics'

tfidf = TfidfVectorizer()

dataset= [query,s1,s2,s3,s4,s5]

matrix = tfidf.fit_transform(dataset)

dic = tfidf.vocabulary_

for key in dic.keys():
    print('{0}   {1}'.format(key,dic[key]))

print(cosine_similarity(matrix[0:1],matrix))


