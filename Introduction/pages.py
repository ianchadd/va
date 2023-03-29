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

class Instructions_slider_3(Page):
    # Third page of instructions for the slider task
    #  example puzzle
    def vars_for_template(self):
        return {
            'participant_vars': self.participant.vars,
            'participation_fee': self.session.config['participation_fee']
        }
    pass

class Instructions_slider_4(Page):
    # Third page of instructions for the slider task
    #  example puzzle
    def vars_for_template(self):
        return {
            'participant_vars': self.participant.vars,
            'participation_fee': self.session.config['participation_fee']
        }
    pass
class Instructions_slider_5(Page):
    # Third page of instructions for the slider task
    #  example puzzle
    def vars_for_template(self):
        return {
            'participant_vars': self.participant.vars,
            'participation_fee': self.session.config['participation_fee']
        }
    pass
class Instructions_slider_6(Page):
    # Third page of instructions for the slider task
    #  example puzzle
    def vars_for_template(self):
        return {
            'participant_vars': self.participant.vars,
            'participation_fee': self.session.config['participation_fee']
        }
    pass
class Instructions_slider_7(Page):
    # Third page of instructions for the slider task
    #  example puzzle
    def vars_for_template(self):
        return {
            'participant_vars': self.participant.vars,
            'participation_fee': self.session.config['participation_fee']
        }
    pass

class Check_understanding(Page):
    # Checks for understanding slider puzzle
    form_model = 'player'
    form_fields = ['uq2',
                   'uq3',
                   'uq4',
                   'uq5',
                   'uq6',
                   'uq7']
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
    Instructions_slider_2,
    Instructions_slider_3,
    Instructions_slider_4,
    Instructions_slider_5,
    Instructions_slider_6,
    Instructions_slider_7,
    Check_understanding
    ]
