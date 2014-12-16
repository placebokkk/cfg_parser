from Structure import Matrix
from CFGCell import CFGCell
class CFGParser:
    def __init__(self, grammar):
        self.gr = grammar
        
    def doParse(self, sentence):
        tokens = sentence.split(' ')
        ftokens = filter((lambda t: t.strip()!=''),tokens)
        return self.parseTokens(ftokens)

    def fillUnaryRule(self, chartNode, cell):
        rhs = cell.getSymbol()
        for lhs in self.gr.getAllCom(rhs):
#print 'unary '+lhs+'->'+rhs
            clist = []
            clist.append(cell)
            fCell = CFGCell(lhs, clist )
            chartNode.append(fCell)
            self.fillUnaryRule(chartNode, fCell)

    def pretty(self, pT, i, depth):
        string = ''
        #print pT.getSymbol()
        ind =''
        for j in range(0,depth):
            ind +=i
        if pT.getChildren()==None:
            string = pT.getSymbol()
        else:
            clist = pT.getChildren()
            if len(clist)==1:
                string = '\n'+ind+'('+pT.getSymbol()  +' '+ self.pretty(clist[0],i,depth+1)+')'
            else:
                string = '\n'+ind+'('+pT.getSymbol()
                for cell in clist[:-1]:
                    string += ' '+self.pretty(cell,i,depth+1) 
                string += self.pretty(clist[len(clist)-1],i,depth+1)+')'
        #print str
        return string
         
    def prettyPrintTree(self, pT):
        if pT == None:
            print 'can\'t parse!!!'
        else:
            print self.pretty(pT, '    ', 0)



    def parseTokens(self, tokens):
        m = len(tokens)
        n = m+1
        chart = Matrix(m, n)
        gr = self.gr
        #print "Terminal:";
        for j in range(1,n):
#            print 'j',j
            #for name in gr.getTerFather(tokens[j-1]):
                #print name;
            tCell = CFGCell(tokens[j-1], None)
            chart[j-1][j].append(tCell)
            tlist = []
            tlist.append(tCell)
            for f in gr.getTerFather(tokens[j-1]):
                fCell = CFGCell(f, tlist)
                chart[j-1][j].append(fCell)
                self.fillUnaryRule(chart[j-1][j], fCell) 
#debug
#            for x in chart[j-1][j]:
#                print j-1,j,x.getSymbol()
#debug
            for i in range(j-2, -1, -1):
#                print 'i',i
                for k in range(i+1, j):
#                    print 'k',k
                    B = chart[i][k]
                    C = chart[k][j]
                    if len(B)== 0 or len(C)==0:
                        pass
                    else:
                        for b in B:
                            if gr.isExistedIncompleted(b.getSymbol()):
                                for c in C:
                                    if not c.isIncompleted():
                                        children = b.getChildren()[:]
                                        children.append(c)
                                        cname = b.getSymbol()+' '+c.getSymbol()
                                        for father in gr.getAllCom(cname):
                                            fCell = CFGCell(father,children )
                                            chart[i][j].append(fCell)
                                            self.pDEBUG(i,j,father,children)
                                            self.fillUnaryRule(chart[i][j], fCell) 
                                        if gr.isExistedIncompleted(cname):
                                            chart[i][j].append(CFGCell(cname,children ))
                                            self.pDEBUG(i,j,cname,children)
                            elif not b.isIncompleted():
                                for c in C:
                                    if not c.isIncompleted():
                                       #Completed Rule
                                        cname = b.getSymbol()+' '+c.getSymbol()
                                        children = [b,c]
                                        for father in gr.getAllCom(b.getSymbol()+' '+c.getSymbol()):
                                            fCell = CFGCell(father,children )
                                            chart[i][j].append(fCell)
                                            self.pDEBUG(i,j,father,children)
                                            self.fillUnaryRule(chart[i][j], fCell) 
                                        if gr.isExistedIncompleted(cname):
                                            fCell = CFGCell(cname,children )
                                            chart[i][j].append(fCell)
                                            self.pDEBUG(i,j,cname,children)
                                            self.fillUnaryRule(chart[i][j], fCell) 

                                
        for cell in chart[0][m]:
            if cell.getSymbol() == 'S':
                return cell
        return None
    
    def pDEBUG(self,i,j,father,children):
#        print 'append father ',i,j,father
#        print 'children';
#        for c in children:
#            print c.getSymbol()
        return 0
