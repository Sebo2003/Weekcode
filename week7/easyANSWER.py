"""
LEETCODE 1876
_________________________________________________________________________________________________
A string is good if there are no repeated characters. Given a string s​​​​​, return the number of good 
substrings of length three in s​​​​​​. Note that if there are multiple occurrences of the same substring, 
every occurrence should be counted. A substring is a contiguous sequence of characters in a string.

Example 1:

Input: s = "xyzzaz"
Output: 1
Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz". 
The only good substring of length 3 is "xyz".

Example 2:

Input: s = "aababcabc"
Output: 4
Explanation: There are 7 substrings of size 3: "aab", "aba", "bab", "abc", "bca", "cab", and "abc".
The good substrings are "abc", "bca", "cab", and "abc".
______________________________________________________________________________________________________
LOGIC:
______________________________________________________________________________________________________
The key to this problem is the set() method. The set() method is like a list of elements, only it keeps
only unique elements when something is appended to it (in addition, all elements are automatically
added in numerical order, not relevant to this question but good to know). Knowing this, we can solve
the problem pretty quickly if we understand substrings.

In languages like Java, .substring() is its own method, but in Python, substrings can be defined as simply
a range of indexes within a string (remember, strings are merely arrays of characters in CS). This range
will be our window, in accordance to the Sliding Window technique.

We begin by initalizing a counter, this will keep track of how many unique substrings we find.

Then, we begin our foor loop: for i in range(len(s) - 2):. Why len(s) - 2, and not - 3 (or len(s))?
It is because, in accodance with the directions stated in this problem, the substring size we are
looking for is always 3 elements long. If we looped len(s) - 3 times, our substring would never
be able to reach the very last character of any array (look at how we defined our window: from i
to i+3 (inclusive)). Try this out yourself; mentally, look at the string, and drop the last 3
characters. Then, move the window, mentally, across the string. You'll find that the window will
never be able to reach the last character! So what do we do? Just account for that by doing 1 + -3,
which is -2!

The rest is simple, because of how set() works, and because we defined our substring to only ever
be i:i+3 elements long (3 elements long), if a window ever has anything OTHER than 3 elements, it
must be because the set() method identified duplicates, and refused to append them to itself.
Incrememnt counter by 1 for every succesful 3-element-long-set-identification, and you're golden!

Note that this solution only requires a single for loop, and a single-pass over the iteration of
string s. You could technically say the time compelxity is O(n-2), but remember that in Big O 
Notation, subtractions are rounded up to its nearest time complexity, so we just say O(n).
Compare this to the boilerplate, which is O(n^2) (and just generally more complicated)!

"""

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s) - 2):
            window = set(s[i:i+3])  # Form a window of size 3
            if len(window) == 3:  # Check if all characters in the window are distinct
                count += 1  # Increment count if the window is a good substring
        return count
        
if __name__ == "__main__":
    sol = Solution()
    string = "aababcabc"
    print(string)
    output = sol.countGoodSubstrings(string)
    print(f"For string {string}, there are {output} 'good strings' ")

