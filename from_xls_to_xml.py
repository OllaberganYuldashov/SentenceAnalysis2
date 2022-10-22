import pandas as pd
import xml.etree.cElementTree as et

excel_data = pd.read_excel('word.xlsx')

data = pd.DataFrame(excel_data, columns=['Id', 'word', 'property'])

root=et.Element("dictionary")

l=len(data)
for i in range(l):
    if '*' in data['word'][i]:
        et.SubElement(root,"word", classId='1', id=str(data['Id'][i]), changeClass="*",
                      property=str(data['property'][i])).text=str(data['word'][i])[:-1]
    else:
        et.SubElement(root, "word", classId='1', id=str(data['Id'][i]), changeClass="",
                      property=str(data['property'][i])).text = str(data['word'][i])
tree = et.ElementTree(root)
tree.write("word.xml", xml_declaration=True, encoding='utf-8')
