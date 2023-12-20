# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
This problem checks wheather an array contains any duplicate elements. The efficient solution can be the utilization of set() method because set holds only unique values. After taking iteration through the array, I can track the unique elements and if any duplicate is found, the function will return the true otherwise false 

# Approach
<!-- Describe your approach to solving the problem. -->
set() holds unique values. Use a set to check for duplicates while iterating through the array, returning True if a duplicate is found, and False otherwises
# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
The time complexity is $$O(n)$$, where 'n' is the length of the input array nums. This is because the code iterates through the array once, and each set operation (addition and lookup) takes constant time on average.

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
The space complexity is also $$O(n)$$ in the worst case. In the worst case, if there are no duplicates in the array, the set unique_elements could potentially store all 'n' elements of the array. In the average case, the space complexity might be less than O(n) because duplicates are found earlier in the iteration, causing the set size to be smaller.
# Code
```
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicate = set()
        for num in nums:
            if num in duplicate:
                return True
            duplicate.add(num)
        return False


# print(containsDuplicate([1,2,3,1]))
```