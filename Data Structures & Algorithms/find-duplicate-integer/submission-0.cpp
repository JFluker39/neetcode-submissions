class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        unordered_set<int> c;
        for (int i = 0; i < nums.size(); i++) {
            if (c.count(nums[i])) {
                return nums[i];
            }
            else c.insert(nums[i]);
        }
    }
};
