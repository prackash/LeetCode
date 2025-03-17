### Naive approach
Every palindrome needs to have their edge characters equal
Steps:
- check start index and the end index of the string if they are equal 
- If yes check if the substring from the start index to the end index is a palindrome, if the length of the current palindrome is greater then store it 
- If the edges are not equal than reduce the end index by 1
- repeat 1 to 3 till end index is no longer greater than the start index. Increase the start index by 1 and repeat untill start index is equal to the length of the string.

return the palindrome length stored


# Manacher Algorithm
Manacher Algorithm calculates the number of characters which are the same on the right and left of each position in the string, this is done as a preprocessing O(n) and stored in a string making it O(1) to check for each character

- Add special character # at the start, end and in between characters, this ensures that the string is always of odd length (i.e., there always a center) A n string will have n+1 # in it.
- Create an array P with length of the padded string, this will contain the length till which the character to the right are the same as the left
- if xabay in abaxabayabd is a palindrome then x is a palindrome of y therefore x shares the same length as y. This is used as optimisation for filling in P.
- Initialise center as 1 and right as 1. Center is the index of the first character and right is the edge of the substring
- iterate through the padded string from the 1st character 
- Calculate the mirror index of the character from the center of the substring(i.e. mirror = 2*center - index).
- if the index is within the limits of the substring then calculate the palin length as the minimum of the remaining length at the right of index till the edge of substring or the palin lenght at the mirror index (abaxabayabd).
- Now search beyond the substring if the characters are the same to the right as they are on left, if they are then increment the palinlength.
- if the sum of index and its palin length is greater than the end index of the substring that means there are more characters that can be added to the substring and still remain a palindrome, thus the center is set at the current index and the end index is moved to index + palinlength.
- The index with the largest palinlength value is the centre of the longest palidrome substring with length palinlength