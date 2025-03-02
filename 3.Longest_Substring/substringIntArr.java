import java.util.Arrays;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length();
        int maxLength = 0;
        int[] charIndex = new int[128];
        Arrays.fill(charIndex, -1);
        int left = 0;
        
        for (int right = 0; right < n; right++) {
            if (charIndex[s.charAt(right)] >= left) {
                left = charIndex[s.charAt(right)] + 1;
            }
            charIndex[s.charAt(right)] = right;
            maxLength = Math.max(maxLength, right - left + 1);
        }
        
        return maxLength;
    }
}

public class substringIntArr{
    public static void main(String[] args){
        Solution sol = new Solution();
        String s = "abcabcbb";
        System.out.println(sol.lengthOfLongestSubstring(s));
    }
}
// Time complexity: O(n)
// Space complexity: O(128) = O(1)
// n is the length of s