# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
This problem is about finding two numbers in an array that add up to the target number that given as parameter of the function.
# Approach
<!-- Describe your approach to solving the problem. -->
First create an empty dict to store the indices of each number of the array. Then iteration of enumeration of the list with indices and track the value of the target in variable **complement**. Then check if the list contains two numbers that adds up to target number. Then add current number and its index to the empty dictionary.If loop doesn't found anything will return an empty list thus there is no solution.
# Complexity 
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
The time complexity of the solution is $$O(n)$$, because in the worst case you will only need to iterate through the array once.
- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
The space complexity of the solution is $$O(n)$$, because in the worst case you will need to store the indices of all the numbers in the  list.
# Code
```
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # empty dict to store the indices of each number of the array.
        num_dict = {} 

        for i, num in enumerate(nums): # enumerate returns list with indices
            complement= target - num   # keeping track of the value from target
            if complement in num_dict:
                return [num_dict[complement],i] # returning the list contains two numbers that adds up to the target 
            num_dict[num] =i # adds current number and its index to the dict
        return [] # if loop doesn't found anything will return empty list means there is no solution

        
```