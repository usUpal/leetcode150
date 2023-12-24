# Intuition

<!-- Describe your first thoughts on how to solve this problem. -->

Checking the validity of rows, columns, and 3x3 boxes in one pass

# Approach

<!-- Describe your approach to solving the problem. -->

Use sets to track unique values in rows, columns, and boxes. enum is for enlisting the values.

# Complexity

- Time complexity:
  <!-- Add your time complexity here, e.g. $$O(n)$$ -->
  $$O(1)$$ since the board size is constant (9x9).
- Space complexity:
  <!-- Add your space complexity here, e.g. $$O(n)$$ -->
  $$o(1)$$

# Code

```
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Set is here to keep track of seen values
        seen = set()

        # Iterate through each cell in the board
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                # Skip empty cells
                if cell != '.':
                    # Check if the value is already seen in the same row, column, or 3x3 box
                    if (cell, i) in seen or (j, cell) in seen or (i // 3, j // 3, cell) in seen:
                        return False
                    # Add the current value to the set
                    seen.add((cell, i))
                    seen.add((j, cell))
                    seen.add((i // 3, j // 3, cell))

        # If no conflicts found, the board is valid
        return True
```
