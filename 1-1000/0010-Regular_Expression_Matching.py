"""
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
"""


class SolutionClassRecursive:
    def isMatch(self, s, p):
        """
        :param s: String
        :param s: String
        :return: Boolean
        """
        # root case, if the last recursive p is empty then
        # if s not empty, this is not right, return False.
        # if s is empty, then this is right, return True.
        if not p:
            return not s

        # helper, to determine the first car is same in s and p or p is .
        first_matched = bool(s) and (s[0] == p[0] or p[0] == '.')

        # recursive starts.
        # if p has only one char, then we look if first matched, and recurse to p[1:] and s[1:],
        #   in this case p is empty, which is root case
        # if p has two and more char, then
        #   if p has a pattern "a*", second place with a *, then either ignore "a*", recurse to p[2:] and s
        #       or move to compare next s, recurse to s[1:] and p
        #   if p doesn't have that pattern, then
        #       we move to p[1:] and s[1:], in fact, we combine with the first one
        if len(p) >= 2 and p[1] == '*':
            return self.isMatch(s, p[2:]) or (first_matched and self.isMatch(s[1:], p))
        else:
            return first_matched and self.isMatch(s[1:], p[1:])
# Space: O(n)
# Time: O(1)


class SolutionClassDP(object):
    def isMatch(self, text, pattern):
        dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]

        dp[-1][-1] = True
        for i in range(len(text), -1, -1):
            for j in range(len(pattern) - 1, -1, -1):
                first_match = i < len(text) and pattern[j] in {text[i], '.'}
                if j + 1 < len(pattern) and pattern[j + 1] == '*':
                    dp[i][j] = dp[i][j + 2] or first_match and dp[i + 1][j]
                else:
                    dp[i][j] = first_match and dp[i + 1][j + 1]

        return dp[0][0]


if __name__ == "__main__":
    s = "baabbaa"
    p = "baa*b*a."
    print(SolutionClassDP().isMatch(s, p))
    for i in range(0, len(s), 1):
        print(s[i])
