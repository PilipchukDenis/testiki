# Создайте класс, содержащий набор целых чисел.
# В классе должна быть реализована следующая функциональность:
# ■ Сумма элементов набора.
# ■ Среднеарифметическое элементов набора.
# ■ Максимум из элементов набора.
# ■ Минимум из элементов набора.
# Протестируйте все возможности созданного класса
# с помощью модульного тестирования(unittest).


# import unittest
# from main import IntegerSet
#
#
# import unittest
#
# class TestIntegerSet(unittest.TestCase):
#
#     def setUp(self):
#         """
#         Выполняется перед каждым тестом. Подготавливает тестовые данные.
#         """
#         self.int_set = IntegerSet([1, 2, 3, 4, 5])
#         self.empty_set = IntegerSet([])
#
#     def test_sum(self):
#         """Тестирует функцию sum()."""
#         self.assertEqual(self.int_set.sum(), 15)
#
#     def test_average(self):
#         """Тестирует функцию average()."""
#         self.assertEqual(self.int_set.average(), 3.0)
#
#     def test_maximum(self):
#         """Тестирует функцию maximum()."""
#         self.assertEqual(self.int_set.maximum(), 5)
#
#     def test_minimum(self):
#         """Тестирует функцию minimum()."""
#         self.assertEqual(self.int_set.minimum(), 1)
#
#     def test_empty_set(self):
#         """
#         Тестирует реакции на пустой набор для функций,
#         которым требуется хотя бы один элемент.
#         """
#         with self.assertRaises(ValueError):
#             self.empty_set.sum()
#
#         with self.assertRaises(ValueError):
#             self.empty_set.average()
#
#         with self.assertRaises(ValueError):
#             self.empty_set.maximum()
#
#         with self.assertRaises(ValueError):
#             self.empty_set.minimum()
#
#     def test_non_integer_values(self):
#         """
#         Тестирует создание набора с некорректными элементами.
#         Ожидается исключение ValueError.
#         """
#         with self.assertRaises(ValueError):
#             IntegerSet([1, 2, "три", 4])
#
# if __name__ == '__main__':
#     unittest.main()



 # 2 Создайте класс для числа. В классе должна быть реализована следующая функциональность:

# ■ Перевод числа в восьмеричную систему исчисления.
# ■ Перевод числа в шестнадцатеричную систему исчисления.
# ■ Перевод числа в двоичную систему исчисления.
# Протестируйте все возможности созданного класса
# с помощью модульного тестирования(unittest).

#
#
# from main import NumberConverter
# import unittest
#
#
# class TestNumberConverter(unittest.TestCase):
#
#     def test_to_octal(self):
#         converter = NumberConverter(10)  # Десятичное число 10.
#         self.assertEqual(converter.to_octal(), '0o12')  # В восьмеричной: 12.
#
#     def test_to_hexadecimal(self):
#         converter = NumberConverter(255)  # Десятичное число 255.
#         self.assertEqual(converter.to_hexadecimal(), '0xff')  # В шестнадцатеричной: ff.
#
#     def test_to_binary(self):
#         converter = NumberConverter(5)  # Десятичное число 5.
#         self.assertEqual(converter.to_binary(), '0b101')  # В двоичной: 101.
#
#     def test_negative_number(self):
#         converter = NumberConverter(-10)  # Отрицательное число -10.
#         self.assertEqual(converter.to_octal(), '-0o12')  # Восьмеричная: -12
#         self.assertEqual(converter.to_hexadecimal(), '-0xa')  # Шестнадцатеричная: -a.
#         self.assertEqual(converter.to_binary(), '-0b1010')  # Двоичная: -1010.
#
#     def test_invalid_input(self):
#         with self.assertRaises(ValueError):
#             NumberConverter("abc")  # Передано не целое число.
#
#
# if __name__ == '__main__':
#     unittest.main()
#
