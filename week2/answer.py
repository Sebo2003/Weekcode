class Solution(object):
    def twoSub(self, nums:list[int], target: int) -> list[int]:

        hashmap = {}

        for i, curr in enumerate(nums):
           
           x = target + curr

           if x in hashmap:
               return [hashmap[x], i]
           
           hashmap[curr] = i

        return []
    
if __name__ == "__main__":
    sol = Solution()
    nums = [5,-3,0,6,3]
    target = -1
    returnList = sol.twoSub(nums, target)
    print("RESULTS: ", returnList)
























"""
#O(n^2) solution
class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] - nums[j] == target:
                    return [i, j]

# Example usage:
sol = Solution()

nums1 = [5,8,0,3,2]
target1 = 5

result1 = sol.twoSum(nums1, target1)
print("Example 1:", result1)  

"""
