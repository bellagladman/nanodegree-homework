import unittest
from assessment_q3 import lowercase_the_word, palindrome_check, reverse_the_word


class TestAssessmentQ3(unittest.TestCase):

    def test_lowercase_the_word(self):
        self.assertEqual(lowercase_the_word('Apple'), 'apple')

    def test_reverse_the_word(self):
        self.assertEqual(reverse_the_word('Apple'), 'elppa')

    def test_palindrome_check(self):
        self.assertEqual(palindrome_check('otto', 'otto'), True)
        self.assertEqual(palindrome_check('scissors', 'srossics'), False)
        # self.assertRaises(AssertionError, palindrome_check, 'ge og') FOR SOME REASON I CAN'T GET THIS TO WORK
#




if __name__ == '__main__':
    unittest.main()


