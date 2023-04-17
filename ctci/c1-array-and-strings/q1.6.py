'''
    implement a method to perform basic string compression using the counts of repeated characters.
    For example, the string aabcccccaaa would become a2b1c5a3.
    If the "compressed" string would not become smaller than the original string, your method should return the original string.
    You can assume the string has only uppercase and lowercase letters (a - z).
'''

class Solution:
    def compress(self, s: str) -> str:
        '''
            1. check if compressed string is shorter than original string
            2. compress string
        '''
        compressed = self.compressString(s)
        if len(compressed) >= len(s):
            return s
        return compressed
    
    def compressString(self, s: str) -> str:
        if not s:
            return s

        compressed = []
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                compressed.append(s[i - 1])
                compressed.append(str(count))
                count = 1

        compressed.append(s[-1])
        compressed.append(str(count))

        return ''.join(compressed)

# test cases
def test_solution():
    solution = Solution()
    test_cases = [
        ("aabcccccaaa", "a2b1c5a3"),
        ("abcde", "abcde"),
        ("", ""),
        ("aabbcc", "aabbcc"),
        ("aaabbbccc", "a3b3c3"),
        ("aabcc", "aabcc"),
        ("aabb", "aabb"),
        ("aaab", "aaab"),
        ("aaaabbbb", "a4b4"),
        ("cccccccaaa", "c7a3"),
        ("cccaaaaccc", "c3a4c3"),
        ("cc", "cc"),
        ("ccc", "c3"),
        ("cccc", "c4"),
        ("cccccc", "c6"),
        ("ccccccc", "c7"),
        ("cccccccc", "c8"),
        ("a", "a"),
        ("aa", "aa"),
        ("aaa", "a3"),
        ("aaabbbbcccccddddeeeeefffff", "a3b4c5d4e5f5"),
        ("a" * 10000 + "b" * 9999, "a10000b9999"),
        ("aaaAAAbbBBccC", "a3A3b2B2c2C1"),
        ("zyxwvutsrqponmlkjihgfedcba", "zyxwvutsrqponmlkjihgfedcba"),
        ("a" * 1000 + "b" * 1000 + "c" * 1000, "a1000b1000c1000"),
        ("q" * 100 + "p" * 50 + "o" * 25 + "n" * 13, "q100p50o25n13"),
        ("a" * 20 + "b" * 20 + "c" * 20 + "d" * 20 + "e" * 20 + "f" * 20 + "g" * 20 + "h" * 20 + "i" * 20 + "j" * 20, "a20b20c20d20e20f20g20h20i20j20")
    ]

    for s, expected in test_cases:
        result = solution.compress(s)
        assert result == expected, f"Expected {expected}, but got {result}. Input: {s}"

test_solution()
