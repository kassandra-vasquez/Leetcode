# ARRAYS AND HASHING

# BRUTE FORCE
# TC: T: O(n^2) S: O(n)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        if not 0 in nums:
            d = prod(nums)
            for i in nums:
                res.append(int(d/i))
        else:
            for i in range(len(nums)):
                p = 1
                for j in range(len(nums)):
                    if i != j:
                        p *= nums[j]
                res.append(p)
        return res
