class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k %= len(nums)
        nums1 = nums[:-k]
        nums2 = nums[-k:]

        nums2.extend(nums1)

        nums[:]=nums2
        