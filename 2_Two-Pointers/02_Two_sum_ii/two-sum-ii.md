# Intuition

<!-- Describe your first thoughts on how to solve this problem. -->

To find the two numbers, start with two pointers pointing to the beginning and end of the array. If the sum of the elements at these pointers is equal to the target, return their indices. If the sum is less than the target, move the left pointer to the right; if the sum is greater, move the right pointer to the left. Repeat until the target is reached.

# Approach

<!-- Describe your approach to solving the problem. -->

Use two pointers, one starting from the beginning and the other from the end. Adjust their positions based on whether the sum is less than or greater than the target.

# Complexity

- Time complexity:
  <!-- Add your time complexity here, e.g. $$O(n)$$ -->
  $$O(n)$$
- Space complexity:
  <!-- Add your space complexity here, e.g. $$O(n)$$ -->
  $$O(1)$$

# Code

```
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1

        return []
```
