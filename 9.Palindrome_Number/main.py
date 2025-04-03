class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        if x//10==0:
            return True
        if x%10 == 0:
            return False
        temp=x
        reverse=0
        while temp>0:
            digit=temp%10
            reverse=reverse*10 +digit
            temp=temp//10
        if reverse==x:
            return True
        return False
        
if __name__ == "__main__":
    x = 121
    print(Solution().isPalindrome(x))
    x = -121
    print(Solution().isPalindrome(x))
    x = 10
    print(Solution().isPalindrome(x))
    x = 12321
    print(Solution().isPalindrome(x))
    x = 123321
    print(Solution().isPalindrome(x))
    x = 123456
    print(Solution().isPalindrome(x))