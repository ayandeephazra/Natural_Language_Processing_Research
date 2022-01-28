# Open one of the files,
list = []
import os
# This is the path where all the files are stored.
folder_path = 'C:\\Users\\Ayan Deep Hazra\\Desktop\\Repos\\Natural_Language_Processing_Research\\open this for text file manipulation\\files'
for data_file in sorted(os.listdir(folder_path)):
    print(data_file)
    list.append(data_file)

i = 0
for j in range(len(list)):
    f = open("C:\\Users\\Ayan Deep Hazra\\Desktop\\Repos\\Natural_Language_Processing_Research\\open this for text file manipulation\\files\\"+str(list[j]), "r", encoding="utf-8")

    content = f.read()

    f.close()
    content_list = content.split(".\n")

    for sentence in content_list:
        f2 = open("FILE" + str(i) + ".txt", "w+", encoding="utf-8")
        i = i + 1
        f2.write(sentence)
        f2.close()

