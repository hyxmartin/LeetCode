"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""


class SolutionClassBruteForce:
    def longestPalindrome(self, s):
        """
        :param s: String
        :return: String
        """
        ret = ''
        for i in range(len(s)):
            for j in range(i, len(s), 1):
                if s[i:j] == s[i:j][::-1] and (j - i > len(ret)):
                    ret = s[i:j]
        return ret

# Space: O(n)
# Time: O(n^2)


class SolutionClassDynamicProgramming:
    def longestPalindrome(self, s):
        """
        :param s: String
        :return: String
        """

        max = 1
        start = 0
        i = 0
        table = [[0 for x in range(len(s))] for y in range(len(s))]

        # 1 char
        while i in range(len(s)):
            table[i][i] = 1
            max = 1
            start = i
            i = i + 1

        i = 0
        # 2 chars
        while i in range(len(s) - 1):
            if s[i] == s[i+1]:
                table[i][i+1] = 1
                max = 2
                start = i
            i = i + 1

        # three chars or more
        k = 3
        while k <= len(s):
            i = 0
            while i <= len(s) - k:
                j = i + k - 1
                if s[i] == s[j] and table[i+1][j-1] == 1:
                    table[i][j] = 1
                    max = k
                    start = i
                i = i + 1
            k = k + 1

        return s[start: start + max]


# Space: O(n)
# Time: O(n^2)


if __name__ == "__main__":
    s = "baabbaa"
    print(SolutionClassDynamicProgramming().longestPalindrome(s))
