class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        unordered_map<int, int> time;
        int n = position.size();
        if (n == 1) {
            return 1;
        }
        for (int i = 0; i < speed.size(); i++) {
            time[position[i]] = speed[i];
        }
        sort(position.begin(), position.end());
        stack<double> s;
        for (int i = 0; i < speed.size(); i++) {
            double x = (double)(target - position[i]) / time[position[i]];
            std::cout << x << " \n";
            while (!s.empty() && x >= s.top()) {
                n--;
                s.pop();
                
            }
            s.push(x);
        }
        return n;
    }
};
