'''
    check permutation:
    give 2 strings, write a method to decide if one is a permutation of the other
'''

class Solution:
    def checkPermutation(self, s1: str, s2: str) -> bool:
        '''
            sort 2 string, check if them are same after sorted

            sort will make rt: O(nlogn), space O(1)
        '''

        s1 = sorted(s1)
        s2 = sorted(s2)

        if s1 == s2:
            return True
        else:
            return False

    def checkPermutation_2(self, s1: str, s2: str) -> bool:
        '''
            have same char count
            can use dict or char array (char array need to assume char set - ascii, ascii-ext, unicode)
        '''

        # s1 s2 should have same length
        if len(s1) != len(s2): return False

        dic = {}
        for c in s1:
            dic[c] = dic.get(c, 0) + 1

        for c in s2:
            dic[c] = dic.get(c, 0) - 1

        for k, v in dic.items():
            if v != 0:
                return False
        return True
        

if __name__ == "__main__":
    c = Solution()
    ans = c.checkPermutation_2("qpwoeiruty", "trewqyuiop")
    ans_2 = c.checkPermutation_2("qpwoeirutys", "trewqyuiopa")
    print(ans, ans_2)