class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> val;
        for (int i = 0; i < nums.size(); i++) {
            int x = target - nums[i];
            if (val.find(x) != val.end()) {
                return {val[x], i};
            }
            val.insert({nums[i], i});
        }
        return {};
    }
};
