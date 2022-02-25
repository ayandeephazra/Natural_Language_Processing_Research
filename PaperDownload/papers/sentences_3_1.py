import re
import glob

letters= "([A-Za-z])"
digits   = "(0|1|2|3|4|5|6|7|8|9)"
prefixes = "(Mr|St|Mrs|Ms|Dr|Prof|Capt|Cpt|Lt|Mt|Ref|Refs|Fig|etc|al|No|Figs|wt|no|Nos|nos|Eq|Eqs|vs|cf|Calc|equiv|aq|ca|Govt|diam|meq|sp|max|Coop|resp|eq|eqs|Ω|min|Hz|gb|et|nr|mol|el|dia|viz|NO|eg)[.]"
suffixes = "(Inc|Ltd|Jr|Sr|Co)"
starters = "(Mr|Mrs|Ms|Dr|Prof|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
websites = "[.](com|net|org|io|gov|me|edu|kh-1)"


def split_into_sentences(text):
    text = " " + text + "  "
    text = text.replace("\n"," ")
    text = text.replace("−","-")
    text = re.sub(prefixes,"\\1<prd>",text)
    text = re.sub(websites,"<prd>\\1",text)
    if "Ph.D" in text: text = text.replace("Ph.D.","Ph<prd>D<prd>")
    text = re.sub("(\])[.]( [a-z])","\\1\\2", text)
    text = re.sub("\s" + letters + "[.] "," \\1<prd> ",text)
    text = re.sub(acronyms +" "+ starters,"\\1<stop> \\2",text)
    text = re.sub(letters + "[.]" + letters + "[.]" + letters + "[.]","\\1<prd>\\2<prd>\\3<prd>",text)
    text = re.sub(letters + "[.]" + letters + "[.]","\\1<prd>\\2<prd>",text)
    text = re.sub(letters + "[.]" + letters,"\\1<prd>\\2<prd>",text)
    text = re.sub(digits + "[.]" + letters,"\\1<prd>\\2<prd>",text)
    text = re.sub(letters + "[.]" + digits,"\\1<prd>\\2<prd>",text)
    text = re.sub(" "+ suffixes +"[.] "+ starters," \\1<stop> \\2",text)
    text = re.sub(" "+ suffixes +"[.]"," \\1<prd>",text)
    text = re.sub(" " + letters + "[.]"," \\1<prd>",text)
    text = re.sub(digits + "[.]" + digits,"\\1<prd>\\2",text)
    text = re.sub(digits + "[.]" + digits + "[.]" + digits ,"\\1<prd>\\2<prd>\\3",text)
    if "”" in text: text = text.replace(".”","”.")
    if "\"" in text: text = text.replace(".\"","\".")
    if "!" in text: text = text.replace("!\"","\"!")
    if "?" in text: text = text.replace("?\"","\"?")
    if "..." in text: text = text.replace("...","<prd><prd><prd>")
    if "..." in text: text = text.replace("..","<prd><prd>")
    text = text.replace(".",".<stop>")
    text = text.replace("?","?<stop>")
    text = text.replace("!","!<stop>")
    text = text.replace("<prd>",".")
    sentences = text.split("<stop>")
    sentences = sentences[:-1]
    sentences = [s.strip() for s in sentences]
    return sentences


mylist = [f for f in glob.glob("clean/10*")]
for i in mylist:
    print(i)
    with open(str(i)) as f:
        lines = f.readlines()
    f.close()
    #print(lines[0])
    splitted=split_into_sentences(lines[0])
    with open('splitted/'+str(i).replace('clean/',''), mode='wt', encoding='utf-8') as myfile:
        myfile.write('\n'.join(splitted))
    myfile.close
