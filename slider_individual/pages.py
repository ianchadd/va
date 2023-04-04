from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Intro(Page):
    def vars_for_template(self):
        roundlength = self.session.config['roundlength']/60 #in minutes
        return{
            'roundlength': int(roundlength)
        }


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
            return self.session.config['roundlength']

    def js_vars(self):
        return {
            'boards': self.player.puzzle_to_play(formatting=0)
        }


class Proceed(Page):
    def before_next_page(self):
        self.player.add_payoff()
        self.player.pass_variable()


page_sequence = [Intro,
                 Ready,
                 Game,
                 Proceed]
