class Solution {

    public String encode(List<String> strs) {
        StringBuilder toreturn = new StringBuilder();
        for (String s : strs) {
            int len = s.length();
            String size = Integer.toString(len);
            String sizelen = Integer.toString(size.length());
            toreturn.append(sizelen);
            toreturn.append(size);
            toreturn.append(s);
        }
        String toReturn = toreturn.toString();
        return toReturn;
    }

    public List<String> decode(String str) {
        List<String> toReturn = new ArrayList<String>();
        char[] letters = str.toCharArray();
        //traversing the array
        int i = 0;
        while (i < letters.length) {
            int num = letters[i] - '0';
            int len = 0;
            if (num == 1) {
                len = letters[i+1] - '0';
            } else {
                for (int j = i+1; j < i + 1 + num; j++) {
                    int val = letters[j] - '0';
                    len += (val)*(Math.pow((double)10, (double)(num - (j - i))));
                }
            }
            StringBuilder sb = new StringBuilder();
            for (int j = i+num+1; j < i+num+1+len ; j++) {
                sb.append(letters[j]);
            }
            toReturn.add(sb.toString());
            i += 1+len+num;
        }
        return toReturn;
    }
}
