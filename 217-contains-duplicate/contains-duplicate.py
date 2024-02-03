class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #If we compare each elements Time: o(nˆ2) Space: o(1)
        #If we do sort then compare Time: o(nlogn) Space: o(1)
        nums1 = sorted(nums)
        for i in range(len(nums1) - 1):
            if nums1[i] == nums1[i + 1]:
                return True
        return False
        
        
        