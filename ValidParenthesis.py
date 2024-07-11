# BRUTE FORCE
#TC T: O(n) S: O(n)
def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {')':'(', ']':'[', '}':'{'}

        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            if i == ')' or i == ']' or i == '}':
                if len(stack) <= 0:
                    return False
                elif len(stack) > 0 and hashmap[i] != stack.pop():
                    return False

        if len(stack) == 0:
            return True
        else:
            return False


# OPTIMIZED
#TC T: O(n) S: O(n)
def isValid(self, s: str) -> bool:
        stack = []
        pair = dict(('()', '[]', '{}'))

        for i in s:
            if i in "([{":
                stack.append(i)
            elif len(stack) == 0 or i != pair[stack.pop()]:
                return False
        return len(stack) == 0
