# CDE_MSE_Databases

## Premise

Accurate and comprehensive material databases extracted from research papers are critical for materials science and engineering but require significant human effort to develop. In this paper we present a simple method of extracting materials data from full texts of research papers suitable for quickly developing modest-sized databases. The method requires minimal to no coding, prior knowledge about the extracted property, or model training, and provides high recall and almost perfect precision in the resultant database. The method is fully automated except for one human-assisted step, which typically requires just a few hours of human labor. The method builds on top of natural language processing and large general language models but can work with almost any such model. The language models GPT-3/3.5, bart and DeBERTaV3 are evaluated here for comparison. We provide a detailed detailed analysis of the methods performance in extracting bulk modulus data, obtaining up to 90% precision at 96% recall, depending on the amount of human effort involved. We then demonstrate the methods broader effectiveness by developing a database of critical cooling rates for metallic glasses.

Find paper at https://arxiv.org/abs/2302.04914

## How to Run

### 1
Git pull PaperDownload Directory
### 2
Run get_papers_1.py to get xml papers, change directory within py file 
### 3
Run process_xml_2.sh and process_xml_3.sh
### 4
Run prepare_property.sh for completion
