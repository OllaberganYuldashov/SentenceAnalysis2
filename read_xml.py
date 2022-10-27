import xml.etree.cElementTree as et

tree=et.parse('word.xml')

root=tree.getroot()

ravish=root.findall('word')

for w in root:

    print(w.attrib["id"],'\t',w.text,'\t',w.attrib["classId"] )