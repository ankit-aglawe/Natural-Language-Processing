from textblob import TextBlob 

def para():
    para = 'Beautiful is better than ugly.Explicit is better than implicit.Simple is better than complex.'

    blob = TextBlob(para)
    print(blob.sentences)
    print(blob.words)
    print(blob.noun_phrases)


def string():
    string = input('Enter a string : ')
    string =str(string)
    string = TextBlob(string)
    cor = string.correct()
    print(cor)
    print('===========================')
    print(cor.translate(from_lang='en',to='fr'))


def extrs():
    filename = 'india.txt'
    fil = open(filename,'r')
    v = fil.read()
    print(v)

    blob = TextBlob(v)
    print(blob.sentences)

    usr = input('enter an int: ')
    usr = int(usr)

    print(blob.sentences[usr])
    print(blob.words[usr])

extrs()