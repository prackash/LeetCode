Logic 

calculate int max as the maximum integer nums[i] in the array so far in the loop 
using int max calculate diff_max as the difference between the maximum int in the loop and the current int, this stores the largest nums[i]-nums[j] so far
using diff_max calculate result as product of diff_max and current element (nums[i]-nums[j])*nums[k]