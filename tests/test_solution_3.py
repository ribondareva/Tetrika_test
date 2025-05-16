import unittest
from task3.solution_3 import appearance


class TestAppearance(unittest.TestCase):
    def test_case_1(self):
        intervals = {
            'lesson': [1594663200, 1594666800],
            'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
            'tutor': [1594663290, 1594663430, 1594663443, 1594666473]
        }
        self.assertEqual(appearance(intervals), 3117)

    def test_case_2(self):
        intervals = {
            'lesson': [1594702800, 1594706400],
            'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513,
                      1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009,
                      1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773,
                      1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503,
                      1594706524, 1594706524, 1594706579, 1594706641],
            'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]
        }
        self.assertEqual(appearance(intervals), 3577)

    def test_case_3(self):
        intervals = {
            'lesson': [1594692000, 1594695600],
            'pupil': [1594692033, 1594696347],
            'tutor': [1594692017, 1594692066, 1594692068, 1594696341]
        }
        self.assertEqual(appearance(intervals), 3565)

    def test_no_overlap(self):
        """Ученик и преподаватель не пересекались вообще"""
        intervals = {
            'lesson': [1000, 5000],
            'pupil': [1000, 2000],
            'tutor': [3000, 4000]
        }
        self.assertEqual(appearance(intervals), 0)

    def test_pupil_absent(self):
        """Ученик отсутствует"""
        intervals = {
            'lesson': [1000, 5000],
            'pupil': [],
            'tutor': [1000, 5000]
        }
        self.assertEqual(appearance(intervals), 0)

    def test_tutor_absent(self):
        """Преподаватель отсутствует"""
        intervals = {
            'lesson': [1000, 5000],
            'pupil': [1000, 5000],
            'tutor': []
        }
        self.assertEqual(appearance(intervals), 0)

    def test_both_absent(self):
        """Оба отсутствуют"""
        intervals = {
            'lesson': [1000, 5000],
            'pupil': [],
            'tutor': []
        }
        self.assertEqual(appearance(intervals), 0)

    def test_exact_lesson_bounds(self):
        """Оба находятся от начала до конца урока"""
        intervals = {
            'lesson': [1000, 5000],
            'pupil': [1000, 5000],
            'tutor': [1000, 5000]
        }
        self.assertEqual(appearance(intervals), 4000)

    def test_outside_lesson_bounds(self):
        """Интервалы выходят за рамки урока — должны обрезаться"""
        intervals = {
            'lesson': [1000, 5000],
            'pupil': [900, 5100],
            'tutor': [950, 5050]
        }
        self.assertEqual(appearance(intervals), 4000)


if __name__ == '__main__':
    unittest.main()
