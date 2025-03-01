#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;
class Solution{
    public:
        vector<int> twoSum(vector<int>& nums, int target) {
            unordered_map<int, int> hashTable;
            for (int i = 0; i < nums.size(); i++) {
                hashTable[nums[i]] = i;
            }
            for (int i = 0; i < nums.size(); i++) {
                int complement = target - nums[i];
                if (hashTable.find(complement) != hashTable.end() && hashTable[complement] != i) {
                    return {i, hashTable[complement]};
                }
            }
            return {}; // No solution found
        }
};

int main() {
    Solution solution;
    vector<int> nums = {2, 7, 11, 15};
    int target = 9;
    vector<int> ans = solution.twoSum(nums, target);
    for (int i = 0; i < ans.size(); i++) {
        cout << ans[i] << " ";
    }
    return 0;
}
// use g++ -std=c++11 two-passHashTable.cpp to compile the code