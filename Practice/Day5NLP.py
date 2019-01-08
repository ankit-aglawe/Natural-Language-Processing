from textblob import TextBlob 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def check():
    s1 = 'The oldest classical Greek and Latin writing had little or no space between words and could be written in boustrophedon (alternating directions).'
    s2 = 'In ancient manuscripts, another means to divide sentences into paragraphs was a line break (newline) followed by an initial at the beginning of the next paragraph.'
    s3 = 'An initial is an oversized capital letter, sometimes outdented beyond the margin of the text.'
    s4 = 'Outdenting is still used in English typography, though not commonly.'
    s5 = 'This style is very common in electronic formats, such as on the World Wide Web and email.'

    query = 'Python is a 2000 made-for-TV horror movie directed by Richard Clabaugh.'

    dataList = [query,s1,s2,s3,s4,s5]

    model = TfidfVectorizer()

    matrix = model.fit_transform(dataList)

    dic = model.vocabulary_ 

    for key in dic.keys():
        print('{} {}'.format(key,dic[key]))
    
    print(matrix)
    print(cosine_similarity(matrix[0:1],matrix))

def filecheck():
    filename = 'data.txt'
    fil = open(filename,'r')
    fil = fil.read()

    blob = TextBlob(fil)
    sen = blob.sentences

    s1 = str(sen[0])
    s2 = str(sen[1])
    s3 = str(sen[2])
    s4 = str(sen[3])
    

    print(s1)
    print(s2)
    print(s4)

    query ='Python is a 2000 made-for-TV horror movie directed by Richard Clabaugh'
    dataList = [query,s1,s2,s3,s4]
    model = TfidfVectorizer()
    matrix = model.fit_transform(dataList)

    dic = model.vocabulary_ 

    for key in dic.keys():
        print('{} {}'.format(key,dic[key]))
    
    print(cosine_similarity(matrix[0:1],matrix))


filecheck()
