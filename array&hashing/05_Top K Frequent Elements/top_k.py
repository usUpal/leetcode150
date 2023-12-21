from collections import Counter
import heapq  # heapq is a min-heap implementation in Python.


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
