Need to use two variable to act as pointers ,a data structure to hold the frequency, and a variable to hold the length.

# Solution 1: Set

1. Use a chatSet (set) as the datastructure to track unique characters in the current substring.
2. Iterate though the string using the 2nd pointer.
3. The character on the 2nd pointer is not in the set, then it is a new character.
4. Add the character to the set and update the length by checking the maximum between the previous value and the difference between pointer index +1.
5. If the character is already in the set, then repeating character, move the 1st pointer forward, removing character till no repeat character. eg set (abirkgp) and current character is r then remove abir from set.
6. Insert current character and repeat 3 to 5 till end, finally return the length.

# Solution 2: Map

1. Use a unordered map (charMap) instead of set.
2. Iterate though the string using the 2nd pointer.
3. If the current character is not in the map or its index is less than the 1st, it means it is a new character.
4. Update the charMap with the character index and update the length.
5. If the character is repeating then move the 1st pointer to the next position after the last occurence of the character. eg  string abirkgprei till p the charMap will be 
a 0
b 1
i 2
r 3
k 4
g 5
p 6
Once it checks for a it notices that the count is 1 and that it is not less than the 1st pointer (i.e) 0 in this case.
Now 1st pointer is charMap[s[right]]+1 in  this case it is 3+1 so it will become 4
r will be replaced by 7
6. repeat till end
when it checks the last character i it is a repeating character but not in the current window after index 7 this is checked by charMap[s[right]] < left. Here it will check if 2 < 4.
final set 
a 0
b 1
i 9
r 7
k 4
g 5
p 6
e 8

left = 4, right = 8, length = 5

### Solution 3: IntArr

1. Use charIndex to store the indices of characters, initialised with -1
2. Iterate throught 2nd pointer
3. check current character present by comparing index in charIndex with 1st pointer if it is greater than 1st pointer, then it is repeating char update 1st pointer to the index next to the current character.
4. Set the value in charIndex as index
5. calculate length
