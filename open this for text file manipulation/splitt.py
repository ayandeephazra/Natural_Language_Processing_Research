f = open("First principles investigation of structural, elastic, electronic and optical properties of HgGeB2 (Bdouble bondP, As) chalcopyrite semiconductors.txt", "r", encoding="utf-8")

content = f.read()

f.close()
content_list = content.split(". ")

i = 0
for sentence in content_list:
    f2 = open("FILE" + str(i) + ".txt", "w+", encoding="utf-8")
    i = i + 1
    f2.write(sentence)
    f2.close()
print(content_list)