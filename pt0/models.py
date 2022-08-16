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

author = 'Yuki Takahashi'

doc = """
General instructions of the study.
"""


class Constants(BaseConstants):
    name_in_url = 'intro'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        self.session.vars['coins'] = list(range(1, 33))
        self.session.vars['names'] = []


class Group(BaseGroup):
    ...


class Player(BasePlayer):
    # 1st page info
    fname = models.StringField(label='First Name:')
    lname = models.StringField(label='Last Name:')
    email = models.StringField(label='E-mail address you registered on ORSEE:')
    # 2nd page info and random number
    coin = models.IntegerField()
    # participation flag
    participate = models.BooleanField()

    def draw_coin(self):
        import random
        self.coin = random.choice(self.session.vars['coins'])
        self.session.vars['coins'].remove(self.coin)

    def assign_plabel(self):  # I assume maximum 5 people have the same name
        if self.fname not in self.session.vars['names']:
            self.participant.label = self.fname
            self.session.vars['names'].append(self.participant.label)
        elif self.fname in self.session.vars['names']:
            tentative_plabel = self.fname + "2"
            if tentative_plabel in self.session.vars['names']:
                tentative_plabel = self.fname + "3"
                if tentative_plabel in self.session.vars['names']:
                    tentative_plabel = self.fname + "4"
                    if tentative_plabel in self.session.vars['names']:
                        tentative_plabel = self.fname + "5"
            self.participant.label = tentative_plabel
            self.session.vars['names'].append(self.participant.label)

    # a function to add tentative earnings to the build-in payff variable
    def add_payoff(self):
        self.payoff += self.session.config['partfee']
