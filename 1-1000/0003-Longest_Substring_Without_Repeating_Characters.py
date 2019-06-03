"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class SolutionClassFinal:
    def lengthOfLongestSubstring(self, s):
        """
        :param s: str
        :return: int
        """
        map = {}
        maxlen = 0
        for i, val in enumerate(s):
            if val not in map:
                map[val] = i
            else:
                maxlen = max(maxlen, i - map[val])
                map[val] = i

        return maxlen
# Space: O(1)
# Time: O(N)


if __name__ == "__main__":
    s = 'abcabcbb'
    print(SolutionClassFinal().lengthOfLongestSubstring(s))
