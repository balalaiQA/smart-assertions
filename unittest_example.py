import unittest
from smart_assertions import soft_assert, verify_expectations


class UnittestExample(unittest.TestCase):

    def test_positive(self):
        soft_assert('one' == 'one')
        soft_assert(3 == 3, 'Custom message if test failed')
        soft_assert(lambda: self.assertEqual(2, 2), 'Message, that will not written')
        soft_assert(lambda: self.assertGreater(2, 1), 'Message, that will not written')
        soft_assert([0, 1] == [0, 1])
        soft_assert(1 == 1)
        verify_expectations()

    def test_negative(self):
        soft_assert('one' == 'two')
        soft_assert('one' == 'two', '{} != {}'.format('one', 'two'))
        soft_assert(1 == 2)
        soft_assert(2 == 3, 'Custom message if test failed')
        soft_assert(lambda: self.assertEqual(3, 4), 'Your custom message; 3 != 4')
        soft_assert(lambda: self.assertGreater(4, 5))
        soft_assert([6, 7] == [8, 9], 'Lists not equals')
        verify_expectations()

    def test_mixed(self):
        soft_assert(1 == 1)
        soft_assert(2 == 3, 'Custom message if test failed')
        soft_assert([0, 1] == [0, 1])
        soft_assert([6, 7] == [8, 9], 'Lists not equals')
        soft_assert(lambda: self.assertGreater(2, 1), "Message, that will not written")
        soft_assert(lambda: self.assertGreater(4, 5), 'Your custom message; 4 < 5!')
        soft_assert('one' == 'one')
        soft_assert('one' == 'two', '{} != {}'.format('one', 'two'))
        verify_expectations()

    def test_loop_example(self):
        for number in range(1, 10):
            soft_assert(number % 2 == 0, '{} is not divisible by 2 without remainder!'.format(number))
        verify_expectations()
