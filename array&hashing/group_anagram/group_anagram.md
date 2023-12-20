# Intuition

<!-- Describe your first thoughts on how to solve this problem. -->

This problem can be solved by sorting the characters of each string in the input list to create a sorted key for a dict, and then grouping the strings together based on their sorted keys.

# Approach

<!-- Describe your approach to solving the problem. -->

The code creates an empty dictionary to store the anagram groups, loops through the input array of strings, sorts the characters of each string to create a sorted key for the dictionary, and groups the strings together based on their sorted keys. Finally, the code returns the values of the dictionary as a list.

# Complexity

- Time complexity:
  <!-- Add your time complexity here, e.g. $$O(n)$$ -->
  The time complexity of the code is $$O(n)$$, where n is the number of strings in the input array.
- Space complexity:
  <!-- Add your space complexity here, e.g. $$O(n)$$ -->
  The space complexity of the code is $$O(n*m)$$, where n is the number of strings in the input list and m is the average length of the strings. This is because the code creates a dict to store the anagram groups, and the size of the dict is proportional to the number of anagram groups, which is determined by the number of strings and the length of the strings

# Code

```
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # create an empty dict to store the anagram groups
        anagram_groups = {}

        for (
            s
        ) in (
            strs
        ):  # iterate through the list of strings to find anagrams. time complexity: O(n)
            sorted_key = "".join(
                sorted(s)
            )  # sort the string and use it as a key for the dict

            if (
                sorted_key in anagram_groups
            ):  # if the key already exists, append the string to the list
                anagram_groups[sorted_key].append(s)
            else:
                anagram_groups[sorted_key] = [
                    s
                ]  # if the key doesn't exist, create a new key and add the string to the list
        return list(anagram_groups.values())  # return the values of the dict as a list


sol = Solution()
print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

```
