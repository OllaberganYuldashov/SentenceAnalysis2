from nltk.tokenize import RegexpTokenizer
import xml.etree.cElementTree as et

file=open('input.txt','r')

text=file.read()

tokenize = RegexpTokenizer("[\w`'‘‘‘’‘-]+")
tokens = tokenize.tokenize(text.lower())





tree=et.parse('word.xml')

root=tree.getroot()

for token in tokens:
    for w in root:
        l=len(w.text)
        if w.text in token[:l]:
            print(token,'\t',w.text)




