from unittest import TestCase, main

from main import get_position_indexes, verify_board_size, verify_input, Game


class GameTest(TestCase):

    def test_get_position_indexes(self):
        positions = [[(1, 1), (0, 0)],
                     [(2, 3), (1, 2)],
                     [(3, 2), (2, 1)],
                     [(100, 100), (99, 99)]
                     ]

        for pos in positions:
            with self.subTest(pos[0]):
                self.assertEqual(get_position_indexes(pos[0]), pos[1])

    def test_verify_board_size(self):
        test_sizes = [('a b', False),
                      ('1 2 3', False),
                      ('-1 4', False),
                      ('1 -4', False),
                      ('-1 -4', False),
                      ('0 4', False),
                      ('1 0', False),
                      ('1 1', True),
                      ('100 100', True)]

        for size in test_sizes:
            with self.subTest(size):
                self.assertEqual(verify_board_size(size[0]), size[1])

    def test_verify_inputs(self):
        test_user_inputs = [('a b', False),
                            ('1 2 3', False),
                            ('6 3', False),
                            ('3 6', False),
                            ('1 1', True),
                            ('2 3', True),
                            ('5 5', True)
                            ]
        correct_size = (5, 5)
        for usr_input in test_user_inputs:
            with self.subTest(usr_input):
                self.assertEqual(verify_input(usr_input[0], correct_size), usr_input[1])

    def test_game_init(self):
        board = [(6, 5), (3, 4), (2, 2), (10, 10)]
        for size in board:
            game = Game(size)
            with self.subTest(size):
                self.assertEqual(len(game.matrix), size[1])
                self.assertEqual(len(game.matrix[0]), size[0])
                self.assertEqual(game.matrix[0][0], '_' * len(str((size[0] * size[1]))))
            del game


if __name__ == '__main__':
    main()
