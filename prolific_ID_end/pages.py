from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants
import json


class P_ID(Page):
    form_model = 'player'
    form_fields = ['p_ID']
    
    def before_next_page(self):
        self.player.participant.vars['p_id_end'] = self.player.p_ID
        
    def error_message(self, values):
        if len(values['p_ID']) !=24:
            return 'You must enter a valid 24 character Prolific ID.'
        
class P_Return(Page):
    form_model = 'player'
    
    def vars_for_template(self):
        parvars = self.participant.vars
        self.player.participant_vars = json.dumps(parvars)
        return dict(
            p_return_url = self.session.config['p_completion_link'],
            par_vars = parvars,
        )
            
page_sequence = [P_ID,
                 P_Return]
