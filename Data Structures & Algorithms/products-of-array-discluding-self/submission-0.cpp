class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int count = 0;
        for (int n: nums) {
            if (n == 0) {
                count += 1;
            }
        }
        if (count >= 2) {
            vector<int> out(nums.size(), 0);
            return out;
        }
        else if (count == 1) {
            vector<int> fin(nums.size(), 0);
            int res = 1;
            int s = 0;
            for (int i = 0; i < nums.size(); i++) {
                if (nums[i] != 0) {
                    res *= nums[i];
                }
                else{
                    s = i;
                }    
            }
            fin[s] = res;
            return fin;
        }
        else {
            int res = 1;
            vector<int> output;
            for (int num: nums) {
                res *= num;
            }
            std::cout << res << "\n";
            for (int i = 0; i < nums.size(); i++) {
                output.push_back(res / nums[i]);
            }
            return output;
        }
    }
};
