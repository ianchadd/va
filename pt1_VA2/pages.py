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
                   'puzzle_histories']

    def get_timeout_seconds(self):
        if self.session.config['test'] == 1:
            return 30  # 30 seconds if test session
        if self.session.config['test'] == 0:
            return 4*60  # 4 minutes if real session

    def js_vars(self):
        return {
            'boards': self.player.puzzle_to_play(formatting=0),
            'probs': self.session.config['va_probs'],
            'failure': self.session.config['failure_tracking']
        }

    def vars_for_template(self):
        return dict(
            pt1image_path='GenderedIcons/{}.png'.format(self.session.config['pt1gender']),
            failure=self.session.config['failure_tracking'],
            turnlength=self.session.config['turnlength']
        )


class Proceed(Page):
    def before_next_page(self):
        self.player.add_payoff()
        self.player.pass_variable()


page_sequence = [Ready,
                 Game,
                 Proceed]
