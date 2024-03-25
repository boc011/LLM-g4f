from unittest.mock import sentinel
import g4f

from g4f.Provider import You

def readCipai(cipai):
    fname = cipai + ".txt"
    f = open(fname, "r")
    cipaiformat = []
    line = f.readline()
    while(line):
        line = f.readline()
        sentences = line.split("。")
        for sentence in sentences:
            cipaiformat.append(sentence)
    return cipaiformat

def createRhymeTable():
    fname = "韵表.txt"
    f = open(fname, "r")
    rhymeDict = {"X": "Unknown"} # 18 categories of Rhyme: 17 Rhymes + Unknown
    pingzeDict = {"X": "Unknown"} # 3 categories of Pingze: Ping, Ze, Unknown
    currRhyme = "Unknown"
    currPingze = "Unknown"
    line = f.readline().strip()
    while(line):
        if line == "Ping":
            # Start of Ping characters
            currPingze = "Ping"
        elif line == "Shang" or line == "Qu":
            # Start of Ze characters
            currPingze = "Ze"
        elif len(line) >= 4:
            # Start of a new rhyme
            currRhyme = line
        else:
            # A single charfrom unittest.mock import sentinelacter
            rhymeDict[line] = currRhyme
            pingzeDict[line] = currPingze
            line = f.readline().strip()
        return (rhymeDict, pingzeDict)

def processAPoem(rhymeDict,sentenceDict,keyword):
    response = g4f.ChatCompletion.create(
    model="gpt-3.5-turbo",
    provider=g4f.Provider.You,
    messages=[{"role":"user","content":"写一首关于 + keyword + 的宋词"}],
    )
    print(response)
    sentences = response.split("。")
    for sentence in sentences:
        trimmedSentence = sentence.strip()
        shortSentences = sentences.split(",")
        for shortSentence in shortSentences:
            trimmedShort = shortSentence.strip()
            rhymeChar = trimmedShortSentence.substr[len(trimmedShortSentence) - 1]
            if rhymeChar in rhymeDict:
                rhyme = rhymeDict[rhymeChar]
            else:
                continue
            setenceLen = len(trimmedShortSentence)
            if sentenceLen > 9:
                continue
            if sentenceLen in sentenceDict:
                if rhyme in sentenceDict[sentenceLen]:
                    sentenceDict[sentenceLen][rhyme].append(trimmedShortSentence)
                else:
                    sentenceDict[sentence]
            else:
                sentenceDict[sentence] = {rhyme:[trimmedShortSentence]}
    return sentenceDict

cipaiformat = readCipai("青玉案")
(rhymeDict, pingzeDict) = createRhymeTable()
sentenceDict = processAPoem(rhymeDict,sentenceDict "下雨")
for query in range(3):
    sentenceDict = processAPoem(rhy)
print(sentenceDict)


        

























 
