"""
LEETCODE 1283:
________________________________
Given an array of integers nums and an integer threshold, we will choose a positive integer divisor, 
divide all the array by it, and sum the division's result. Find the smallest divisor such that the 
result mentioned above is less than or equal to threshold.

Each result of the division is rounded to the nearest integer greater than or equal to that element. 
(For example: 7/3 = 3 and 10/2 = 5).

Example 1:

Input: nums = [1,2,5,9], threshold = 6
Output: 5
Explanation: We can get a sum to 17 (1+2+5+9) if the divisor is 1. 
If the divisor is 4 we can get a sum of 7 (1+1+2+3) and if the divisor is 5 the sum will be 5 (1+1+1+2). 

Example 2:

Input: nums = [44,22,33,11,1], threshold = 5
Output: 44

Constraints:

    1 <= nums.length <= 5 * 10^4
    1 <= nums[i] <= 10^6
    nums.length <= threshold <= 10^6
__________________________________________________________________________________________
LOGIC:

First, let us more fully understand what the problem is asking of us. It is asking us to find the divisor
that is as close to variable treshold as possible, without going over, where the divisor is the intger
that, when all elements in the array are diveded by and their quotients sum, is less than threshold. Its
a little tricky to write or grasp, but once you understand that, it should get easier. 

This problem can be solved linearly. In fact, it may be your first instinct. If we imagine every element in
some array as "i", then what we would try in a linear fashion would be: i/1, i/2, i/3, i/4, i/5, i/6, and so on,
until we find that magic number. The probelm is that, at largest values of i or long lengths of an array, this
is wildly ineffecient. Instead, we need an algorithm that allows us to perform much fewer operations. In this
case, we can use binary search to achieve log(n) time.

As you know, binary search only works for lists that are already sorted. But, in [Example 2], we see array nums
to be sorted in random order ([44,22,33,11,1]), so what gives? Let us think for a moment how we might solve
this problem mathematically.

A very important detail of this problem is that, when two numbers don't divide evenly, to round UP. This is
different from how you might expect to solve this problem, using the integer division operation (//). The key 
problem with integer division in this scenario however, is that in Python, integer division always rounds integers 
DOWN. This is why we use math.ceil() instead of //, as math.ceil() rounds integer division UP.

At any rate, because we are rounding UP in this problem, lets think of what the implications are. This would mean
that the smallest possible element in any array at any given time is 1. This is pricecly because we are rounding
up. For example, if we are in the 9th iteration of some array, and we do 1/9, this rounds UP to 1 and not DOWN
to 0. At the same time, we know that in math, any number divided by itself is 1. When we combine these two
facts, we find a very important piece of information: the largest element in any array is our maximum possible
divisor size. This is because if we divded every element in the array but that maximum divisor, every element
in that array will be 1. 

Because of this, we know our upper bound will be the maximum of any array. So what about our minimum? As we
established earlier, the smallest possible element in any array in this problem is 1. Thus, we have found the
range of possibilities our divisor can lie in: [1, max]. This is certainly a better place to look than the 
infinite possibilities linear searching forces us to deal with!

This still doesn't solve the problem posited earlier though: our inputted list can be unsorted. Don't worry
though, because now that we know divisor must exist between [1, max], we can search for a divisor in a 
range that IS sorted. For example, say we have an array of [9,3,6,1]. Because we know divisor is within
[1, max], divisor can be any one of the numbers from this range: [1,2,3,4,5,6,7,8,9]. In our list,
our lower bound, or "left", is 1, and our upper bound, or "right" is max, in this case 9. Hence, we
define left = 1, and right = max(nums).

Now, we begin to implement binary search. First, we define how long we're gonna spend looking for
divisor, so we do while left <= right (because if right becomes less than left, we begin to traverse backwards).
Then, as we do in binary search, we define our mid point. In this case, we do the normal definition of mid
in a binary search in Python: mid = (left + right) // 2 (remember: we are traversing through [1, max] right
now, not nums!)

Before we continue, lets not forget the criteria of the problem. Divisor is defined as the integer that, 
when each element in the list is divded by and then are summed as, must be less than threshold. 

Now, we deal with this tricky bit of code: sum(math.ceil(num / mid) for num in nums) > threshold. Let break it down:

Firstly, lets look at the outermost layer, sum() > threshold. We know that if the sum of all elements in an array,
divided by divisor, is larger than our threshold, the value of divisor must be some value larger than what it is
right now (Because when dividing two numbers, x/y = z, we know y and z have an inverse relationship). Thus the 
loop continues. Hence: sum() > threshold. Therefore, we can infer that everything inside of sum() must be
all the elements divided by some number. So we go further.

Secondly, lets like in the innermost layer: math.ceil(num / mid) for num in nums. To understand this, we must
first understand a bit about syntax in python: a single-line for loop can be called, and its iterator can be
called in the same line in what's called a unary operation. With that being said, remember that math.ceil()
allows for integer division that rounds UP, so we start in there. What two integers are we dividng and rounding
UP? Its num / mid. We know what mid is, but what is "num"? "num" is defined in the for loop adjacent to this
equation: for num in nums. Remember that "nums" is our inputted array, so in this case, "num" is like our
i value. We are iterating over every element in array nums, where nums = 0, nums = 1, nums = 2, and so on.
So we can return to our math.ceil(): num / mid. Remeber what mid is! Its the mid of [1, max], not nums!

To summarize: sum(math.ceil(num / mid) for num in nums) > threshold finds the sum of all elements in 
array nums, where every element was divided by mid beforehand, and then comapres it against threshold. 
If sum(math.ceil(num / mid) for num in nums) > threshold is true, we do this: left = mid + 1. Why?

Well, if it is true that sum(math.ceil(num / mid) for num in nums) > threshold, then that means the 
value of mid begets a sum that is too large. Since we know that divding by larger numbers begets smaller
quoteints (remember the relationship between y and z in x/y = z), then we know we need to be using larger
numbers to divide by. Since [1, max] is sorted, we can move our lower bound, left, to be right of our
current mid point, and hence: left = mid + 1. We can inverse this logic to understand why, in the 
scenario of sum(math.ceil(num / mid) for num in nums) > threshold being false, right = mid - 1.

We do this a couple of times. Eventually, we find that left <= right, and our loop is done. We finally 
return left, and the problem is solved. But wait a minute, why left? Why not mid, or right, or aything
else? Why do we return left specifically?

Let us remind ourselves what left, right, and mid are exactly. Left is our lower limit, right is our
upper limit, and mid is the value inbetween left and right. And what are these bounds in relation to?
Its [1, max]. What is the problem asking us to return? The divisor. What is the divisor? The integer
that, when all elements in a array are divided by, and all those quotients are summed, the sum is
less than the threshold. 

Receall our loop condition: while left <= right. Once this condition is broken, it implies that the
left and right pointers have converged, and left is now greater than right. Since left is in charge of
our lower bounds, its final value will be the smallest element of our final list, and because of
how said list was iterated over (sum(math.ceil(num / mid) for num in nums) > threshold), will be,
by extension, the divisor that is as close to treshold as possible, without tipping over. The
left variable is our divisor. Returing right would return the wrong divisor, and returing mid would
just be returning some random number.

As so, when left is returned, the problem has been solved, and it has been solved far far far more
efficiently than if we did a linear search.
__________________________________________________________________________________________
"""

import math 

class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        left = 1
        right = max(nums)
        
        while left <= right:

            mid = (left + right) // 2

            if sum(math.ceil(num / mid) for num in nums) > threshold:
                left = mid + 1
            else:
                right = mid - 1

        return left

if __name__ == "__main__":
    sol = Solution()
    threshold = 6
    nums = [1,2,5,9]
    resultInt = sol.smallestDivisor(nums, threshold)
    print("SMALLEST DIVISOR: ", resultInt)