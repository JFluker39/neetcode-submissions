class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        vector<int> result(n ,0);
        stack<int> temps;
        for (int i = 0; i < n; i++) {
            while(!temps.empty() && temperatures[i] > temperatures[temps.top()]) {
                result[temps.top()] = i - temps.top();
                temps.pop();
            }
            temps.push(i);
 
        }
        return result;

    }
};
