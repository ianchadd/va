from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Intro(Page):
    form_model = 'player'
    form_fields = ['uq1',
                   'uq2',
                   'uq3',
                   'uq4',
                   'uq5',
                   'uq6',
                   'uq7']


class Ready(Page):
    timeout_seconds = 5  # 5 seconds


class Game(Page):
    form_model = 'player'
    form_fields = ['puzzles_solved_pt1',
                   'puzzle_histories',
                   'va_correct']

    ###def get_timeout_seconds(self):
    ###    if self.session.config['test'] == 1:
    ###        return 30  # 30 seconds if test session
    ###    if self.session.config['test'] == 0:
    ###        return self.session.config['roundlength']  # 4 minutes if real session

    def js_vars(self):
        return {
            'boards': self.player.puzzle_to_play(formatting=0),
            'probs': self.session.config['va_probs'],
            'failure': self.session.config['failure_tracking']
        }

    def vars_for_template(self):
        va_pron = 'he'
        if self.participant.vars['pt1gender']:
            va_pron = 'she'
        return dict(
            va_pron = va_pron,
            va_name = self.session.config['va_name'],
            pt1image_path='GenderedIcons/{}.png'.format(self.participant.vars['pt1gender']),
            failure=self.session.config['failure_tracking'],
            turnlength=self.session.config['turnlength'],
            roundlength=self.session.config['roundlength']
        )


class Proceed(Page):
    def before_next_page(self):
        self.player.add_payoff()
        self.player.pass_variable()

class Debrief(Page):
    form_model = 'player'
    form_fields = ['guess_correct']

    def vars_for_template(self):
        va_pron = 'he'
        if self.participant.vars['pt1gender']:
            va_pron = 'she'
        return {
            'details': 'va/details.pdf',
            'va_pronoun': va_pron,
            'va_name': self.session.config['va_name'],
            'va_turns': int(self.session.config['roundlength']/(2 * self.session.config['turnlength']))
            }
    def before_next_page(self):
        if self.player.guess_correct == self.player.va_correct:
            self.player.payoff += self.session.config['pt1qbonus'] #TODO: Change


page_sequence = [Ready,
                 Game,
                 Proceed,
                 Debrief]
