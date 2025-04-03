The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"


Solution :
Create an array of length numRows with empty strings, initialise an array pointer and a flag to direct the flow 

The direction is set to True (going down) when the array pointer is pointing to index 0, append the current character to the index and move to next index (array pointer is incremented). Repeat the same till array pointer reaches the last index. 

At the last index set the direction to False (going up), append the current character to the index and move to previous index (array pointer is decremented). Repeat the same tiill array pointer is 0.

Repeat till there are no more characters in string s and then return ''.join(rows) which joins all the rows with empty space.