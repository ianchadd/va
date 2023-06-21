from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Summary(Page):
    def vars_for_template(self):
        return {
            'participant_vars': self.participant.vars,
            'participation_fee': self.session.config['participation_fee'],
            'paid_task': self.participant.vars['pay_task']
        }
    pass




page_sequence = [
    Summary
    ]
