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


author = 'Ian Chadd'

doc = """
Payment summary app for VA project.
"""


class Constants(BaseConstants):
    name_in_url = 'Payment Summary'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    # def creating_session(self):
    pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    task_for_payment = random.choice(["Task 1: Individual Slider Task", "Task 2: VA Slider Task"])
