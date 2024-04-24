class solution:
    def isanagram(self,s:str,t:str)->bool:
        if len(s)!=len(t):
            return False
        char_count_s=[0]*26
        char_count_t=[0]*26
        for char in s:
            char_count_s[ord(char)-ord('a')]+=1
            for char in t:
                char_count_t[ord(char)-ord('a')]-=1
                return char_count_s==char_count_t
