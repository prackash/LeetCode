Since the arrays are already sorted we can make use of that to reduce the time complexity

Using binary search we can proceed

1. We use the smaller array to calculate the middle index for both 
2. Calculate the number of elements present to the left of the partition
3. Set the two pointers low to 0 and high to the size of array
4. calculate the middle index of the 1st array (smallest array) low+high //2
5. Calculate the middle index of the 2nd array using midindex1 left +mid1 //2
6. Retrieve the values for 4 values l1,l2,r1,r2 where l1,l2 are the number to prior to the middle value r1,r2 are the middle values of the arrays
7. If l1 <= r2 and r1>=l2 then return max of l1 and l2 if the total array size is even else return the sum of max of l1 l2 and min of r1 r2 / 2
