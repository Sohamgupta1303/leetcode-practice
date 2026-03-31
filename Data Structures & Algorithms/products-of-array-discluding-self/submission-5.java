class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] toreturn = new int[nums.length];
        int[] prefix = new int[nums.length];
        int[] postfix = new int[nums.length];

        for (int i = 0; i < nums.length; i++) {
            prefix[i] = nums[i];
            if (i > 0) {
                prefix[i] = prefix[i]*prefix[i-1];
            }
        }
        for (int i = nums.length-1; i > -1; i--) {
            postfix[i] = nums[i];
            if (i < nums.length - 1) {
                postfix[i] = postfix[i]*postfix[i+1];
            }
            if (i == 0) {
                toreturn[i] = postfix[i+1];
            } else if (i == nums.length - 1) {
                toreturn[i] = prefix[i-1];
            } else {
                toreturn[i] = postfix[i+1] * prefix[i-1];
            } 
        }
        return toreturn;
    }   
}