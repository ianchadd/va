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


author = 'Yuki Takahashi'

doc = """
Intermediate app with wait page only.
Group participants by their ability similarity.
This is needed to do perfect stranger matching across supergame in pt2.
"""


class Constants(BaseConstants):
    name_in_url = 'pt1grp'
    players_per_group = 8
    num_rounds = 1


class Subsession(BaseSubsession):
    def group_by_arrival_time_method(self, waiting_players):
        import random
        def sorting_key_ability(pl):  # sort players by ability
            return pl.participant.vars['puzzles_solved_pt1']
        print('Players currently waiting:', waiting_players)
        # wait until all players arrive
        if len(waiting_players) >= (self.session.config['num_part'] - Constants.players_per_group*self.grp_counter):
            print('ALL PLAYERS HAVE ARRIVED, SO WE NOW FORM GROUPS')
            print('before shuffle:', waiting_players)
            random.shuffle(waiting_players)
            print('after shuffle:', waiting_players)
            waiting_players.sort(key=sorting_key_ability)
            print('players must be sorted by their ability (from lowest to highest):', waiting_players)
            to_be_grpd = waiting_players[:Constants.players_per_group]
            print('WE GROUP THE FOLLOWING PLAYERS:', to_be_grpd)
            self.grp_counter += 1  # add 1 to a group counter
            return to_be_grpd

    grp_counter = models.IntegerField(initial=0)


class Group(BaseGroup):
    def grouping(self):  # assign group label
        import random
        id_list = random.sample([1, 2, 3, 4, 5, 6, 7, 8], 8)
        i = 0
        for p in self.get_players():
            p.participant.vars['mygrp'] = (self.id_in_subsession - 1)
            p.participant.vars['mygid'] = id_list[i]
            i += 1
            # below are lines for debug to check mygrp and mygid
            p.mygrp = p.participant.vars['mygrp']
            p.mygid = p.participant.vars['mygid']


class Player(BasePlayer):
    # set variables for debug on pt2grp
    mygrp = models.IntegerField()
    mygid = models.IntegerField()
