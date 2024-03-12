"""
LEETCODE 930
______________________________________________________________________________________________________
Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.

 

Example 1:

Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The 4 subarrays are in quotes below:
["1,0,1",0,1]
["1,0,1,0",1]
[1,"0,1,0,1"]
[1,0,"1,0,1"]

Example 2:

Input: nums = [0,0,0,0,0], goal = 0
Output: 15
*Note: a subarray can consit of only 1 element
__________________________________________________________________________________________________________

Below is the brute-force O(n^2) solution. n is the length of the list. It iterates from [start:n], where
start increments by values of 1 starting at 0 (if it makes it easier, subsitute start and end with i and j).
It then checks if the current subarray sums to goal, and increments counter by 1. How can this be done
in O(n) time? Its by use of the Sliding Window technique, as well as using a two-pointer based technique.


"""
class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        count = 0
        n = len(nums)
        for start in range(n):
            current_sum = 0
            for end in range(start, n):
                current_sum += nums[end]
                if current_sum == goal:
                    count += 1
        return count

if __name__ == "__main__":
    sol = Solution()
    nums = [1, 0, 1, 0, 1]
    goal = 2
    print(sol.numSubarraysWithSum(nums, goal))  # Output: 4

    nums = [0, 0, 0, 0, 0]
    goal = 0
    print(sol.numSubarraysWithSum(nums, goal))  # Output: 15
