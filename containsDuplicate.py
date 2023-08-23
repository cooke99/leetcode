class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums_set = set(nums) # Set contains only unique elements

        if (len(nums) != len(nums_set)):
            # If the length of the set != length of array, there is a duplicate
            # element in the array
            return True
        
        else:
            return False
