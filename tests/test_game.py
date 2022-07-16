from unittest import TestCase, main

from main import get_position_indexes, verify_board_size, verify_input


class GameTest(TestCase):
    positions = [[(1, 1), (0, 0)],
                 [(2, 3), (1, 2)],
                 [(3, 2), (2, 1)],
                 [(100, 100), (99, 99)]
                 ]

    test_sizes = [('a b', False),
                  ('1 2 3', False),
                  ('-1 4', False),
                  ('1 -4', False),
                  ('-1 -4', False),
                  ('0 4', False),
                  ('1 0', False),
                  ('1 1', True),
                  ('100 100', True)]

    test_user_inputs = [('a b', False),
                        ('1 2 3', False),
                        ('6 3', False),
                        ('3 6', False),
                        ('1 1', True),
                        ('2 3', True),
                        ('5 5', True)
                        ]

    def test_get_position_indexes(self):
        for pos in self.positions:
            with self.subTest(pos[0]):
                self.assertEqual(get_position_indexes(pos[0]), pos[1])

    def test_verify_board_size(self):
        for size in self.test_sizes:
            with self.subTest(size):
                self.assertEqual(verify_board_size(size[0]), size[1])

    def test_verify_inputs(self):
        correct_size = (5, 5)
        for usr_input in self.test_user_inputs:
            with self.subTest(usr_input):
                self.assertEqual(verify_input(usr_input[0], correct_size), usr_input[1])


if __name__ == '__main__':
    main()
