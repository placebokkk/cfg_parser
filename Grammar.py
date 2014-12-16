from KVDB import KVDB
class CFGGrammar:
    def __init__(self, file):
        self.db = KVDB()   #Non-Terminal DB
        self.t_db = KVDB() #lexcial DB
        self.in_db = KVDB()
        self.readCFGFile(file)

    def addRule(self, key, value):
        self.db.addValue(key,value)
        return 1

    def getRule(self, key):
        return self.db.getValue(key)


    def getAllCom(self, key):
        return self.db.getAllValues(key)

    def getKeyList(self):
        return self.db.getKeyList()

    def addTerRule(self, word, lhs):
        self.t_db.addValue(word, lhs)
        return 1
 
    def getTerList(self):
        return self.t_db.getKeyList()
        
    def getTerFather(self, word):
        return self.t_db.getAllValues(word)

    def getIncomList(self):
        return self.in_db.getKeyList()
        
    def getAllIncom(self, inrhs):
        return self.in_db.getAllValues(inrhs)
         
         
    def addIncompletedRule(self, lhs, rhs):
        for l in range(len(rhs)-1, 1, -1):
            rlist = rhs[:l]
            right = ''
            for item in rlist[:-1]:
                right +=item+' '
            right +=rlist[len(rlist)-1]
            self.in_db.addValue(right, lhs)
        
    def isExistedIncompleted(self, name):
# print 'iei!!',name;
#       print self.getIncomList()
#       print (name in self.getIncomList())
        return (name in self.getIncomList())

    def readCFGFile(self,filename):
        cfgFile=open(filename)
        for lines in cfgFile:
            lines=lines[:-1]
            if not lines:
                continue
            rightlist = []
            tmp = lines.split('=')
        #    print tmp
            left = tmp[0].strip()
            right = tmp[1].strip()
            if right.find('|')!=-1:
                rightlist = map((lambda x:(x.strip())),right.split('|'))
                for ter in rightlist:
                    self.t_db.addValue(ter,left)
            else:
                self.db.addValue(right,left)
                rightlist = right.split(' ')
                if len(rightlist) > 2:
                    self.addIncompletedRule(left,rightlist)
                
        
        return 0



    def showGrammar(self):
        self.db.showData()
        self.t_db.showData()
        self.in_db.showData()
    

    
  
    

    
    
