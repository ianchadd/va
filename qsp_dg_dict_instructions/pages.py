from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):
    form_model = 'player'
    form_fields = ['attn_check_bird']
    
    def vars_for_template(self):
        id_list = []
        flag_list = []
        for i in self.participant.vars['id_choices']:
            id_list.append(i)
        for i in self.participant.vars['my_flag_choices']:
            flag_list.append('flag_survey/flags/flag_{}'.format(i)+'.png')

        pvars = self.participant.vars
        task = pvars['task']
        part = pvars['part']
        return dict(
            id_list = id_list,
            flag_list = flag_list,
            participant_vars = str(pvars),
            task = task,
            part = part
        )
    def before_next_page(self):
        self.player.set_ID(self.player.chooseID)
        self.player.set_other_flag()
        self.player.participant_vars_dump(self)


    
class Recip_Choose_ID_O(Page):
    #player will be able to choose from a list of randomly generated ID options
    form_model = 'player'
    
    def vars_for_template(self):
        return dict(
            img='flag_survey/recip_id_choose.png',
            participant_vars = str(self.participant.vars)
        )

    def before_next_page(self):
        self.player.set_ID(self.player.chooseID)
        self.player.set_other_flag()

class Recip_Choose_Icon(Page):
    #player will choose a flag icon on this page
    form_model = 'player'
    def vars_for_template(self):
        return dict(
            img='flag_survey/recip_icon_choose.png',
            participant_vars = str(self.participant.vars)
        )

class Options_List(Page):
    form_model = 'player'
    def vars_for_template(self):
        my_list = []
        for i in self.participant.vars['recip_options']:
            my_list.append([i[0],'flag_survey/flags/flag_{}'.format(i[1])+'.png'])
        rows = 3
        pvars = self.participant.vars
        task = pvars['task']
        part = pvars['part']
        return dict(
            recip_options = my_list,
            participant_vars = str(pvars),
            task = task,
            part = part
        )

    

page_sequence = [
    #Informed_Consent,
    Instructions,
    #Choose_ID_R,
    #ID_result,
    #Choose_ID_C,
    #Recip_Choose_ID_O,
    #Recip_Choose_Icon,
    Options_List
]
