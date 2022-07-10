from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants


class P_ID(Page):
    form_model = 'player'
    form_fields = ['p_ID']

    def before_next_page(self):
        self.player.participant.vars['p_id_begin'] = self.player.p_ID

    def error_message(self, values):
        if len(values['p_ID']) !=24:
            return 'You must enter a valid 24 character Prolific ID.'

page_sequence = [P_ID]
