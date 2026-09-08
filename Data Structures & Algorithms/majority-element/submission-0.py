
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        dictt = Counter(nums)

        for ele in dictt:
            if dictt[ele]>len(nums)/2:
                return ele
        