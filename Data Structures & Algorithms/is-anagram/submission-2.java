class Solution {
    public boolean isAnagram(String s, String t) {
        List<Character> sList = new ArrayList<Character>();
        for (char c : s.toCharArray()) {
            sList.add(c);
        }

        for (char c : t.toCharArray()) {
            boolean removed = sList.remove((Character)c);
            if (!removed) {
                return false;
            }
        }

        return sList.size() == 0;
    }
}
