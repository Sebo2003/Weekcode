"""
LEETCODE 4
___________________________
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:

    nums1.length == m
    nums2.length == n
    0 <= m <= 1000
    0 <= n <= 1000
    1 <= m + n <= 2000
    -10^6 <= nums1[i], nums2[i] <= 10^6
______________________________________
LOGIC:

To be honest, just watch the Neetcode video on this: https://www.youtube.com/watch?v=q6IEA26hvXc&t=30s
He'll explain it real good
_______________________________________
"""
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        left, right = 0, m

        while left <= right:
            partition_nums1 = (left + right) // 2
            partition_nums2 = (m + n + 1) // 2 - partition_nums1

            max_left_nums1 = float('-inf') if partition_nums1 == 0 else nums1[partition_nums1 - 1]
            min_right_nums1 = float('inf') if partition_nums1 == m else nums1[partition_nums1]

            max_left_nums2 = float('-inf') if partition_nums2 == 0 else nums2[partition_nums2 - 1]
            min_right_nums2 = float('inf') if partition_nums2 == n else nums2[partition_nums2]

            if max_left_nums1 <= min_right_nums2 and max_left_nums2 <= min_right_nums1:
                if (m + n) % 2 == 0:
                    return (max(max_left_nums1, max_left_nums2) + min(min_right_nums1, min_right_nums2)) / 2.0
                else:
                    return max(max_left_nums1, max_left_nums2)
            elif max_left_nums1 > min_right_nums2:
                right = partition_nums1 - 1
            else:
                left = partition_nums1 + 1

solution = Solution()
nums1 = [1, 3]
nums2 = [2]
print(solution.findMedianSortedArrays(nums1, nums2)) 

nums1 = [1, 2]
nums2 = [3, 4]
print(solution.findMedianSortedArrays(nums1, nums2))
