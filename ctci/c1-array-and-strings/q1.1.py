'''
check if all characters in a string are unique.
follow up: don't use any extra data structure
'''

class Solution:
    def isUnique(self, s: str) -> bool:
        # check string is ascii 
        if len(s) > 128: return False
        # use a bool array
        char_set = [False for i in range(128)]
        for c in s:
            ci = ord(c)
            if char_set[ci] is True:
                return False
            else:
                char_set[ci] = True
        return True

    def isUnique_2(self, s: str) -> bool:
        checker = 0
        for c in s:
            offset = ord(c) - ord('a')
            if checker & (1 << offset) > 0:
                return False
            checker |= 1 << offset
        return True

    def isUnique_followup(self, s: str) -> bool:
        '''
            *no extra data structure or space
            1. for each char check whole str, O(n^2)
            2. sort
        '''
        s = sorted(s)
        for i in range(len(s)):
            if i+1 >= len(s):
                break
            if s[i] == s[i+1]:
                return False
        return True

if __name__ == "__main__":
    c = Solution()
    ans = c.isUnique_followup("asdaghjkl")
    print(ans)