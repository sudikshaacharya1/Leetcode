class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashset = set()

        for i in nums:
            if i in hashset:
                hashset.discard(i)
            else:
                hashset.add(i)

        # After the loop, there should be only one element in the set
        # Return that element
        return hashset.pop()