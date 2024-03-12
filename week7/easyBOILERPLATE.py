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
 

This boilerplate comes pre-loaded with the brute force solution to this problem. It uses a hashmap (dictonary)
to identify duplicates in each substring. Because of this, the time compelxity of this code is O(n^2), because
we iterate over the length of the dictonary for every iteration of a character in our input (string s). 
However, using the Sliding Window Technique, it is possible to solve the same problem in O(n) time, which
is expotentially faster!

Hint: Lookup the set() method for Python...

"""

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        counter = 0

        for i in range(len(s)):
            chars = {}
            sub = s[i:i+3]
            if(len(sub) != 3):
                break
            for char in sub:
                if char not in chars:
                    chars[char] = 1
                else:
                    chars[char]+=1

            if(len(chars) == 3):
                counter += 1 

        return counter
        
if __name__ == "__main__":
    sol = Solution()
    string = "xyzzaz"
    print(string)
    output = sol.countGoodSubstrings(string)
    print(f"For string {string}, there are {output} 'good strings' ")

