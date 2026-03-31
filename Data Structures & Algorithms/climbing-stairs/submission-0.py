class Solution:
    def climbStairs(self, n: int) -> int:
        # base cases
        if (n < 2):
            return 1;
        if (n == 2):
            return 2;

        # recursive case
        return self.climbStairs(n - 1) + self.climbStairs(n - 2);

        