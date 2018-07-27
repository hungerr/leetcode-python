class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = {}
        for i, num in enumerate(nums):
            if target - num in nums_dict:
                return [nums_dict[target - num], i]
            if num not in nums_dict:
                nums_dict[num] = i


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    s = Solution()
    print s.twoSum(nums, target)
