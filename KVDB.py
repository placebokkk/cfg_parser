#key-value database
class KVDB:
    def __init__(self):
        self.db = {}    #database
        self.keys = []    #all keys
    def addValue(self, k, v):
        if k not in self.keys:
            self.keys.append(k)
        if not self.db.has_key(k):
            self.db[k]=[]
        self.db[k].append(v)
        return 1

    def getValue(self, k):
        if not self.db.has_key(k):
            return None
        else:
            return self.db[k][0]


    def getAllValues(self, k):
        if not self.db.has_key(k):
            return []
        else:
            return self.db[k]

    def getKeyList(self):
        return self.keys

#use for debug
    def showData(self):
        for k in self.keys:
                print k,self.db[k]
        return 1
