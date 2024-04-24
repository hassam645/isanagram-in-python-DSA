class solution:
    def isanagram(self,s:str,t:str)->bool:
        if len(s)!=len(t):
            return False
        x=set(s)
        for i in x:
            s.count(s)==s.count(t)
            return False
        return True