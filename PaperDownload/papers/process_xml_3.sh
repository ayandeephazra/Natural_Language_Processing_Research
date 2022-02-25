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
    for element in root.iterfind('.//{http://www.elsevier.com/xml/common/dtd}para'):
        for ele in element.findall('.//{http://www.elsevier.com/xml/common/dtd}display'):
            parent=ele.getparent()
            parent.remove(ele)
        ElementTree.dump(element)" >> tmp_xml_convert.py

for i in 10*
do
	echo $(python3 -c "import tmp_xml_convert as sf; sf.get_text_from_file('${i}')" | awk '{gsub(/<[^>]*>/,"")};1') | tr '\n' ' ' | sed 's/\s\s*/ /g' > clean/$i
	echo $i
done

rm tmp_xml_convert.py