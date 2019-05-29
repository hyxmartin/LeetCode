"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class SolutionClass(object):
    def two_sum(self, nums, target):
        """
        :param nums:
        :param target:
        :return:
        """
        mapping = {}

        for index, val in enumerate(nums):
            diff = target - val
            if diff in mapping:
                return [index, mapping[diff]]
            else:
                mapping[val] = index

# Space: O(N)
# Time: O(N)


if __name__ == "__main__":
    arr = [2, 7, 11, 15]
    tar = 9
    print(SolutionClass().two_sum(arr, tar))
