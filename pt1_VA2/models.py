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


author = 'Yuki Takahashi'

doc = """
Individual round
"""


class Constants(BaseConstants):
    name_in_url = 'pt1_VA2'
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
    # understanding questions
    uq1 = models.IntegerField (
        label = '1. Which of the following statements is true? ',
        widget = widgets.RadioSelect,
        choices = [
            [1, 'In this part, I will work on puzzles individually for 4 minutes and earn € 0.2 for each puzzle I solve.'],
            [2, 'In this part, I will work on puzzles in pairs for 4 minutes and earn € 0.2 for each puzzle we solve.'],
            [3, 'In this part, I will work on the puzzles individually for 4 minutes, but I will not gain anything.'],])
    uq2 = models.IntegerField (
        label = "2. Which of the following puzzles is in the correct order?",
        widget = widgets.RadioSelect,
        choices = [[1, 'A.'], [2, 'B.'],])
    uq3 = models.IntegerField (
        label = '3. What is the strategy to use to solve the puzzle as fast as possible? ',
        widget = widgets.RadioSelect,
        choices = [
            [1, "First, arrange the cells in the left column in the correct order, then those in the bottom row. Always minimize the number of moves you have to make."],
            [2, "First, arrange the cells in the top row in the correct order, then those in the right column. Always minimize the number of moves to make."],
            [3, "First, arrange the cells in the top row in the correct order, then those in the left column. Always minimize the number of moves to make."],])
    uq4 = models.IntegerField (
        label = "4. Look at the following puzzle. What's the right move? ",
        widget = widgets.RadioSelect,
        choices = [[1, 'Move 4 down.'], [2, 'Move 7 to left.'],])
    uq5 = models.IntegerField (
        label = '5. Consider the puzzle in question 4. What is the minimum number of moves to solve the puzzle? ',
        widget = widgets.RadioSelect,
        choices = [[1, '2'], [2, '3'], [3, '4'],])
    uq6 = models.IntegerField (
        label = "6. Look at the following puzzle. What's the right move?",
        widget = widgets.RadioSelect,
        choices = [[1, 'Move the 5 to the left.'], [2, 'Move the 8 up.'],])
    uq7 = models.IntegerField (
        label = '7. Consider the puzzle in question 6. What is the minimum number of moves to solve the puzzle? ',
        widget = widgets.RadioSelect,
        choices = [[1, '2'], [2, '3'], [3, '4'],])

    # error messages
    def uq1_error_message(self, uq1):
        print(uq1)
        if uq1 != 1:
            return self.session.config['uq_error']

    def uq2_error_message(self, uq2):
        print(uq2)
        if uq2 != 2:
            return self.session.config['uq_error']

    def uq3_error_message(self, uq3):
        print(uq3)
        if uq3 != 3:
            return self.session.config['uq_error']

    def uq4_error_message(self, uq4):
        print(uq4)
        if uq4 != 2:
            return self.session.config['uq_error']

    def uq5_error_message(self, uq5):
        print(uq5)
        if uq5 != 3:
            return self.session.config['uq_error']

    def uq6_error_message(self, uq6):
        print(uq6)
        if uq6 != 1:
            return self.session.config['uq_error']

    def uq7_error_message(self, uq7):
        print(uq7)
        if uq7 != 1:
            return self.session.config['uq_error']

    # a function to pass vars for later apps
    def pass_variable(self):
        self.participant.vars['puzzles_solved_pt1'] = self.puzzles_solved_pt1

    # a function to add tentative earnings to the build-in payff variable
    def add_payoff(self):
        self.payoff += round(self.session.config['pt1rate'] * self.puzzles_solved_pt1, 2)
