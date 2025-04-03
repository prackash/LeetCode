class Solution:
    def reverse(self, x:int)->int:
        sign = 1 if x>=0 else -1
        x= abs(x)
        reversed_x =0
        while x>0:
            reversed_x = reversed_x*10 + x%10
            x = x//10
        reversed_x = sign*reversed_x
        if reversed_x < -2**31 or reversed_x > 2**31-1:
            return 0
        return reversed_x
# Example usage
if __name__ == "__main__":
    solution = Solution()
    print(solution.reverse(123))  # Output: 321
    print(solution.reverse(-123))  # Output: -321
    print(solution.reverse(120))  # Output: 21
    print(solution.reverse(0))  # Output: 0
    print(solution.reverse(1534236469))  # Output: 0 (out of bounds)
