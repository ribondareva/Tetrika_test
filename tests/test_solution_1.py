import unittest
from task1.solution_1 import sum_two


class TestStrictDecorator(unittest.TestCase):

    def test_correct_arguments(self):
        self.assertEqual(sum_two(1, 2), 3)

    def test_type_error_positional(self):
        with self.assertRaises(TypeError) as context:
            sum_two(1, 2.0)
        self.assertIn("Аргумент b ожидает int", str(context.exception))

    def test_type_error_keyword(self):
        with self.assertRaises(TypeError) as context:
            sum_two(a=1, b="2")
        self.assertIn("Аргумент b ожидает int", str(context.exception))

    def test_extra_keyword_argument(self):
        with self.assertRaises(TypeError):
            sum_two(a=1, b=2, c=3)


if __name__ == '__main__':
    unittest.main()
