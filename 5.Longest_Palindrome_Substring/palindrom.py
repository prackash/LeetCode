class Solution:
    def Palindrome(sellf, s:str)-> str:
        length = 0
        palin= s[0]
        while length<len(s):
            till = len(s)-1
            while till>length:
                if s[till]==s[length]:
                    temp = s[length:till+1]
                    if temp==temp[::-1]:
                        if len(temp)>len(palin):
                            palin = temp
                till-=1
            length+=1
        return palin

if __name__ == "__main__":
    s = Solution()
    print(s.Palindrome("babad"))
    