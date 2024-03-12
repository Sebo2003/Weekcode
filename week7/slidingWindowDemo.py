"""
This code returns the highest sum of a subarray of k length within input array nums.
It iterates through all possible subarrays of of k length in nums.
"""

def maxSum(nums, k):
    if k > len(nums):
        return None

    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(1, len(nums) - k + 1):
        window_sum = window_sum - nums[i - 1] + nums[i + k - 1]
        max_sum = max(max_sum, window_sum)

    return max_sum

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(maxSum(nums, k))  
