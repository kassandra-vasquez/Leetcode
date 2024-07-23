# TC: T: O(n * k log k) - sorting each nwords of max length of k S: O(n * k)
class Solution:
    def groupAnagrams(self, words: List[str]) -> List[List[str]]:
        a_map = defaultdict(list)

        for word in words:
            sorted_word = "".join(sorted(word))
            a_map[sorted_word].append(word)
        return list(a_map.values())
