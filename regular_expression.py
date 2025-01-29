import re
def findwords(text):

    hastag = re.findall(r"#%w/+",text)
    mention = re.findall(r"@%w/+",text)
    return hastag,mention

text = "#huih uihfsui @hiagduweg #hfuus @urisdgy"

hastags,mention = findwords(text)
print(hastags)
print(mention)