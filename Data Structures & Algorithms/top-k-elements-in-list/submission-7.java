class Solution {
    public int[] topKFrequent(int[] nums, int k) {
         int[] topFrequent = new int[k];
         Map<Integer, Integer> numAndFrequency = new HashMap<>();
         int numCurrentElements = 0;

         for (int element : nums) {
            int frequency = numAndFrequency.getOrDefault(element, 0);
            numAndFrequency.put(element, frequency + 1);
         }
         numCurrentElements = numAndFrequency.keySet().size();

         while (numCurrentElements != k) {
            for (int element : numAndFrequency.keySet()) {
                int frequency = numAndFrequency.get(element);
                numAndFrequency.put(element, frequency - 1);

                if (numAndFrequency.get(element) == 0) {
                    numAndFrequency.put(element, numAndFrequency.get(element) - 1);
                    numCurrentElements -- ;
                }
                
            }
         }

         int i = 0;
         for (int num : numAndFrequency.keySet()) {
            if (numAndFrequency.get(num) > 0) {
                topFrequent[i] = num;
                i++;
            }
         }

         return topFrequent;
    }
}