from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


class Constants(BaseConstants):
    name_in_url = 'p_id_end'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    p_ID = models.StringField(label = '')
    participant_vars = models.LongStringField()

    def p_ID_error_message(self,value):
        if len(value) != 24:
            return "Your prolific ID must be 24 characters long."
