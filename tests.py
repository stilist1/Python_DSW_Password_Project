import unittest
from funcs import generatePassword 


class TestPasswordGenerator(unittest.TestCase):

    def test_generate_valid_password(self):
        length = 10
        password = generatePassword(length)  
        self.assertEqual(len(password), length)

    def test_generate_invalid_length_low(self):
        length = 0
        with self.assertRaises(ValueError): 
            generatePassword(length)

    def test_generate_invalid_length_high(self):
        length = 30
        with self.assertRaises(ValueError): 
            generatePassword(length)


if __name__ == '__main__':
    unittest.main()
