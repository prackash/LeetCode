class Solution:
    def convert(self, s: str, numRows: int) -> str:
        row, direc = 0,False
        if numRows==1 or numRows>=len(s):
            return s
        rows=['']*numRows

        for char in s:
            rows[row]+=char
            if row == 0:
                direc = True
            elif row == numRows-1:
                direc=False
            row+=1 if direc else -1
        return ''.join(rows)        
# Example usage
if __name__ == "__main__":
    solution = Solution()
    s = "PAYPALISHIRING"
    numRows = 3
    result = solution.convert(s, numRows)
    print(result)  # Output: "PAHNAPLSIIGY"
