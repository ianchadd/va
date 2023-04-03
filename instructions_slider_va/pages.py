from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Intro(Page):
    # Intro page to welcome the participant to the Task
    def vars_for_template(self):
        return {
            'va_slider_rate': self.session.config['pt1rate'],
            'participant_vars': self.participant.vars,
            'participation_fee': self.session.config['participation_fee']
        }
    pass

class VA_Introduction(Page):
    # Intro page for the virtual assistant
    def vars_for_template(self):
        va_pron = 'he'
        if self.session.config['pt1gender']:
            va_pron = 'she'
        return {
            'va_pronoun': va_pron,
            'va_name': self.session.config['va_name'],
            'va_img_path': 'GenderedIcons/{}.png'.format(self.session.config['pt1gender']),
            'va_slider_rate': self.session.config['pt1rate'],
            'participant_vars': self.participant.vars,
            'participation_fee': self.session.config['participation_fee']
        }
    pass

class VA_Algo(Page):
    # Info on the algo for the VA
    def vars_for_template(self):
        va_pron = 'he'
        if self.session.config['pt1gender']:
            va_pron = 'she'
        return {
            'va_pronoun': va_pron,
            'va_name': self.session.config['va_name'],
            'va_img_path': 'GenderedIcons/{}.png'.format(self.session.config['pt1gender']),
            'va_slider_rate': self.session.config['pt1rate'],
            'participant_vars': self.participant.vars,
            'participation_fee': self.session.config['participation_fee']
        }
    pass

class VA_Turns(Page):
    # Info on the nature of turns
    def vars_for_template(self):
        va_pron = 'he'
        if self.session.config['pt1gender']:
            va_pron = 'she'
        return {
            'turn_length': self.session.config['turnlength'],
            'round_length': self.session.config['roundlength']/60,
            'va_pronoun': va_pron,
            'va_name': self.session.config['va_name'],
            'va_img_path': 'GenderedIcons/{}.png'.format(self.session.config['pt1gender']),
            'va_slider_rate': self.session.config['pt1rate'],
            'participant_vars': self.participant.vars,
            'participation_fee': self.session.config['participation_fee']
        }
    pass

class VA_Quality_Guess(Page):
    # Info on the nature of turns
    def vars_for_template(self):
        va_pron = 'he'
        if self.session.config['pt1gender']:
            va_pron = 'she'
        return {
            'turn_length': self.session.config['turnlength'],
            'round_length': self.session.config['roundlength']/60,
            'va_turns': int(self.session.config['roundlength']/(2 * self.session.config['turnlength'])),
            'va_pronoun': va_pron,
            'va_name': self.session.config['va_name'],
            'va_img_path': 'GenderedIcons/{}.png'.format(self.session.config['pt1gender']),
            'va_slider_rate': self.session.config['pt1rate'],
            'participant_vars': self.participant.vars,
            'participation_fee': self.session.config['participation_fee']
        }
    pass

class VA_Quality_Guess_Entry(Page):
    # Info on the nature of turns
    form_model = 'player'
    form_fields = ['initial_guess']
    def vars_for_template(self):
        va_pron = 'he'
        if self.session.config['pt1gender']:
            va_pron = 'she'
        return {
            'turn_length': self.session.config['turnlength'],
            'round_length': self.session.config['roundlength']/60,
            'va_turns': int(self.session.config['roundlength']/(2 * self.session.config['turnlength'])),
            'va_pronoun': va_pron,
            'va_name': self.session.config['va_name'],
            'va_img_path': 'GenderedIcons/{}.png'.format(self.session.config['pt1gender']),
            'va_slider_rate': self.session.config['pt1rate'],
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
    VA_Introduction,
    VA_Algo,
    VA_Turns,
    VA_Quality_Guess,
    VA_Quality_Guess_Entry
    ]
