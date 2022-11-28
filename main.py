from nltk.tokenize import RegexpTokenizer
import xml.etree.ElementTree as et

file=open('input.txt','r')

text=file.read()

tokenize = RegexpTokenizer("[\w`'‘‘‘’‘-]+")
tokens = tokenize.tokenize(text.lower())
#print(type(tokens))
tree=et.parse('word.xml')

root=tree.getroot()
a=[]

for token in tokens:
    a.append({'word': str(token), "pos": "null", "root": "null"})
#print(a)

for i in range(len(a)):

    for dic in root:

        s=dic.text
        if((dic.attrib["classId"]=="fel") and ("moq" in s[-3:])):
            s=str(dic.text[:-3])

        l=len(s)

        if(s == a[i]["word"][:l]) :
            if (a[i]['root'] == "null"):
                a[i]["pos"] = str(dic.attrib["classId"])
                a[i]["root"] = s
            elif (l > len(a[i]["root"])):
                a[i]["pos"] = str(dic.attrib["classId"])
                a[i]["root"] = s
print(a)


for x in a:
    print(x)