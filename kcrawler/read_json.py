import nltk
nltk.download('punkt')
from textblob import TextBlob as tb
import json
import math
import sys


class TfIdf:

    def __init__(self, corpusPath):
        self.cps = corpusPath
        self.corpus = ""
        self.content = ""

    def setup(self):
        for cp in self.cps:
            self.corpus = json.load(open(cp, 'r'))
            self.buildCorpus()

    def buildCorpus(self):
        for i in range(0, len(self.corpus)):
            self.content = '. '.join(self.corpus[i]['content'])
            self.content.replace('..', '.')

    def writeToFile(self):
        outfileName = "stop-words.txt"
        outFile = open(outfileName, 'w')
        outFile.write(self.content)
        outFile.write('\n')
        outFile.close()


corpusPath = ["response.json"]
t = TfIdf(corpusPath)
t.setup()
t.writeToFile()
