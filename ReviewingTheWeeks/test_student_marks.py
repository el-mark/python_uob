from unittest import TestCase
import ReviewingTheWeeks.student_marks_v2 as student_marks_v2

class TestClass(TestCase):

    def test_split_data(self):
        assert student_marks_v2.split_data() == [['Ann Smith', 51, 60, 80], ['Derek Jones', 12, 49, 90], ['Hannah Qui', 55, 90, 85],['Anya Lopez', 55, 60, 75]]
#assert is an aid to debugging - if the condition is true it passes the test