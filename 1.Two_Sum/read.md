## Two Sum

### Problem Statement:

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

- 2 <= nums.length <= 104
- 109 <= nums[i] <= 109
- 109 <= target <= 109
- Only one valid answer exists.

### Solution 1: Brute Force 


This is the simplest solution and so it is also the least efficient with the time complexity of O(n^2), here we consider every pair of elements and check if the sum is equal to the target. 

Done using nested loops, the outer loop iterates through all but last element while the inner loop iterates from next element of the outer loop iteration to last.
1. Loop i from 0 to n-1
2. Loop j from i+1 to n
3. Check if num[i] + num[j] is equal to target if yes return the indeces. Repeat till Loops are completed
4. If no solution then return empty or None


### Solution 2:

This solution is done using a hashmap and has a time complexity of O(n) since lookups in hashmap are constant time.

1. Create an empty hashtable
2. Iterate through the array and store the elements and their indices in the hashtable.
3. Iterate once more and calculate the compliment of for each element in the array from the target.
4. If the complement exists and is not the same index as the element return the pair of indeces
5. If no solution exists after the iteration return empty array or None


Alternatively it can also be done in one iteration rather than two

1. Create an empty hashtable
2. Iterate through the array, calculate the complement of the element from the target, if the complement is in the map then return the index of the element and of the complement.
3. Else add the element to the map.
4. If no solution exists after the iteration return empty array or None

