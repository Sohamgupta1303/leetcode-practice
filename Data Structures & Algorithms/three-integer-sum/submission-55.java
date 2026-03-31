class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        Set<List<Integer>> triplets = new HashSet<>();
        List<List<Integer>> answer = new ArrayList<>();

        for (int i = 0 ; i < nums.length; i++) {
            int left = i + 1;
            int right = nums.length - 1;
            while (right > left) {
                int sum = nums[right] + nums[left] + nums[i];
                if (sum > 0) {
                    right--;
                } else if (sum < 0) {
                    left++;
                } else {
                    List<Integer> triplet = new ArrayList<Integer>();
                    triplet.add(nums[left]);
                    triplet.add(nums[right]);
                    triplet.add(nums[i]);
                    triplets.add(triplet);
                    right --; left++;
                    
                }
            }
        }
        for (List<Integer> boy : triplets) {
            answer.add(boy);
        }
        return answer;
    }
}
