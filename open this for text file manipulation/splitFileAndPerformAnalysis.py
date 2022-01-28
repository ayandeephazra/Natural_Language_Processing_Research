# f = open("file.txt", "r", encoding="utf-8")

# content = f.readLines()

# f.close()
# content_list = content.split(". ")

# i = 0
# for sentence in content:
#   print("i", sentence)
# //f2 = open("FILE" + str(i) + ".txt", "w+", encoding="utf-8")
# / i = i + 1
# f2.write(sentence)
# f2.close()
# print(content_list)
#             file = open(folder_path, encoding="cp1252")
 #               csvreader = csv.reader(file)

import csv

i = 0

folder_path = "C:\\Users\\Ayan Deep Hazra\\Desktop\\Repos\\Natural_Language_Processing_Research\\open this for text file " \
              "manipulation\\labeled_papers_in_txt(w_crystals).csv"

# try multiple encodings if one fails
file = open(folder_path, encoding="cp1252")
csvreader = csv.reader(file)
rows = []
statuses = []

for row in csvreader:
    rows.append(row[0])
    statuses.append(row[1])
i = 0

i = 0
tn = 0
tp = 0
fn = 0
fp = 0
total = 0
with open("file.txt", "r", encoding="utf-8") as file:
    for line in file:

        j = 0
        #print(line)
        words = line.split()
        if len(words) > 0:
            if words[0] == "input:":
                total = total + 1
               # print(words[1])
                # print(" ".join(words[1:len(words)-3]))
                string = " ".join(words[1:len(words) - 3])
                #print(string)
                i = i + 1
                # print(i)
                # for (row, status) in zip(rows, statuses):
                for t in range(len(rows)):
                    # print(row[0], len(row[0]))
                    j = j + 1
                    print("string", string)
                    print("row", rows[t])
                    if string.strip() == rows[t].strip():
                        if statuses[t] == "entailment":
                            if float(words[len(words) - 1]) < 0.5:
                                tn = tn + 1

                            else:
                                tp = tp + 1
                        else:
                            print(float(words[len(words) - 1]))
                            if float(words[len(words) - 1]) < 0.5:
                                fp = fp + 1
                            else:
                                fn = fn + 1
                    else:
                        print("bsdk")
                    # rows.append(row[0])




print("tn:", tn)
print("tp:", tp)
print("fp:", fp)
print("fn:", fn)
print(total)
