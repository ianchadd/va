from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class ThankYou(Page):
    def is_displayed(self):
        return self.participant.vars['participate'] == 0


page_sequence = [ThankYou]
