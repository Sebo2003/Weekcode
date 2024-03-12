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
LOGIC:
__________________________________________________________________________________________
Like the easy problem, this problem relies upon using set(), which is a list that only keeps track of unique
elements added to it, in increasing order. This problem requires the use of a "dynamic" sliding window
(to solve in O(n) time), meaning the range of consideration (window) will change per some conditions on
some iterations. 

Here is how the problem will be solved:

The window will start at index 0 of nums, with a window size of 1 element to start. Since we need to 
compare nums[i] against nums[j], the window size is going to have to increase. So we increase its size
by one, from index 0 to index 1 (two elements long). How do we change the window size?

We do it by keeping track of its lowest and maximum bound, or in otherwords, its left and right most
element. Hence, we will use left and right pointers (two-pointer technique). Left, the minimum, will
begin at 0, as all arrays begin at index 0. Right, however, will be the iterator of our for loop. Why?
It is because the Right pointer will stretch out from the first element all the way to the last, and
as such, will also begin at index 0, but will gradually increase by 1 (just like i in a regular for loop).

So, we begin the for loop, iterating over the length of nums. First, we check if right - left > k. Why?
One of the criterion of the problem was to make sure abs(i - j) <= is true. Well, in a nested for loop,
we would know that i = i, and j = i + 1. That +1 is why we take the abs() of the difference. BUT, since
we are iterating by pointer Right, that's like saying j = i. Hence, we can just do the regular difference
between left and right. Think of it like this: abs(i - j) == j - i.

We compare that difference against > k. If the condition is met, we remove the leftth index of the
window, and increase left by 1. This action does two things: 1) Removes irrelevant data from our window,
and 2) raises our minimum by 1.

If the rightth index of nums exists in our window, that means it didn't hit any of our if statement
flags, and logically, must be equal to nums[left] (nums[i]). Else, we return False.

This video explains it very well: https://www.youtube.com/watch?v=ypn0aZ0nrL4

"""
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        window = set()
        left = 0
        for right in range(len(nums)):
            if(right - left) >= k:
                window.remove(nums[left])
                left+=1
            if nums[right] in window:
                return True
            window.add(nums[right])
        return False

if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,3,1,2,3]
    k = 2
    valid = sol.containsNearbyDuplicate(nums, k)
    print(f"The validity of {nums} is: {valid}")
    #print(f"In the list {nums}, there {'IS' if valid else 'IS NOT'} at least 1 valid duplicate set")

        
