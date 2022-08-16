from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class GroupForNextApp(WaitPage):
    template_name = 'pt1grp/MyWaitPage.html'
    group_by_arrival_time = True

    body_text = 'Waiting for the other participants to finish the puzzles. '\
                'This may take a few minutes.'

    def after_all_players_arrive(self):
        if len(self.group.get_players()) == 8:
            self.group.grouping()


page_sequence = [GroupForNextApp]
