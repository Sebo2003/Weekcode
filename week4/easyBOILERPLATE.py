class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 0:
            return False
        
        #Remember that x^y = x*x...
        
        return False

if __name__ == "__main__":
    sol = Solution()
    number = 1
    resultBool = sol.isPerfectSquare(number)
    print(f"Is {number} a perfect square? Answer: {resultBool}")
