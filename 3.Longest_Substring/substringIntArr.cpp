#include <iostream>
#include <vector>
#include <string>
using namespace std;
class Solution{
    public:
        int lengthOfLongestSubstring(string s){
            int n = s.size();
            int ans = 0;
            vector<int> index(128, -1);
            int left = 0;
            for(int right = 0; right < n; right++){
                if(left <= index[s[right]]){
                    left = index[s[right]] + 1;
                }
                index[s[right]] = right;
                ans = max(ans, right - left + 1);
            }
            return ans;
        }
};

int main(){
    string s = "abcabcbb";
    Solution sol;
    cout << sol.lengthOfLongestSubstring(s) << endl;
    return 0;
}