class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_set = set()

        for ele in nums:
            
            if ele in new_set:
                return True
            new_set.add(ele)
        return False

        