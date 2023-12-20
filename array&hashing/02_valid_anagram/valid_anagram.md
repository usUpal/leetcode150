# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
This problem checks if two strings have the same characters with the same frequencies. Frequency means the number of character occurs in the string.
# Approach
<!-- Describe your approach to solving the problem. -->
First check length of 2 strings. If length of the 2 string doesn't match then return false already.Then store the frequencies of each character in a dict. dict is a key-value pair data structure so that I can store the key as character and value as the frequency of those characters. Now through iteration populate the dictionary of each strings and check if the dictionary matched with each other, if matches return true otherwise false.
# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
The time complexity is $$O(n)$$ where 'n' is the length of the strings, as it involves iterating through the strings once. 
- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
The space complexity is also $$O(n)$$ due to the usage of dictionaries to store character frequencies.

# Code
```
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False # if length of the 2 string doesn't match then return false already
            
        # storing the frequency of each character using dict
        s_freq = {}
        t_freq = {}

        # populate the frequency of each char of 2 string in dict 
        for i in s:
            s_freq[i] = s_freq.get(i,0) + 1 # get() method is for getting the value of the key and here 0 is setting default value of the key and then increment 1 if frequency occurs as well.
        for i in t:
            t_freq[i] = t_freq.get(i,0) + 1

        
        return s_freq == t_freq # check if the dictionary matches; if matches returns true otherwise false
```