from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)



doc = """
Individual round slider task
"""


class Constants(BaseConstants):
    name_in_url = 'slider_task'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # define puzzles to play
    def puzzle_to_play(self, formatting):
        my_boards = [
            [[1, 2, 3], [4, 5, 6], [7, None, 8]],
            [[1, 2, 3], [4, None, 5], [7, 8, 6]],
            [[1, 2, 3], [4, 6, None], [7, 5, 8]],
            [[None, 2, 3], [1, 4, 5], [7, 8, 6]],
            [[1, 3, 6], [4, 2, None], [7, 5, 8]],
            [[1, 2, 3], [7, 4, 6], [5, 8, None]],
            [[1, 2, 3], [7, 4, None], [5, 8, 6]],
            [[2, 5, 3], [1, 7, 6], [4, 8, None]],
            [[4, 1, 3], [7, 2, None], [8, 6, 5]],
            [[None, 1, 3], [5, 2, 7], [4, 8, 6]],
            [[2, None, 6], [1, 3, 8], [4, 5, 7]],
            [[4, 1, None], [8, 3, 2], [5, 7, 6]],
            [[1, 5, 2], [None, 7, 6], [3, 4, 8]],
            [[2, 3, 8], [7, 1, 4], [None, 6, 5]],
            [[2, 7, 3], [5, 1, None], [4, 8, 6]],
        ]
        if formatting == 0:  # returns board
            return my_boards
        if formatting == 1:  # returns string
            my_boards_str = []
            for k in range(0, 15):
                my_puzzle_str = ''
                for i in range(0, 3):
                    for j in range(0, 3):
                        my_puzzle_str = my_puzzle_str + str(my_boards[k][i][j])
                my_puzzle_str = my_puzzle_str.replace('None', '_')
                my_boards_str.append(my_puzzle_str)
            return my_boards_str

    # puzzle info
    puzzles_solved_pt1 = models.IntegerField()
    puzzle_histories = models.LongStringField()

    # a function to pass vars for later apps
    def pass_variable(self):
        self.participant.vars['puzzles_solved_pt1'] = self.puzzles_solved_pt1

    # a function to add tentative earnings to the build-in payff variable
    def add_payoff(self):
        self.payoff += round(self.session.config['pt1rate'] * self.puzzles_solved_pt1, 2)
