class Solution():
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        sumOf = 0
        
        for i in range(len(nums)):
            i+=1
            for j, num in enumerate(nums):
                cur = num/i
                sumOf+=cur
            if sumOf < i:
                return i

        return 0

if __name__ == "__main__":
    sol = Solution()
    threshold = 6
    nums = [1,2,5,9]
    resultInt = sol.smallestDivisor(nums, threshold)
    print("SMALLEST DIVISOR: ", resultInt)