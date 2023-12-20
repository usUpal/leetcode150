class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # empty dict to store the indices of each number of the array.
        num_dict = {}

        for i, num in enumerate(nums):  # enumerate returns list with indices
            complement = target - num  # keeping track of the value from target
            if complement in num_dict:
                return [
                    num_dict[complement],
                    i,
                ]  # returning the list contains two numbers that adds up to the target
            num_dict[num] = i  # adds current number and its index to the dict
        return (
            []
        )  # if loop doesn't found anything will return empty list means there is no solution
