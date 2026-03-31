class Solution {
public:

    string encode(vector<string>& strs) {
        string result = "";
        for (string str : strs) {
            int str_size = str.size();
            int str_size_size = (to_string(str_size)).size();
            result += to_string(str_size_size);
            result += to_string(str_size);
            result += str;
        }
        return result;
    }

    vector<string> decode(string s) {
        int i = 0;
        vector<string> result;
        while (i < s.size()) {
            int str_size_size = s[i] - '0';
            string str_size_string = "";
            for (int j = i + 1; j < i + 1 + str_size_size; j++) {
                str_size_string += s[j];
            }
            i += str_size_size;
            i += 1;
            int str_size = stoi(str_size_string);
            string str = "";
            int end = i + str_size;
            while (i < end) {
                str += s[i];
                i++;
            }
            result.push_back(str);
        }
        return result;
    }
};
