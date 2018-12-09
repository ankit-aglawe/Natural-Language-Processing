from textblob.classifiers import NaiveBayesClassifier
from os.path import isfile, join
import os, glob


C01= 'Bacterial Infections and Mycoses'                      
C02='Virus Diseases'                                        
C03='Parasitic Diseases'                                    
C04='Neoplasms'                                             
C05='Musculoskeletal Diseases'                              
C06='Digestive System Diseases'                             
C07='Stomatognathic Diseases'                               
C08='Respiratory Tract Diseases'                            
C09='Otorhinolaryngologic Diseases'                         
C10='Nervous System Diseases'                               

category =[]
trainData=[]


path = '/home/ai1/My_Files/NLP/Assignment 3'
f= glob.glob('/home/ai1/My_Files/NLP/Assignment 3/*/*')

for dirct in os.listdir(path):
    a= dirct
    for i in f:
        k = open(i).read().replace('\n','')
        tuple =k,a
        trainData.append(tuple)
        
    category.append(a)
    
    

print(category)

classifier = NaiveBayesClassifier(trainData)





