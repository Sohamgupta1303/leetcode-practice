class Solution {
    public int removeElement(int[] nums, int val) {
        int padding = 0;
        for (int i = nums.length - 1; i > -1; i--) {
            if (nums[i] == val) {
                int temp = nums[nums.length - 1 - padding];
                nums[nums.length - 1 - padding] = val;
                nums[i] = temp;
                padding++;
            }
        }
        return nums.length - padding;
    }
}