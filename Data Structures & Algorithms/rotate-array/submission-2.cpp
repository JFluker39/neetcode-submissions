class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        vector<int> rot = nums;
        int len = nums.size();
        for (int i = 0; i < len; i++) {
            nums[(i + k) % len] = rot[i];
        }
    }
};