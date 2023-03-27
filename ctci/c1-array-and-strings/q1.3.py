from typing import List

'''
    URLify
    replace all spaces in a string with '%20', you can assume the string have enough space at the end to hold the additional characters 
'''

class Solution:
    def replaceSpace(self, s: List[str], trueLength: int) -> None:
        '''
            go backwards, swap char to new index, and replace space char with '%20'
        '''
        numOfSpace: int = self.countSpace(s, trueLength)
        # origin string tail, and +2 extra char when replace space to '%20'
        new_index: int = trueLength - 1 + numOfSpace * 2

        for old_index in reversed(range(trueLength)):
            # old index loop from string tail (true tail) to head
            # new index start from end of given space, backward don't worry about overwrite
            if s[old_index] == ' ':
                s[new_index] = '0'
                s[new_index - 1] = '2'
                s[new_index - 2] = '%'
                new_index -= 3
            else:
                s[new_index] = s[old_index]
                new_index -= 1

    def countSpace(self, s: List[str], trueLength: int) -> int:
        ans: int = 0
        for i in range(trueLength):
            if s[i] == ' ':
                ans += 1
        return ans

if __name__ == "__main__":
    c = Solution()
    s = list("Mr John Smith    ")
    c.replaceSpace(s, 13)
    print(''.join(s))