#------------------------------------------------------Question------------------------------------------------------#

# Given two strings, write a method to decide if one is a permutation of the other.

#--------------------------------------------------------Tips--------------------------------------------------------#

# 007 - Of course, you could convert the linked lists to integers, compute the sum, and then convert it back to a new 
#       linked list. If you did this in an interview, your interviewer would likely accept the answer, and then see if 
#       you could do this without converting it to a number and back.
# 084 - There is one solution that is 0(N log N) time. Another solution uses some space, but is O(N) time.
# 122 - Could a hash table be useful?
# 131 - Two strings that are permutations should have the same characters, but in different orders. Can you make the 
#       orders the same?

#-----------------------------------------------Questions_&_Assumptions----------------------------------------------#

# Like in many questions, we should confirm some details with our interviewer. We should understand if the
# permutation comparison is case sensitive. That is: is God a permutation of dog? Additionally, we should
# ask if whitespace is significant. We will assume for this problem that the comparison is case sensitive and
# whitespace is significant. So, "god   " is different from "dog".

# Observe first that strings of different lengths cannot be permutations of each other. There are two easy
# ways to solve this problem, both of which use this optimization.

#-----------------------------------------------------Solution-1-----------------------------------------------------#

# Sort the strings.

# If two strings are permutations, then we know they have the same characters, but in different orders. There­
# fore, sorting the strings will put the characters from two permutations in the same order. We just need to
# compare the sorted versions of the strings.

def checkBySort(s1, s2):
    if len(s1) != len(s2):
        return False
    s1, s2 = sorted(s1), sorted(s2)
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True

# Though this algorithm is not as optimal in some senses, it may be preferable in one sense: It's clean, simple
# and easy to understand. In a practical sense, this may very well be a superior way to implement the problem.

# However, if efficiency is very important, we can implement it a different way.

#-----------------------------------------------------Solution-2-----------------------------------------------------#

# Check if the two strings have identical character counts.

# We can also use the definition of a permutation-two words with the same character counts-to imple­ment
# this algorithm. We simply iterate through this code, counting how many times each character appears.
# Then, afterwards, we compare the two arrays.

def checkByCount(s1, s2):
    if len(s1) != len(s2):
        return False
    counter = [0] * 256
    for c in s1:
        counter[ord(c)] += 1
    for c in s2:
        if counter[ord(c)] == 0:
            return False
        counter[ord(c)] -= 1
    return True

#--------------------------------------------------------Tests-------------------------------------------------------#

import unittest

class Test(unittest.TestCase):
    # s1, s2, isPermutation
    permutations = {
        ("dog", "god", True),
        ("abcd", "bacd", True),
        ("3563476", "7334566", True),
        ("wef34f", "wffe34", True),
        ("dogx", "godz", False),
        ("abcd", "d2cba", False),
        ("2354", "1234", False),
        ("dcw4f", "dcw5f", False),
        ("DOG", "dog", False),
        ("dog ", "dog", False),
        ("aaab", "bbba", False),
    }

    testFunctions = [
        checkBySort,
        checkBySort,
    ]

    def test_cp(self):
        # true check
        for checkPermutation in self.testFunctions:
            for s1, s2, expected in self.permutations:
                assert checkPermutation(s1, s2) == expected

if __name__== "__main__":
    unittest.main()
