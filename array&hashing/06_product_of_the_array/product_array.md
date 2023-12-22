# Intuition

<!-- Describe your first thoughts on how to solve this problem. -->

Calculate the product of all elements to the left and right of each element.

# Approach

<!-- Describe your approach to solving the problem. -->

Use prefix and suffix products to compute the result.

# Complexity

- Time complexity:
  <!-- Add your time complexity here, e.g. $$O(n)$$ -->
  $$O(n)$$
- Space complexity:
  <!-- Add your space complexity here, e.g. $$O(n)$$ -->
  $$O(n)$$

# Code

```
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
```
