#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hashMap;
        
        // O(n)
        for(int i = 0; i < nums.size(); i++) {
            int comp = target - nums[i];
            if (hashMap.contains(nums[i])) {
                int res = hashMap[nums[i]];
                return vector<int>{i, res};
            }
            hashMap[comp] = i;
        }
        
        return vector<int>{};
        
    }
};