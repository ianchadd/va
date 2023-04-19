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


class VA_Freq(Page):
    form_model = 'player'
    form_fields = [
        'VAFREQ',
        'VAACCESS',
        'VAWORK'
    ]

class VA_Gen(Page):
    form_model = 'player'
    form_fields = [
        'VAGEN'
    ]

class VA_Uses(Page):
    form_model = 'player'
    form_fields = [
        'AI_alarms',
        'AI_info',
        'AI_music',
        'AI_calls',
        'AI_sched',
        'AI_recs',
        'AI_calcs',
        'AI_other',
        'diff_AI'
    ]
    def error_message(self,values):
        if values['AI_other']:
            return 'If you select Other, you must specify in the provided field'

        if values['AI_alarms'] == 0 and values['AI_info'] == 0 and values['AI_music'] == 0 and values['AI_calls'] == 0 and values['AI_sched'] == 0 and values['AI_recs'] == 0 and values['AI_calcs'] == 0 and values['AI_other'] == 0:
            return 'You must select at least one response.'
        elif values['AI_other'] and type(values['diff_AI']) == type(None):
            return 'If you select Other, you must specify in the provided field'

class VA_Trust(Page):
    form_model = 'player'
    form_fields = [
        'VATRUST'
    ]

class VA_TrustMC(Page):
    form_model = 'player'
    form_fields = [
        'AI_trust_conv',
        'AI_trust_eff',
        'AI_trust_prod',
        'AI_trust_help',
        'AI_trust_acc',
        'AI_trust_rel',
        'AI_trust_priv',
        'AI_trust_sec',
        'AI_trust_human',
        'AI_trust_other',
        'diff_AI_trust'
    ]

    def error_message(self, values):
        if values['AI_trust_conv'] == 0 and values['AI_trust_eff'] == 0 and values['AI_trust_prod'] == 0 and values['AI_trust_help'] == 0 and values['AI_trust_acc'] == 0 and values['AI_trust_rel'] == 0 and values['AI_trust_priv'] == 0 and values['AI_trust_sec'] == 0 and values['AI_trust_human'] == 0 and values['AI_trust_other'] == 0:
            return 'You must select at least one response.'
        elif values['AI_trust_other'] and type(values['diff_AI_trust']) == type(None):
            return 'If you select Other, you must specify in the provided field'

class VA_DistrustMC(Page):
    form_model = 'player'
    form_fields = [
        'AI_distrust_conv',
        'AI_distrust_eff',
        'AI_distrust_prod',
        'AI_distrust_help',
        'AI_distrust_acc',
        'AI_distrust_rel',
        'AI_distrust_priv',
        'AI_distrust_sec',
        'AI_distrust_human',
        'AI_distrust_other',
        'diff_AI_distrust'
    ]

    def error_message(self, values):
        if values['AI_distrust_conv'] == 0 and values['AI_distrust_eff'] == 0 and values['AI_distrust_prod'] == 0 and values['AI_distrust_help'] == 0 and values['AI_distrust_acc'] == 0 and values['AI_distrust_rel'] == 0 and values['AI_distrust_priv'] == 0 and values['AI_distrust_sec'] == 0 and values['AI_distrust_human'] == 0 and values['AI_distrust_other'] == 0:
            return 'You must select at least one response.'
        elif values['AI_distrust_other'] and type(values['diff_AI_distrust']) == type(None):
            return 'If you select Other, you must specify in the provided field'

class VA_Emotions(Page):
    form_model = 'player'
    form_fields = [
        'VAHAPPY',
        'VAPROD'
    ]

class GPT_Time(Page):
    form_model = 'player'
    form_fields = [
        'GPTFAM',
        'GPTSTART',
        'GPTPROL'
    ]


class GPT_Uses(Page):
    form_model = 'player'
    form_fields = [
        'GPT_USE_time',
        'GPT_USE_accu',
        'GPT_USE_comp',
        'GPT_USE_bonus',
        'GPT_USE_none',
        'GPT_USE_other',
        'diff_GPT_USE'
    ]

    def error_message(self, values):
        if values['GPT_USE_time'] == 0 and values['GPT_USE_accu'] == 0 and values['GPT_USE_comp'] == 0 and values['GPT_USE_bonus'] == 0 and values['GPT_USE_none'] == 0 and values['GPT_USE_other'] == 0:
            return 'You must select at least one response.'
        elif values['GPT_USE_other'] and type(values['diff_GPT_USE']) == type(None):
            return 'If you select Other, you must specify in the provided field'

class GPT_Fair(Page):
    form_model = 'player'
    form_fields = [
        'GPTCHEAT_PRO',
        'GPTCHEAT_EDU',
        'GPTPROD_PRO',
        'GPTLEARN_EDU',
        'GPTFAIR_PRO',
        'GPTFAIR_COMP'
    ]

class GPT_Bias(Page):
    form_model = 'player'
    form_fields = [
        'GPTABILITY',
        'GPTGENDER'
    ]

class GPT_Misc(Page):
    form_model = 'player'
    form_fields = [
        'GPTSKILLS',
        'GPTCREATIVE'
    ]

page_sequence = [Instructions,
                # VA_Perception_Gend,
                # VA_Perception_Perf,
                # Age,
                # Sex,
                # Gender,
                # Orientation,
                # S_History,
                # Relationship,
                # Primary_Earner,
                # Income,
                # Attn_Check,
                # Ethnicity,
                # Religion,
                # Politics,
                # LGBT_Free,
                # LGBT_Ally,
                # Location,
                # Attitudes_Gend,
                # VA_Freq,
                # VA_Uses,
                # VA_Gen,
                # VA_Trust,
                # VA_TrustMC,
                # VA_DistrustMC,
                # VA_Emotions,
                 GPT_Time,
                 GPT_Uses,
                 GPT_Fair,
                 GPT_Bias,
                 GPT_Misc
                 ]
