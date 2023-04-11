from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants

class Instructions(Page):
    form_model = 'player'
    form_fields = []

class Age(Page):
    form_model = 'player'
    form_fields = [#'age',
                   'yob']

class Attn_Check(Page):
    form_model = 'player'
    form_fields = ['attn_check_1']

class Sex(Page):
    form_model = 'player'
    form_fields = ['sex']

class Gender(Page):
    form_model = 'player'
    form_fields = ['male',
                   'female',
                   't_male',
                   't_female',
                   'gnc',
                   'nb',
                   'other_g',
                   'diff_gend']
    def error_message(self,values):
        #if values['other_g'] and type(values['diff_gend']) == type(None):
        #    return 'If you select Other, you must specify in the provided field'

        if values['male'] == 0 and values['female'] == 0 and values['t_male'] == 0 and values['t_female'] == 0 and values['gnc'] == 0 and values['nb'] == 0 and values['other_g'] == 0:
            return 'You must select at least one response.'
        elif values['other_g'] and type(values['diff_gend']) == type(None):
            return 'If you select Other, you must specify in the provided field'

class Orientation(Page):
    form_model = 'player'
    form_fields = ['orientation',
                   'other_orientation']

    def error_message(self,values):
        if values['orientation'] =='Other (please state below)' and type(values['other_orientation']) == type(None) :
            return 'If you select Other, you must specify in the provided field'


class S_History(Page):
    form_model = 'player'
    form_fields = ['sex_hist',
                   'attracted_men',
                   'attracted_women']

class Relationship(Page):
    form_model = 'player'
    form_fields = ['relationship',
                   'other_relationship']

    def error_message(self,values):
        if values['relationship'] =='Other (please state below)' and type(values['other_relationship']) == type(None):
            return 'If you select Other, you must specify in the provided field'


class Primary_Earner(Page):
    def is_displayed(self):
        return self.player.relationship != 'Single'

    form_model = 'player'
    form_fields = ['primary_earner']

class Income(Page):
    form_model = 'player'
    form_fields = ['income']

class Ethnicity(Page):
    form_model = 'player'
    form_fields = ['ethnicity',
                   'other_ethnicity']

    def error_message(self,values):
        if values['ethnicity'] =='Other (please state below)' and type(values['other_ethnicity']) == type(None):
            return 'If you select Other, you must specify in the provided field'
class Religion(Page):
    form_model = 'player'
    form_fields = ['religion',
                   'other_religion']
    def error_message(self,values):
        if values['religion'] =='Some other religious affiliation (please specify below)' and type(values['other_religion']) == type(None):
            return 'If you select Other, you must specify in the provided field'

class Politics(Page):
    form_model = 'player'
    form_fields = ['econ_politics',
                   'social_politics']

class LGBT_Free(Page):
    form_model = 'player'
    form_fields = ['lgbt_free']

class LGBT_Ally(Page):
    form_model = 'player'
    form_fields = ['consider_lgbt_ally',
                   'program_lgbt_ally']

class Location(Page):
    form_model = 'player'
    form_fields = ['live_in',
                   'other_live_location',
                   'grew_up_in',
                   'other_grew_up_location']
    def error_message(self,values):
        if (values['live_in'] =='Other (please state below)' and type(values['other_live_location']) == type(None)) or(values['grew_up_in'] =='Other (please state below)' and type(values['other_grew_up_location']) == type(None)) :
            return 'If you select Other, you must specify in the provided field'

class Attitudes_Gend(Page):
    form_model = 'player'
    form_fields = [
        'FEWORK',
        'FEHOME',
        'FEPRES',
        'FEPOL',
        'FECHILD',
        'FEPRESCH',
        'FEHELP',
        'FEFAM'
    ]

class VA_Perception_Gend(Page):
    form_model = 'player'
    form_fields = [
        'CGI',
    ]
    def vars_for_template(self):
        va_pron = 'he'
        if self.session.config['pt1gender']:
            va_pron = 'she'
        return dict(
            va_pron = va_pron,
            va_name = self.session.config['va_name'],
            va_img_path='GenderedIcons/{}.png'.format(self.session.config['pt1gender'])
        )

class VA_Perception_Perf(Page):
    form_model = 'player'
    form_fields = [
        'va_performance_bucket',
        'va_performance_cts'
    ]
    def vars_for_template(self):
        va_pron = 'he'
        if self.session.config['pt1gender']:
            va_pron = 'she'
        return dict(
            va_pron = va_pron,
            va_name = self.session.config['va_name'],
            va_img_path='GenderedIcons/{}.png'.format(self.session.config['pt1gender'])
        )

page_sequence = [Instructions,
                VA_Perception_Gend,
                VA_Perception_Perf,
                 Age,
                 Sex,
                 Gender,
                 #Orientation,
                 #S_History,
                 #Relationship,
                 #Primary_Earner,
                 Income,
                 Attn_Check,
                 Ethnicity,
                 #Religion,
                 #Politics,
                 #LGBT_Free,
                 #LGBT_Ally,
                 #Location,
                 Attitudes_Gend,
                 ]
