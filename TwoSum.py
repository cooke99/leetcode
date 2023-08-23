class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_dict = {}
        for idx, val in enumerate(nums):
            diff_dict[target - val] = idx

        for idx,val in enumerate(nums):
            idx2 = diff_dict.get(val,None)
            if (idx2 is None):
                continue
            elif (idx == idx2):
                continue
            else:
                return [idx, idx2]