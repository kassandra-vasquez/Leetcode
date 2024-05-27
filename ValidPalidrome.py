# BRUTE FORCE
# TC: T: O(n) - linear/fair  S: O(n) - linear/fair
def isPalindrome(self, s: str) -> bool:
    result = ""

    for char in s:
        if char.isalnum():
            result += char
        result = result.lower()
    return result == result[::-1]


# OPTIMIZED
# TC: T:O(n) - linear/fair S:(1) - constant/best
def isPalindrome(self, s: str) -> bool:
    s = s.lower()
    l, r = 0, len(s) - 1

    while l < r:
        if not s[l]. isalnum():
            l += 1
        elif not s[r].isalnum():
            r -= 1
        elif s[l] != s[r]:
            return False
        else:
            l += 1
            r -= 1
    return True
