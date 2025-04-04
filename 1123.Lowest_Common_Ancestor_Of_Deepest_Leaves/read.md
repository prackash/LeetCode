if there is no root return None

calculate the depth of the left subtree
calculate the depth of the right subtree
if both depths are equal then that is the Lowest common ancestor
if left depth is greater then move the root to the left child else move the root to the right child
return a recursive call of the function used on the root

the function stops when either it reaches the common ancestor or the deepest leaf node