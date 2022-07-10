from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Reg(Page):
    form_model = 'player'
    form_fields = ['fname',
                   'lname',
                   'email']

    def before_next_page(self):
        if self.player.fname != '':
            self.player.assign_plabel()
            self.player.add_payoff()


class Draw(Page):
    def before_next_page(self):
        self.player.draw_coin()


class Wait(Page):
    def vars_for_template(self):
        return dict(
            image_path='coin/coin{}.png'.format(self.player.coin)
        )


class Excess(Page):
    form_model = 'player'
    form_fields = ['participate']

    def before_next_page(self):
        self.participant.vars['participate'] = self.player.participate

    def app_after_this_page(self, upcoming_apps):  # flag inactive players
        if self.player.participate == 0:
            return "pt99"


class Intro(Page):
    ...


page_sequence = [Reg,
                 Draw,
                 Wait,
                 Excess,
                 Intro]
