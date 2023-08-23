class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_dict = {}
        for idx, val in enumerate(nums):
            # We store the desired sum partner for each number in the array in a dictionary as a key
            # O(n)
            diff_dict[target - val] = idx

        for idx,val in enumerate(nums):
            # Iterate over the array and use .get to see if there's a match in the dict - which is O(1)
            # O(n)*O(1) = O(1)
            idx2 = diff_dict.get(val,None)
            if (idx2 is None):
                continue
            elif (idx == idx2):
                continue
            else:
                return [idx, idx2]