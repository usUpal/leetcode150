class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        duplicate = set()
        for num in nums:
            if num in duplicate:
                return True
            duplicate.add(num)
        return False


sol = Solution()
print(sol.containsDuplicate([1, 2, 3, 1]))  # True
