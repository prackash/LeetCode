class Solution:
    def addBoundaries(self, s:str)->str:
        if len(s)==0:
            return "##"
        s2 = "" 
        for i in range(len(s)):
            s2+="#"+s[i]
        s2+="#"
        return s2
    def removeBoundaries(self, s:str)->str:
        s2 = ""
        for i in range(len(s)):
            if s[i]!="#":
                s2+=s[i]
        return s2

    def longestPalindrome(self,s:str)->str:
        s2 = self.addBoundaries(s)
        maxlen=1
        maxpal=s[0]
        print(s2)
        p= [0]*len(s2)
        print(p)
        center = 0
        right = 0
        for i in range(len(s2)):
            # print(p)
            mirror = 2*center-i
            if right>i:
                p[i] = min(right-i,p[mirror])
            while i+(1+p[i])<len(s2) and i-(1+p[i])>=0 and s2[i+(1+p[i])]==s2[i-(1+p[i])] :
                p[i]+=1
            if i+p[i]>right:
                center = i
                right = i+p[i]
            if p[i]>maxlen:
                maxlen = p[i]
                maxpal = s2[i-p[i]:i+p[i]+1]
        return self.removeBoundaries(maxpal)



if __name__=="__main__":
    s = Solution()
    s2 = s.longestPalindrome("abqbababbbababaaaabaaaa")
    print(s2)