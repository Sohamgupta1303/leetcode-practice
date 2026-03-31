class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> values = new HashSet<Integer>();
        for (int num : nums) {
            values.add(num);
        }

        int longestSequence = 0;
        for (int num : nums) {
            if (!values.contains(num - 1)) {
                int sequence = 1;
                while (values.contains(num + 1)) {
                    sequence++;
                    num++;
                }
                longestSequence = longestSequence > sequence ? longestSequence : sequence;
            }
        }
        return longestSequence;
    }
}
