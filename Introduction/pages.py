from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Intro(Page):
    # Intro page to welcome the participant to the study
    def vars_for_template(self):
        return {
            'participant_vars': self.participant.vars,
            'participation_fee': self.session.config['participation_fee']
        }
    pass

class Instructions_slider_0(Page):
    # First page of instructions for the slider task
    def vars_for_template(self):
        return {
            'participant_vars': self.participant.vars,
            'participation_fee': self.session.config['participation_fee']
        }
    pass

class Instructions_slider_1(Page):
    # Second page of instructions for the slider task
    # First example puzzle
    def vars_for_template(self):
        return {
            'participant_vars': self.participant.vars,
            'participation_fee': self.session.config['participation_fee']
        }
    pass

class Instructions_slider_2(Page):
    # Second page of instructions for the slider task
    # First example puzzle
    def vars_for_template(self):
        return {
            'participant_vars': self.participant.vars,
            'participation_fee': self.session.config['participation_fee']
        }
    pass






page_sequence = [
    Intro,
    Instructions_slider_0,
    Instructions_slider_1,
    Instructions_slider_2
    ]
