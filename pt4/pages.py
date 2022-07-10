from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Intro(Page):
    def before_next_page(self):
        self.player.calc_payment()


class SurveyASI(Page):
    form_model = 'player'
    form_fields = ['genderatt']

    def before_next_page(self):
        for i in Constants.genderatt_categories:
            setattr(self.player, i, getattr(self.player, 'conversion_gender')(i))


class SurveyBFI(Page):
    form_model = 'player'
    form_fields = ['bigfive']

    def before_next_page(self):
        for i in Constants.bigfive_categories:
            setattr(self.player, i, getattr(self.player, 'conversion')(i))


class SurveyDem(Page):
    form_model = 'player'
    form_fields = ['age',
                   'female',
                   'region',
                   'major',
                   'prog',
                   'freeq1',
                   'freeq2',
                   'puzzle_difficulty',
                   'freeq3']


class ThankYou(Page):
    form_model = 'player'
    form_fields = ['send_results']

    def vars_for_template(self):
        pt1earn = round(self.participant.vars['puzzles_solved_pt1'] * self.session.config['pt1rate'], 2)
        pt3earn = self.participant.vars['puzzles_solved_pt3'] * self.session.config['pt3rate']
        return dict(pt1earn=pt1earn,
                    pt3earn=pt3earn,
                    )


page_sequence = [Intro,
                 SurveyASI,
                 #SurveyBFI,
                 SurveyDem,
                 ThankYou]
