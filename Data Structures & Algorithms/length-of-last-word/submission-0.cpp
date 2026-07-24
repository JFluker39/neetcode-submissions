class Solution {
public:
    int lengthOfLastWord(string s) {
        int len = 0;
        int n = s.length();
        int letter_seen = 0;

        for (int i = n - 1; i >= 0; i--) {
            if (s[i] == ' ' && letter_seen == 0) {
                continue;
            }
            else if (s[i] == ' ' && letter_seen > 0) {
                break;
            }
            else {
                letter_seen++;
                len++;
            }
        }
        return len;
        
    }
};