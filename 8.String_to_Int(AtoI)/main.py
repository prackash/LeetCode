class Solution:
    def myAtoi(self, s: str) -> int:
        num=0
        sign=1
        index=0
        result=0
        stri=s.lstrip()
        length=len(stri)
        # print(length)
        if length ==0:
            return 0
        # while s[index] == " ":
        #     index+=1

        if stri[index]=="-":
            sign =-1
            index+=1
        elif stri[index]=="+":
            index+=1
        
        # print(index)
        while index<length and stri[index].isdigit():
            digit = ord(stri[index])-ord('0')
            result= result*10 + digit
            # print(result)
            index+=1
            # print(index)
        result=sign*result
        if result < -2**31:
            return -2**31
        if result > 2**31 -1:
            return 2**31 -1
        return result
        
# Test cases
s = Solution()
# print(s.myAtoi("42"))           # Expected output: 42
print(s.myAtoi("   -042"))      # Expected output: -42
# print(s.myAtoi("4193 with words"))  # Expected output: 4193
# print(s.myAtoi("words and 987")) # Expected output: 0
# print(s.myAtoi("-91283472332")) # Expected output: -2147483648