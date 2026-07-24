class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int n = nums.size();
        unordered_set<int> c;
        int l = 0;
        int r = 0;
        int start = 0;
        while(nums[l] != nums[r] || start == 0) {
            start = 1;
            if (l < n - 1){
                l += 1;
            }
            else {
                l = 0;
            }
            if (r < n - 2) {
                r += 2;
            }
            else if (r < n -1) {
                r = 0;
            }
            else {
                r = 1;
            }

        }   
        return nums[l];     
    }
};
