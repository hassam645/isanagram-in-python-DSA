class solution:
    def isanagram(self,s:str,t:str)->bool:
        ss=sorted(s)
        tt=sorted(t)
        return ss==tt