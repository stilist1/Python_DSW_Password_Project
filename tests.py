import unittest
from funcs import generatePassword  # Предполагается, что функция generatePassword импортируется из funcs.py


class TestPasswordGenerator(unittest.TestCase):

    # Тест на генерацию пароля с корректной длиной
    def test_generate_valid_password(self):
        length = 10
        password = generatePassword(length)  # Вызываем функцию для генерации пароля

        # Проверяем, что длина пароля соответствует введенной
        self.assertEqual(len(password), length)

    # Тест на генерацию пароля с некорректной длиной (меньше 1)
    def test_generate_invalid_length_low(self):
        length = 0
        with self.assertRaises(ValueError):  # Ожидаем, что будет выброшено исключение
            generatePassword(length)

    # Тест на генерацию пароля с некорректной длиной (больше 25)
    def test_generate_invalid_length_high(self):
        length = 30
        with self.assertRaises(ValueError):  # Ожидаем, что будет выброшено исключение
            generatePassword(length)


if __name__ == '__main__':
    unittest.main()
