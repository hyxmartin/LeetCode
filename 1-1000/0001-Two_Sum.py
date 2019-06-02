"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class SolutionClass1(object):
    def twoSum(self, nums, target):
        """
        :param nums: List[int]
        :param target: int
        :return: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums), 1):
                if nums[j] == target - nums[i]:
                    return [i, j]

# Space: O(1)
# Time: O(N^2)


class SolutionClassFinal(object):
    def twoSum(self, nums, target):
        """
        :param nums: List[int]
        :param target: int
        :return: List[int]
        saved in a dict[value:pos] and look if a value have saved that equals target - current value
        if not save into dict
        if yes return current and the saved position
        """
        mapping = {}
        for i in range(len(nums)):
            if target - nums[i] not in mapping:
                mapping[nums[i]] = i
            else:
                return [mapping[target - nums[i]], i]
        return []
# Space: O(N)
# Time: O(N)


if __name__ == "__main__":
    arr = [2, 7, 11, 15]
    tar = 17
    print(SolutionClassFinal().twoSum(arr, tar))
