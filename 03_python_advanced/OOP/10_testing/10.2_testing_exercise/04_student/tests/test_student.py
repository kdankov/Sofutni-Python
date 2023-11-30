from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):

    def setUp(self):
        self.student_1 = Student('Student 1', {'Python': ['n1', 'n2', 'n3'], 'JS': ['n1', 'n2']})
        self.student_2 = Student('Student 2')

    def test_init_with_initial_courses(self):
        self.assertEqual('Student 1', self.student_1.name)
        self.assertEqual({'Python': ['n1', 'n2', 'n3'], 'JS': ['n1', 'n2']}, self.student_1.courses)

    def test_init_without_initial_courses(self):
        self.assertEqual('Student 2', self.student_2.name)
        self.assertEqual({}, self.student_2.courses)

    def test_enroll_if_the_course_is_already_enrolled(self):
        result = self.student_1.enroll('Python', ['n4', 'n5'], add_course_notes='N')

        self.assertEqual('Course already added. Notes have been updated.', result)
        self.assertEqual({'Python': ['n1', 'n2', 'n3', 'n4', 'n5'], 'JS': ['n1', 'n2']}, self.student_1.courses)

    def test_enroll_if_the_course_does_not_exist(self):
        result = self.student_1.enroll('C#', ['n1', 'n2'], add_course_notes='Y')

        self.assertTrue('C#' in self.student_1.courses)
        self.assertEqual('Course and course notes have been added.', result)
        self.assertEqual(['n1', 'n2'], self.student_1.courses['C#'])

    def test_enroll_if_the_course_does_not_exists_with_empty_string(self):
        result = self.student_1.enroll('C#', ['n1', 'n2'], add_course_notes='')

        self.assertTrue('C#' in self.student_1.courses)
        self.assertEqual('Course and course notes have been added.', result)
        self.assertEqual(['n1', 'n2'], self.student_1.courses['C#'])

    def test_add_new_course_without_adding_notes(self):
        result = self.student_1.enroll('C#', ['n1', 'n2'], 'N')

        self.assertTrue('C#' in self.student_1.courses)
        self.assertEqual('Course has been added.', result)
        self.assertEqual([], self.student_1.courses['C#'])

    def test_add_notes_if_course_does_not_exist_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student_1.add_notes('C#', ['n1', 'n2'])

        expected = 'Cannot add notes. Course not found.'

        self.assertEqual(expected, str(ex.exception))

    def test_add_notes_if_course_exists(self):
        result = self.student_1.add_notes('Python', ['n4', 'n5'])

        self.assertEqual('Notes have been updated', result)

    def test_leave_course_if_course_does_not_exists_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student_1.leave_course('C#')

        expected = 'Cannot remove course. Course not found.'

        self.assertEqual(expected, str(ex.exception))

    def test_leave_course_if_course_exists(self):
        result = self.student_1.leave_course('JS')

        self.assertEqual('Course has been removed', result)
        self.assertNotIn('JS', self.student_1.courses)


if __name__ == '__main__':
    main()
