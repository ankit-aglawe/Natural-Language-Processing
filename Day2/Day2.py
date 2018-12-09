from textblob import Word

w = Word("book")

print(" Plural noun is :" +" "+ w.pluralize())

#------------------------------------------------------------------------


x = Word("trees")

print(" Singular noun is :" +" "+ x.singularize())


#------------------------------------------------------------------------


from textblob import TextBlob

sent=TextBlob(raw_input("Enter a sentence :"))
      

for word, tag in sent.tags:
      print(word+" "+tag)
      
    
#--------------------------------------------------------------------------


f = open("india.txt","r")

text= f.read()

para = TextBlob(text)

print("Total words are: ", len(para.words))

print("Total sentences are :"), len(para.sentences)

noun=set()

for word,tag in para.tags:
    if tag=="NN" or tag=="NNS":
        noun.add(word)
    
    
print(noun)

mainString=""

for n in noun:
    mainString= n+","+mainString

print("The Main Words are: ", mainString)


theSent= para.sentences
title= theSent[0]
print(title)

theLen = len(para.sentences)

print("summary of "+str(title))

print("------------------------------")


print(theSent[1])
print(theSent[theLen-1])

