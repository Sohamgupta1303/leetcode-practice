class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0) {
            return "";
        }

        String common = strs[0];
        for (String str : strs) {
            int chars = Math.min(common.length(), str.length());
            int i = 0;
            while (i < chars && common.charAt(i) == str.charAt(i)) {
                i++;
            }
            System.out.println(common);
            System.out.println(common.substring(i));

            common = common.substring(0, i);
        }

        return common;
    }
}