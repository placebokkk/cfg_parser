#!/usr/bin/python
from CFGParser import CFGParser
from Grammar import CFGGrammar
import sys
import time
CFGGrammarFile = "CFG.data"
senFile = "sentence.data"

fin = open(senFile,'r')
cfgGrammar = CFGGrammar(CFGGrammarFile)
parser = CFGParser(cfgGrammar)
start_t = time.clock()
for sen in fin:
    sen=sen[:-1]
    cell=parser.doParse(sen)
#parser.printTree(cell)
    print sen;
    parser.prettyPrintTree(cell)

end_t = time.clock()
print 'use time:',(end_t - start_t),'second.'
