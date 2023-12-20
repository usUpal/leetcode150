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
