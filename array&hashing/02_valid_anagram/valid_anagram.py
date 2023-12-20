class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False  # if length of the 2 string doesn't match then return false already

        # storing the frequency of each character using dict
        s_freq = {}
        t_freq = {}

        # populate the frequency of each char of 2 string in dict
        for i in s:
            s_freq[i] = (
                s_freq.get(i, 0) + 1
            )  # get() method is for getting the value of the key and here 0 is setting default value of the key and then increment 1 if frequency occurs as well.
        for i in t:
            t_freq[i] = t_freq.get(i, 0) + 1

        return (
            s_freq == t_freq
        )  # check if the dictionary matches; if matches returns true otherwise false
