class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] toret = new int[2];

        HashMap<Integer, Integer> values = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            values.put(nums[i], i);
        }

        for (int i = 0; i < nums.length; i++) {
            if (values.containsKey(target - nums[i]) && i != values.get(target - nums[i])) {
                toret[0] = Math.min(i, values.get(target-nums[i]));
                toret[1] = Math.max(i, values.get(target-nums[i]));
                return toret;
            }
        }

        return toret;
            
        
    }
}
