# Open one of the files,
list = []
import os

# This is the path where all the files are stored.
folder_path = 'C:\\Users\\Ayan Deep Hazra\\PycharmProjects\\pythonProject1\\files'
for data_file in sorted(os.listdir(folder_path)):
    print(data_file)
    list.append(data_file)

for i in range(len(list)):
    f = open("files/" + str(list[i]), "r", encoding="utf-8")

    content = f.read()
    if content.find('hardness') != -1:
        print(content, list[i])
