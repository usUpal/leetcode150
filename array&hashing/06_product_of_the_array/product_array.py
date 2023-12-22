class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        prefix_product, suffix_product = 1, 1

        # Calculate prefix products
        for i in range(n):
            result[i] *= prefix_product
            prefix_product *= nums[i]

        # Calculate suffix products
        for i in range(n - 1, -1, -1):
            result[i] *= suffix_product
            suffix_product *= nums[i]

        return result


sol = Solution()
print(sol.productExceptSelf([1, 2, 3, 4]))  # [24, 12, 8, 6]
