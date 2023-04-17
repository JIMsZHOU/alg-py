'''
    There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. 
    Given two strings, write a function to check if they are one edit (or zero edits) away.
    EXAMPLE
    pale, ple -> true
    pales, pale -> true
    pale, bale -> true
    pale, bake -> false
'''

class Solution:
    def isOneEditAway(self, s1: str, s2: str) -> bool:
        '''
            break down the question:
            1. 3 types of edit, insert, remove, replace
            2. insert and remove means the length of 2 string are different
            3. replace means 2 string have same length
            4. insert and remove can see as same, shorter insert 1 char become longer
        '''

        if abs(len(s1) - len(s2)) > 1:
            # mean absolutely can't finish in 1 edit
            return False
        
        if len(s1) == len(s2):
            return self.isOneReplaceAway(s1, s2)
        
        return self.isOneInsertAway(s1, s2)
    
    def isOneReplaceAway(self, s1: str, s2: str) -> bool:
        '''
            check if 2 string are one replace away
        '''
        diffCount = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diffCount += 1
            if diffCount > 1:
                return False
        return True
    
    def isOneInsertAway(self, s1: str, s2: str) -> bool:
        '''
            check if 2 string are one insert away
        '''
        # make sure s1 is shorter
        if len(s1) > len(s2):
            s1, s2 = s2, s1
        
        # check if s1 is substring of s2
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                return s1[i:] == s2[i+1:]
        return True