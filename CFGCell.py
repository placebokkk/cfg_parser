class CFGCell:
    def __init__(self, symbol, cellList):
        self.symbol = symbol
        self.children = cellList

    def getChildren(self):
        return self.children

    def getOnlyChildren(self):
        return self.children[0]

    def getSymbol(self):
        return self.symbol

    def isIncompleted(self):
#print self.symbol.split(' '),len(self.symbol.split(' '))
        return len(self.symbol.split(' '))>1
