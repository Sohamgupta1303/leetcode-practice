class Solution {
    public int[] twoSum(int[] numbers, int target) {
        /*
            Normal twoSum: go through the array numbers and for 
            each element we check if an existing hashSet (with all the 
            previous elments) has target - numbers[i] and if it does 
            we return those two numbers. 

            the difference: in this one we need to return the indices
            but also i think you have to do it using two pointers (YOU DO 
            BECAUSE YOU CANT USE O(n) SPACE)
        */
        int left = 0; 
        int right = numbers.length - 1;

        while (right > left) {
            int sum = numbers[left] + numbers[right];
            if (sum > target) {
                right = right - 1;
            } else if (sum < target) {
                left = left + 1;
            } else {
                return new int[] {left + 1, right + 1};
            }
        }
        return new int[0];
    }
}
