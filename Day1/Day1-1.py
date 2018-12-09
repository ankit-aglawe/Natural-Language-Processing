from textblob import TextBlob

a = raw_input("enter a string : ")

a=str(a)

sent = TextBlob(a)

b= sent.correct()

print b

c= sent.translate(to='fr')

print 'Translation in french is :',c



