"""
LeetCode 70: Climbing Stairs
You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        one_step_before = 2
        two_steps_before = 1
        for i in range(3, n + 1):
            current = one_step_before + two_steps_before
            two_steps_before = one_step_before
            one_step_before = current
        return one_step_before\n