import java.util.HashMap;
import java.util.Map;

class Solution{
    public int[] twoSum(int[] nums, int target){
        Map<Integer, Integer> map = new HashMap<>();
        for(int i = 0; i < nums.length; i++){
            map.put(nums[i], i);
        }
        for(int i = 0; i < nums.length; i++){
            int complement = target - nums[i];
            if(map.containsKey(complement) && map.get(complement) != i){
                return new int[]{i, map.get(complement)};
            }
        }
        return new int[]{};
    }
}
public class twoPassHashTable{
    public static void main(String[] args){
        Solution sol = new Solution();
        int[] nums = {2, 7, 11, 15};
        int target = 9;
        int[] res = sol.twoSum(nums, target);
        for(int i = 0; i < res.length; i++){
            System.out.print(res[i] + " ");
        }
    }
}