class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Set is here to keep track of seen values
        seen = set()

        # Iterate through each cell in the board
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                # Skip empty cells
                if cell != ".":
                    # Check if the value is already seen in the same row, column, or 3x3 box
                    if (
                        (cell, i) in seen
                        or (j, cell) in seen
                        or (i // 3, j // 3, cell) in seen
                    ):
                        return False
                    # Add the current value to the set
                    seen.add((cell, i))
                    seen.add((j, cell))
                    seen.add((i // 3, j // 3, cell))

        # If no conflicts found, the board is valid
        return True


sol = Solution()
print(
    sol.isValidSudoku(
        [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )
)  # True
