2->4->3 represents 342


example: assume 342 + 465
it will be represented as 2->4->3 + 5->6->4

The linked lists can be of different lengths anywhere from 1 to 100

## Solution 

1. Create a dummy Linked list
2. Create a pointer for the Linked list and initialise carry as 0
3. loop until there are elements in l1, l2, or if carry is not 0
4. Add the values in the linked lists with the carry
5. Append the unit digit value of sum to the dummy linked list and the remaining value to carry


