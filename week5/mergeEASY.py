"""
The following code consists of a Pythonic implementation of the Mergesort algorithm

However, there is a catch:

There are 5 logical mistakes in the code below. Your job is to identify the problems,
and then fix them. It is not until you solve all 5 mistakes with the code will you
be able to print the correct result, which should look like this:

BEFORE:  [4, 0, -1, 7, 6]
AFTER:  [-1, 0, 4, 6, 7]


If it looks like anything else, problems still exist. All problems are logical, there
are no syntax errors in the code. In addition, all problems can be solved using a single edit, 
nothing needs to be completley overhauled or rewritten. Below is an example:

[Assume we want to check whether one value is equal to another]:

X = Y (wrong)

X == Y (correct)

The example above is not neccisarliy related to Mergesort, its just to examplify the 
degree of any given mistake in the code - they are simple, small problems, but ultimatley 
result in wrong logical operations. 

To reiterate, 5 of these simple mistakes exist.

If you execute the code below as is, it will result in a "RecursionError", that can be your
starting point.

Good luck!
"""

class Solution(object):
    def sortArray(self, nums):
        if len(nums) < 1:
            return nums

        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]

        left = self.sortArray(right)
        right = self.sortArray(right)

        return self.merge(left, right)

    def merge(self, left, right):
        indexL, indexR = 0, 1
        merged = []

        while indexL < len(left) or indexR < len(right):
            if left[indexL] < right[indexR]:
                merged.append(left[indexL])
                indexL += 1
            else:
                merged.append(right[indexR])
                indexR += 1

        merged.extend(left[indexL:])
        merged.extend(right[:indexR])

        return merged

if __name__ == "__main__":
    nums = [4, 0, -1, 7, 6]
    print("BEFORE: ", nums)
    sol = Solution()
    merged = sol.sortArray(nums)
    print("AFTER: ", merged)
