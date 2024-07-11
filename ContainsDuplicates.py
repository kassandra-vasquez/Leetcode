# BRUTE FORCE
# TC: T: O(n^2) S: O(1)
def hasDuplicates(self, nums: List[int]) -> bool:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False


# OPTIMIZED SOLUTION
# TC: T&S: O(n) 
def hasDuplicate(self, nums: List[int]) -> bool:
    hashset = set()

    for num in nums:
        if num in hashset:
            return True
        hashset.add(num)
    return False
