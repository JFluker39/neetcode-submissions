class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        vector<int> result(n ,0);
        stack<vector<int>> temps;
        for (int i = 0; i < n; i++) {
            if(temps.empty()) {
                temps.push({temperatures[i], i});
            }
            else if (temperatures[i] > temps.top()[0]) {
                while(!temps.empty() && temperatures[i] > temps.top()[0]) {
                    result[temps.top()[1]] = i - temps.top()[1];
                    temps.pop();
                }
                temps.push({temperatures[i], i});
            }
            else {
                temps.push({temperatures[i], i});
            }
        }
        return result;

    }
};
