import pandas as pd
import xml.etree.cElementTree as et

root=et.Element("dictionary")
id=0
#Sifat
excel_data = pd.read_excel('excel/sifat.xlsx')
data = pd.DataFrame(excel_data, columns=['word', 'property'])

l=len(data)
for i in range(l):
    id=id+1
    if '*' in data['word'][i]:
        et.SubElement(root,"word", classId='sifat', id=str(id), changeClass="*",
                      property=str(data['property'][i])).text=str(data['word'][i])[:-1]
    else:
        et.SubElement(root, "word", classId='sifat', id=str(id), changeClass="",
                      property=str(data['property'][i])).text = str(data['word'][i])


#Son
excel_data = pd.read_excel('excel/son.xlsx')
data = pd.DataFrame(excel_data, columns=['word', 'property'])
id=0
l=len(data)
for i in range(l):
    id=id+1
    if '*' in data['word'][i]:
        et.SubElement(root,"word", classId='son', id=str(id), changeClass="*",
                      property=str(data['property'][i])).text=str(data['word'][i])[:-1]
    else:
        et.SubElement(root, "word", classId='son', id=str(id), changeClass="",
                      property=str(data['property'][i])).text = str(data['word'][i])


#Fel
excel_data = pd.read_excel('excel/fel.xlsx')
data = pd.DataFrame(excel_data, columns=['word', 'property'])
id=0
l=len(data)
for i in range(l):
    id=id+1
    if '*' in data['word'][i]:
        et.SubElement(root,"word", classId='fel', id=str(id), changeClass="*",
                      property=str(data['property'][i])).text=str(data['word'][i])[:-1]
    else:
        et.SubElement(root, "word", classId='fel', id=str(id), changeClass="",
                      property=str(data['property'][i])).text = str(data['word'][i])



#Ravish
excel_data = pd.read_excel('excel/ravish.xlsx')
data = pd.DataFrame(excel_data, columns=['word', 'property'])
id=0
l=len(data)
for i in range(l):
    id=id+1
    if '*' in data['word'][i]:
        et.SubElement(root,"word", classId='ravish', id=str(id), changeClass="*",
                      property=str(data['property'][i])).text=str(data['word'][i])[:-1]
    else:
        et.SubElement(root, "word", classId='ravish', id=str(id), changeClass="",
                      property=str(data['property'][i])).text = str(data['word'][i])

#Ot
excel_data = pd.read_excel('excel/ot.xlsx')
data = pd.DataFrame(excel_data, columns=['word', 'property'])
id=0
l=len(data)
for i in range(l):
    id=id+1
    if '*' in data['word'][i]:
        et.SubElement(root,"word", classId='ot', id=str(id), changeClass="*",
                      property=str(data['property'][i])).text=str(data['word'][i])[:-1]
    else:
        et.SubElement(root, "word", classId='ot', id=str(id), changeClass="",
                      property=str(data['property'][i])).text = str(data['word'][i])

#Yordamchi so`zlar
excel_data = pd.read_excel('excel/yordamchi.xlsx')
data = pd.DataFrame(excel_data, columns=['word', 'property'])
id=0
l=len(data)
for i in range(l):
    id=id+1
    if '*' in data['word'][i]:
        et.SubElement(root,"word", classId='yordamchi soz', id=str(id), changeClass="*",
                      property=str(data['property'][i])).text=str(data['word'][i])[:-1]
    else:
        et.SubElement(root, "word", classId='yordamchi soz', id=str(id), changeClass="",
                      property=str(data['property'][i])).text = str(data['word'][i])

#Oraliq so`zlar
excel_data = pd.read_excel('excel/oraliq.xlsx')
data = pd.DataFrame(excel_data, columns=['word', 'property'])
id=0
l=len(data)
for i in range(l):
    id=id+1
    if '*' in data['word'][i]:
        et.SubElement(root,"word", classId='oraliq soz', id=str(id), changeClass="*",
                      property=str(data['property'][i])).text=str(data['word'][i])[:-1]
    else:
        et.SubElement(root, "word", classId='oraliq soz', id=str(id), changeClass="",
                      property=str(data['property'][i])).text = str(data['word'][i])

#faylga yozish
tree = et.ElementTree(root)
tree.write("word.xml", xml_declaration=True, encoding='utf-8')
