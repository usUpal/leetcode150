# Intuition

<!-- Describe your first thoughts on how to solve this problem. -->

Compare the string with its reverse after removing non-alphanumeric characters.

# Approach

<!-- Describe your approach to solving the problem. -->

Use two pointers to traverse the string from both ends, skipping non-alphanumeric characters.

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
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char.lower() for char in s if char.isalnum())
        return s == s[::-1]

```
