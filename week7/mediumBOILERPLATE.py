"""
Given an integer array nums and an integer k, return true if there are two distinct indices 
i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
__________________________________________________________________________________________

This is the brute force O(n^2) solution. We compare the ith element against every i + 1th element, or j.
We search from lenght i to len(nums) - 1, as j = i + 1. If both conditions are met, return True. 
How can this be implemented in O(n) time using Sliding Window?

"""
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        size = len(nums)
        for i in range(size):
            for j in range(i, size-1):
                j+=1
                if nums[i] == nums[j] and abs(i - j) <= k:
                    return True

        return False

if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,3,1,2,3]
    k = 2
    valid = sol.containsNearbyDuplicate(nums, k)
    print(f"The validity of {nums} is: {valid}")
    #print(f"In the list {nums}, there {'IS' if valid else 'IS NOT'} at least 1 valid duplicate set")

        
