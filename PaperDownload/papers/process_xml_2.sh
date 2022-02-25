#!/bin/bash

if [ ! -e clean ]
then
  mkdir clean
fi

echo "from lxml import etree
from xml.etree import ElementTree

def get_text_from_file(xml_file):
    tree=etree.parse(xml_file)
    root=tree.getroot()
    for element in root.iterfind('.//para'):
        for ele in element.findall('.//display'):
            parent=ele.getparent()
            parent.remove(ele)
        ElementTree.dump(element)" >> tmp_xml_convert.py

for i in 10*
do
	new=$(echo $i | sed "s/^/\'/" | sed "s/$/\'/")
	new=\'${i}\'
	echo $(python3 -c "import tmp_xml_convert as sf; sf.get_text_from_file($new)" | awk '{gsub(/<[^>]*>/,"")};1') | tr '\n' ' ' | sed 's/\s\s*/ /g' > clean/$i
	echo $i
done

rm tmp_xml_convert.py
