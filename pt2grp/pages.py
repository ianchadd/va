from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class GroupForNextApp(WaitPage):
    template_name = 'pt2grp/MyWaitPage.html'
    group_by_arrival_time = True

    body_text = 'In attesa degli altri partecipanti finire il puzzle. ' \
                'Questo potrebbe richiedere alcuni minuti.'

    def after_all_players_arrive(self):
        self.group.make_matches()


page_sequence = [GroupForNextApp]
