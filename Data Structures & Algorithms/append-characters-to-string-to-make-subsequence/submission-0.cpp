class Solution {
public:
    int appendCharacters(string s, string t) {
        int len = t.length();
        int z = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == t[z]) {
                z++;
            }
        }
        return len - z;
    }
};