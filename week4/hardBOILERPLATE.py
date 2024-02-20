from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # Utilize partitioning to pinpoint the middle elements.
        # Remember to handle cases where one array is smaller than the other.
        # Good luck.

        return -1.0

solution = Solution()
nums1 = [1, 3]
nums2 = [2]
print(solution.findMedianSortedArrays(nums1, nums2)) #Should print 2.0

nums1 = [1, 2]
nums2 = [3, 4]
print(solution.findMedianSortedArrays(nums1, nums2)) #Should print 2.5
