# BRUTE FORCE
# TC: T: O(n^2) - quadratic/worst S: O(1) - constant/best
def hasDuplicates(self, nums: List[int]) -> bool:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

# OPTIMIZED SOLUTION
# TC: T&S: O(n) - constant/best
def hasDuplicate(self, nums: List[int]) -> bool:
    hashset = set()

    for num in nums:
        if num in hashset:
            return True
        hashset.add(num)
    return False
