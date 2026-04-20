class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n   # handle large k

        # Step 1: reverse whole array
        nums.reverse()

        # Step 2: reverse first k elements
        nums[:k] = reversed(nums[:k])

        # Step 3: reverse remaining elements
        nums[k:] = reversed(nums[k:])
