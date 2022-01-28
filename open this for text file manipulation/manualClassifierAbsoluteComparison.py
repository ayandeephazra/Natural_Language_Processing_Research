import csv

positives = 0
negatives = 0
i = 1
tn = 0
tp = 0
fn = 0
fp = 0
flag = 0
flag2 = 0
totalRawCount = 0
flag5 = 0
linelist = []

#################################################################################################################
#################################################################################################################
#################################################################################################################

folder_path = "C:\\Users\\Ayan Deep Hazra\\Desktop\\Repos\\Natural_Language_Processing_Research\\open this for text file " \
              "manipulation\\filtered_test_scibert.csv"
csvfile = open(folder_path, encoding="utf-8")
csvreader = csv.reader(csvfile)
rows = []
truelabel = []

for row in csvreader:
    rows.append(row[0])

for row in csvreader:
    truelabel.append(row[1])

#################################################################################################################
#################################################################################################################
#################################################################################################################
rowcount = -1
filecount = -1
with open("file4.txt", "r", encoding="utf-8") as file:
    for line in file:
        filecount = filecount + 1
        rowcount = -1
        words = line.split()
        if len(words) == 0:
            continue
        for row in rows:
            rowcount = rowcount + 1
            print("halliday", rowcount, filecount, len(words))
            print(words[0], "hh", row, "HHHHH", " ".join(words[1:len(words) - 3]))
            if len(words) > 0 and words[0] == "input:":
                if (" ".join(words[1:len(words) - 3])).strip() == row:
                    print("resnick 8888888888888888888888888888888888888888888888888888888888888888")
                    if float(words[len(words) - 1]) > 0.5:
                        if truelabel[rowcount] == "entailment":
                            tp = tp + 1
                        else:
                            fp = fp + 1
                    else:
                        if truelabel[rowcount] == "entailment":
                            fn = fn + 1
                        else:
                            tn = tn + 1
                    break
            else:
                continue

print(positives)
print(negatives)
# fp = positives - tp
# tn = negatives - fn
print("tn:", tn)
print("tp:", tp)
print("fp:", fp)
print("fn:", fn)

recall = tp / (tp + fn)
precision = tp / (tp + fp)

print("recall: ", recall)
print("precision: ", precision)
print("F score:", 2 * precision * recall / (precision + recall))
print(totalRawCount)
