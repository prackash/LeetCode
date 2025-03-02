#include <iostream>
#include <string>
#include <unordered_set>
using namespace std;
class Solution{
    public:
        int lengthOfLongestSubstring(string s){
            int n = s.size();
            int ans = 0;
            unordered_set<char> index;
            int left = 0;

            for(int right=0; right<n; right++){
                if(index.count(s[right])== 0){
                    index.insert(s[right]);
                    ans = max(ans, right - left + 1);
                } else{
                    while(index.count(s[right]) != 0){
                        index.erase(s[left]);
                        left++;
                    }
                    index.insert(s[right]);
                }
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