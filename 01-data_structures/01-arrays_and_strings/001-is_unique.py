#------------------------------------------------------Question------------------------------------------------------#

# Implement an algorithm to determine if a string has all unique characters. What if you cannot use 
# additional data structures?

#--------------------------------------------------------Tips--------------------------------------------------------#

# 044 - try a hash table
# 117 - bit vector?
# 132 - try solve in O(n log n)

#-----------------------------------------------Questions_&_Assumptions----------------------------------------------#

# You should first ask your interviewer if the string is an ASCII string or a Unicode string. Asking this question
# will show an eye for detail and a solid foundation in computer science. We'll assume for simplicity the char­
# acter set is ASCII. If this assumption is not valid, we would need to increase the storage size.

#------------------------------------------------------Solution------------------------------------------------------#

def unique(string):
    # Assuming character set is ASCII (128 characters)
    if len(string) > 128:
        return False

    char_set = [False for _ in range(128)]
    for char in string:
        val = ord(char)
        if char_set[val]:
            # char already found in string
            return False
        char_set[val] = True

    return True

#--------------------------------------------------------Tests-------------------------------------------------------#

import unittest

class Test(unittest.TestCase):
    dataTrue = [('abcd'), ('s4fad'), ('')]
    dataFail = [('23ds2'), ('hb 627jh=j ()'), ('asdfa')]

    def test_unique(self):
        # true check
        for test_string in self.dataTrue:
            actual = unique(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataFail:
            actual = unique(test_string)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()
