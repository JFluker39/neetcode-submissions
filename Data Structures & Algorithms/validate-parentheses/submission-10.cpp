class Solution {
public:
    bool isValid(string s) {
        stack<char> open;
        unordered_map<char, char> check = {
            {')' , '('},
            {'}' , '{'},
            {']' , '['}
        };

        for (char c: s) {
            if (check.count(c)) {
                if (!open.empty() && check[c] == open.top()) {
                    open.pop();
                }
                else {
                    return false;
                }
            }
            else {
                open.push(c);
            }
        }
        return open.empty();
    }
};
