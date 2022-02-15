import requests as r
import json
import xml.dom.minidom
import lxml.etree as etree

key = "af51ce170274fce0cc09ce679d40ea04"
url = "https://api.elsevier.com/content/search/sciencedirect"

params_download = (
    ('APIKey', key),
)
headers_search = {"x-els-apikey": key,
                  "Content-Type": "application/json",
                  "Accept": "application/json"}

data = {
    "qs": "\"band gap\""
}

a = r.put(url, json=data, headers=headers_search)
a = a.json()
print(a)
n_papers = a["resultsFound"]

for chunk in range(0, n_papers, 100):
    print("Downloading papers: " + str(chunk) + "/" + str(n_papers))
    data = {
        "qs": "\"area specific resistance\"",
        "display": {
            "offset": chunk,
            "show": 100
        }
    }
    a = r.put(url, json=data, headers=headers_search)
    # print(a)
    a = a.json()

    for j in a["results"]:
        # print(j["doi"])
        paper = r.get('https://api.elsevier.com/content/article/doi/' + j["doi"] + "?", params=params_download)
        paper = paper.text
        with open("papers/" + j["doi"].replace('/', 'SL').replace('(', 'LP').replace(')', 'RP'), "w",
                  encoding="utf8") as text_file:
            text_file.write(paper)
