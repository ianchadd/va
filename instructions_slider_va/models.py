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
import random


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'Introduction'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    # def creating_session(self):
    pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass 
    # uq2 = models.IntegerField (
    #     label = "1. Which of the following puzzles is in the correct order?",
    #     widget = widgets.RadioSelect,
    #     choices = [[1, 'A.'], [2, 'B.'],])
    # uq3 = models.IntegerField (
    #     label = '2. What is the correct strategy to use to solve the puzzle as fast as possible? ',
    #     widget = widgets.RadioSelect,
    #     choices = [
    #         [1, "First arrange the cells in the left column in the correct order, then those in the bottom row. Always minimize the number of moves you make."],
    #         [2, "First arrange the cells in the top row in the correct order, then those in the right column. Always minimize the number of moves make."],
    #         [3, "First arrange the cells in the top row in the correct order, then those in the left column. Always minimize the number of moves make."],])
    # uq4 = models.IntegerField (
    #     label = "3. Look at the following puzzle. What's the correct move? ",
    #     widget = widgets.RadioSelect,
    #     choices = [[1, 'Move 4 down.'], [2, 'Move 7 to left.'],])
    # uq5 = models.IntegerField (
    #     label = '4. Consider the puzzle in question 3. What is the minimum number of moves to solve the puzzle? ',
    #     widget = widgets.RadioSelect,
    #     choices = [[1, '2'], [2, '3'], [3, '4'],])
    # uq6 = models.IntegerField (
    #     label = "5. Look at the following puzzle. What's the correct move?",
    #     widget = widgets.RadioSelect,
    #     choices = [[1, 'Move the 5 to the left.'], [2, 'Move the 8 up.'],])
    # uq7 = models.IntegerField (
    #     label = '6. Consider the puzzle in question 5. What is the minimum number of moves to solve the puzzle? ',
    #     widget = widgets.RadioSelect,
    #     choices = [[1, '2'], [2, '3'], [3, '4'],])
    #
    # def uq2_error_message(self, uq2):
    #     print(uq2)
    #     if uq2 != 2:
    #         return self.session.config['uq_error']
    #
    # def uq3_error_message(self, uq3):
    #     print(uq3)
    #     if uq3 != 3:
    #         return self.session.config['uq_error']
    #
    # def uq4_error_message(self, uq4):
    #     print(uq4)
    #     if uq4 != 2:
    #         return self.session.config['uq_error']
    #
    # def uq5_error_message(self, uq5):
    #     print(uq5)
    #     if uq5 != 3:
    #         return self.session.config['uq_error']
    #
    # def uq6_error_message(self, uq6):
    #     print(uq6)
    #     if uq6 != 1:
    #         return self.session.config['uq_error']
    #
    # def uq7_error_message(self, uq7):
    #     print(uq7)
    #     if uq7 != 1:
    #         return self.session.config['uq_error']
