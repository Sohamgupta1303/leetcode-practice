class Solution {
    public int majorityElement(int[] nums) {
        HashMap<Integer, Integer> numAndFreq = new HashMap<>();
        for (int num : nums) {
            int freq = numAndFreq.getOrDefault(num, 0);
            int newFreq = freq + 1;
            if (newFreq > (nums.length / 2)) {
                return num;
            }
            numAndFreq.put(num, newFreq);
        }
        return 0;
    }
}