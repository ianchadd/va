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
    name_in_url = 'payment_summary'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        import random
        tasks = ["Task 1: Individual Slider Task", "Task 2: VA Slider Task"] #sets treatment var at participant level with balanced 2x2
        for p in self.get_players():
            p.participant.vars['pay_task'] = random.choice(tasks)

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
