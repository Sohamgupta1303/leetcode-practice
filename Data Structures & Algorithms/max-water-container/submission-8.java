class Solution {
    public int maxArea(int[] heights) {
        int left = 0; 
        int right = heights.length - 1;
        
        int maxArea = 0;

        while (right > left) {
            int distance = right - left;
            int minHeight = Math.min(heights[left], heights[right]);

            int area = distance * minHeight;
            maxArea = Math.max(maxArea, area);
            System.out.println(left + ", " + right);
            System.out.println(maxArea);

            if (heights[left] <= heights[right]) {
                left++;
            } else {
                right--;
            }
        }

        return maxArea;
    }
}
