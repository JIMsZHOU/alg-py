'''
    given a string, write a function to check if it is a permutation of a palindrome
    palindrome: a world of phrase that is the same forwards and backwards

    not limited to dictionary words and not case sensitive and non-letter characters are ignored
    input: Tact Coa (permutation: taco cat, atco cta, etc)
'''

class Solution:
    def isPermutationOfPalindrome(self, s: str) -> bool:
        '''
         break down the question:
         1. palindrome is a word or phrase that is the same forward and backwards
         2. permutation is a rearrangement of letters
         depending on above, the input string should have below characteristics:
         1. for even number of characters, all characters should appear even number of times
         2. for odd number of characters, all characters should appear even number of times except one character
        '''

        # covert input to lower case
        s = s.lower()

        # build dictionary of character counts
        charCount = {}

        for c in s:
            if not c.isalpha():
                continue
            charCount[c] = charCount.get(c, 0) + 1

        # check if all characters appear even number of times
        oddCount = 0
        for c in charCount.values():
            if c % 2 == 1:
                oddCount += 1
            if oddCount > 1:
                return False
        
        return True
    
    def isPermutationOfPalindrome_2(self, s: str) -> bool:
        '''
            solution2:
            use bit vector to reduce space complexity
        '''

        def toggle(bitVector, index) -> int:
            if index < 0:
                return bitVector
            mask = 1 << index
            bitVector ^= mask # xor to toggle bit
            return bitVector
        
        def createBitVector(s: str) -> int:
            bitVector = 0
            for c in s:
                if c.isalpha():
                    x = ord(c) - ord('a') # get index of character
                    bitVector = toggle(bitVector, x)
            return bitVector
        
        def checkExactlyOneBitSet(bitVector: int) -> bool:
            return (bitVector & (bitVector - 1)) == 0
        
        bitVector = createBitVector(s)
        return bitVector == 0 or checkExactlyOneBitSet(bitVector)