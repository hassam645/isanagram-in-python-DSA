class solution:
    def isanagram(self,s:str,t:str)->bool:
        if len(s)!=len(t):
            return False
        hashmap={}
        for char in s:
            hashmap[char]=hashmap.get(char,0)+1
            for char in t:
                if char  is not hashmap or hashmap[char]==0:
                    return False
                else:
                    hashmap[char]-=1
                    return True