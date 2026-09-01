class Solution(object):
    def climbStairs(self, n):
        dp = [-1] * (n + 1)
        return self.solve(n, dp)

    def solve(self, n, dp):
        if n < 0:
            return 0

        if n == 0:
            return 1

        if dp[n] != -1:
            return dp[n]

        one = self.solve(n - 1, dp)
        two = self.solve(n - 2, dp)

        dp[n] = one + two
        return dp[n]