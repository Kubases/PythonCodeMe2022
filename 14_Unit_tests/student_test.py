import unittest
from student import Student


class TestStudent(unittest.TestCase):
    def setUp(self):
        print('---setUp---')

    def tearDown(self):
        print('---tearDown---')

    @classmethod
    def setUpClass(cls):
        print('~~~~setUp~~~~')

    @classmethod
    def tearDownClass(cls):
        print('~~~~tearDown~~~~')

    def test_email(self):
        ex_student = Student('Johny', 'Depp', 4.7, None)
        self.assertEqual(ex_student.email, 'johny.depp@university.com')

        ex_student.last = 'Targaryen'
        self.assertEqual(ex_student.email, 'johny.targaryen@university.com')

    def test_fullname(self):
        ex_student = Student('Johny', 'Depp', 4.7, None)
        self.assertEqual(ex_student.fullname, 'Johny Depp')

    def test_grant_scholarship_successful(self):
        ex_student = Student('Johny', 'Depp', 5, None)
        ex_student.grant_scholarship()
        self.assertTrue(ex_student.scholarship)

    def test_grant_scholarship_unsuccessful(self):
        ex_student = Student('Johny', 'Depp', 3, None)
        ex_student.grant_scholarship()
        self.assertFalse(ex_student.scholarship)


if __name__ == '__main__':
    unittest.main()
