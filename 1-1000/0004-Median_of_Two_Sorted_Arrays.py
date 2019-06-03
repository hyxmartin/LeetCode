"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""


class SolutionClassFinal:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :param nums1: list[int]
        :param nums2: list[int]
        :return: float
        """
        for i in nums1:
            nums2.append(i)
        nums2.sort()
        length = len(nums2)
        if length % 2 == 0:
            median = (nums2[length // 2 - 1] + nums2[length // 2]) / 2
        else:
            median = nums2[length // 2]
        return median
# Space: O(1)
# Time: O(N)


if __name__ == "__main__":
    nums1 = [1, 2, 3]
    nums2 = [5, 6, 4]
    print(SolutionClassFinal().findMedianSortedArrays(nums1, nums2))
