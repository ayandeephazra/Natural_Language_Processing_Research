from lxml import etree
from xml.etree import ElementTree


def get_text_from_file(xml_file):
    tree = etree.parse(xml_file)
    root = tree.getroot()
    for element in root.iterfind('.//para'):
        for ele in element.findall('.//display'):
            parent = ele.getparent()
            parent.remove(ele)
        ElementTree.dump(element)
