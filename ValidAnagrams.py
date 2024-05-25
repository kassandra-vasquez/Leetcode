# BRUTE FORCE
# TC: T&S: O(n!) - factorial/worst
from itertools import permutations
def isAnagram(self, s: str, t: str) -> bool:
    perms = [''.join(p) for p in permutations(s)]
    return t in perms

# OPTIMIZED OK
# TC: T: O(n log n) - loglinear/bad S: O(n) - linear/fair
def isAnagram(self, s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

# OPTIMIZED BETTER
# TC: T&S: O(n) - linear/fair
def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    Scount, Tcount = {}, {}

    for index in range(len(s)):
        Scount[s[index]] = 1 + Scount.get(s[index], 0)
        Tcount[t[index]] = 1 + Tcount.get(t[index], 0)

    for count in Scount:
        if Scount[count] != Tcount.get(count, 0):
            return False
    return True
