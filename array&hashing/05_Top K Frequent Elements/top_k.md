# Intuition

<!-- Describe your first thoughts on how to solve this problem. -->

here is to find the top K most frequent elements in a list, which can be solved by counting the frequency of each element using a hash table and selecting the top K elements with the highest frequency using a priority queue.A priority queue is a special type of queue in which each element has a priority associated with it and elements are served in order of their priority. Elements with higher priority are served before those with lower priority.

# Approach

<!-- Describe your approach to solving the problem. -->

The approach uses a hash table to count the frequency of each element in the input array and a priority queue to select the top K elements with the highest frequency.

# Complexity

- Time complexity:
  <!-- Add your time complexity here, e.g. $$O(n)$$ -->
  The time complexity of this solution is $$O(n log k)$$ where n is the length of the input array.because counting the frequency of each element in the input array takes $$O(n)$$ time and selecting the top K elements using a priority queue takes $$O(k log k)$$ time.
- Space complexity:
  <!-- Add your space complexity here, e.g. $$O(n)$$ -->
  The space complexity is $$O(n)$$ for the hash table used to count the frequency of each element.Because of a hash table is used to store the frequency of each element in the input array, which takes $$O(n)$$ space.

# Code

```
from collections import Counter
import heapq # heapq is a min-heap implementation in Python.


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts = Counter(
            nums
        )  # Use collections.Counter to count the frequency of each element in the input array nums.
        return heapq.nlargest(
            k, counts.keys(), key=counts.get
        )  # Using heapq.nlargest to select the top k elements with the highest frequency. heapq.nlargest takes a key function as argument, which is used to compare elements. In this case, frequency count as the key.


sol = Solution()
print(sol.topKFrequent([1, 1, 1, 2, 2, 3], 2))
```
