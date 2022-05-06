import re


def performCapitalization(data):
    data.capitalize()
    return data

# hello : 2
# world : 1
def getSummary(data):
    mapTemp = {}
    for line in data:
        splitString = line.split()
        res = re.findall(r'\w+', str(splitString))
        for word in res:
            word = word.lower()
            if word in mapTemp:
                mapTemp[word] = mapTemp[word] + 1
            else:
                mapTemp.update({word: 1})
    return mapTemp
