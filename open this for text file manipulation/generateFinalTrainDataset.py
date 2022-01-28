import os
import csv

list = []

# This is the path where all the files are stored.

folder_path = "C:\\Users\\Ayan Deep Hazra\\Desktop\\Repos\\Natural_Language_Processing_Research\\open this for text file " \
              "manipulation\\labeled_papers_in_txt(w_crystals).csv"

# try multiple encodings if one fails
file = open(folder_path, encoding="cp1252")
csvreader = csv.reader(file)
posRows = []
negRows = []

for row in csvreader:
    if row[1]== "entailment":
        posRows.append(row[0])
    if row[1] == "contradiction":
        negRows.append(row[0])

i = 0
j = 0

for sentence in posRows:
    f2 = open("C:\\Users\\Ayan Deep Hazra\\PycharmProjects\\pythonProject1\\open this for text file " \
              "manipulation\\crystal_trainset\\positive\\FILE" + str(i) + ".txt", "w+", encoding="utf-8-sig")
    i = i + 1
    f2.write(sentence)
    f2.close()

for sentence in negRows:
    f2 = open("C:\\Users\\Ayan Deep Hazra\\PycharmProjects\\pythonProject1\\open this for text file " \
              "manipulation\\crystal_trainset\\negative\\FILE" + str(j) + ".txt", "w+", encoding="utf-8-sig")
    j = j + 1
    f2.write(sentence)
    f2.close()
