class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> anagram =  new HashMap<>();

        for (String s : strs) {
            String letters = Arrays.toString(getLetterList(s));
            if (anagram.containsKey(letters)) {
                anagram.get(letters).add(s);
            } else {
                List<String> values = new ArrayList<>();
                values.add(s);
                anagram.put(letters, values);
            }
        }

        List<List<String>> toreturn = new ArrayList<>();
        for (String i : anagram.keySet()) {
            toreturn.add(anagram.get(i));
        }

        return toreturn;
    }

    private int[] getLetterList(String s) {
        int[] letters = new int[26];
        for (char c : s.toCharArray()) {
            letters[c - 'a']++;
        }
        return letters;
    }
}