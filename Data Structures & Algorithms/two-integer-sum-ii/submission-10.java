class Solution {
    public int[] twoSum(int[] numbers, int target) {
        /*
            Normal twoSum: go through the array numbers and for 
            each element we check if an existing hashSet (with all the 
            previous elments) has target - numbers[i] and if it does 
            we return those two numbers. 

            the difference: in this one we need to return the indices
            but also i think you have to do it using two pointers. 
        */

        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int i = 0; i < numbers.length; i++) {
            int val = numbers[i];
            if (val*2 != target && map.keySet().contains(target - val)) {
                int[] ret = {map.get(target - val) + 1, i + 1};
                return ret;
            }
            map.putIfAbsent(val , i);
        }
        return null;   
    }
}
