import unittest
import cap

class Testcap(unittest. Testcase)

    def test_one_word(self):
        text = 'python'
        result = cap
        result = cap.cap_text(text)
        self.assertEqual(result, 'python')

    def test_multiple_words(self):
        text = 'monty python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'python')
if __name__ == '__main__':
    unittest.main()
