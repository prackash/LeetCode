
A string x is a suffix of a string y if and only if x is a substring of y that starts from some index (including 0) in y and extends to the index y.length - 1. For example, 25 is a suffix of 5125 whereas 512 is not.

Example 2:

Input: start = 15, finish = 215, limit = 6, s = "10"
Output: 2
Explanation: The powerful integers in the range [15..215] are 110 and 210. All these integers have each digit <= 6, and "10" as a suffix.
It can be shown that there are only 2 powerful integers in this range.
Example 3:

Input: start = 1000, finish = 2000, limit = 4, s = "3000"
Output: 0
Explanation: All integers in the range [1000..2000] are smaller than 3000, hence "3000" cannot be a suffix of any integer in this range.
 
Logic:

Convert the integer from base 10 to base limit, essentially if the digit is above limit change it to limit and all the following numbers to limit

for example consider integer 2583 and limit 7, the integer will be converted to 2577

2583(10) == 2577(7)

Now count from the power full numbers from 0 till the converted integer

let the suffix be 23, ans be 0 and base be limit+1
since the suffix is of length 2 remove the right most 2 digits from the integer {25}

for each digit of the integer from the left 
ans is the sum of the product of ans and base and the digit value {ans=ans*base + int(n)}
ans = 0*8 +2 = 2
ans = 2*8 + 5 = 16+5=21

if the prefix of the int appended with the suffix is lesser than the converted integer increment the answer by one.
{"25"+"23" < 2577}
ans=ans+1 = 22

now calculate the same for the end integer and the return the difference of the two

