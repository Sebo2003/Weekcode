import math 

class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:

        #Remember division rules in Python, and that in this problem, we round UP
        #9/5 = 1.8
        #9//5 = 1
        #math.ceil(9/5) = 2

        return 0 #Not your final answer. What should you return at the end?

if __name__ == "__main__":
    sol = Solution()
    threshold = 6
    nums = [1,2,5,9]
    resultInt = sol.smallestDivisor(nums, threshold)
    print("SMALLEST DIVISOR: ", resultInt)