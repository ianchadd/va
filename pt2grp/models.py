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
Intermediate app. Do matching based on preference in part 2.
"""


class Constants(BaseConstants):
    name_in_url = 'pt2grp'
    players_per_group = 8
    num_rounds = 1


class Subsession(BaseSubsession):
    def group_by_arrival_time_method(self, waiting_players):
        def sorting_key_gid(pl):  # sort players by mygid
            return pl.participant.vars['mygid']
        def sort_by_gid(grp):  # sort group by players' gid
            grp.sort(key=sorting_key_gid)
            return grp
        grp1 = [p for p in waiting_players if p.participant.vars['mygrp'] == 1]
        grp2 = [p for p in waiting_players if p.participant.vars['mygrp'] == 2]
        grp3 = [p for p in waiting_players if p.participant.vars['mygrp'] == 3]
        grp4 = [p for p in waiting_players if p.participant.vars['mygrp'] == 4]
        if len(grp1) == 8:
            sort_by_gid(grp1)
            print('THIS IS GROUP 1, WHICH CONSISTS OF THE FOLLOWING PLAYERS:', grp1)
            return grp1
        if len(grp2) == 8:
            sort_by_gid(grp2)
            print('THIS IS GROUP 2, WHICH CONSISTS OF THE FOLLOWING PLAYERS:', grp2)
            return grp2
        if len(grp3) == 8:
            sort_by_gid(grp3)
            print('THIS IS GROUP 3, WHICH CONSISTS OF THE FOLLOWING PLAYERS:', grp3)
            return grp3
        if len(grp4) == 8:
            sort_by_gid(grp4)
            print('THIS IS GROUP 4, WHICH CONSISTS OF THE FOLLOWING PLAYERS:', grp4)
            return grp4


class Group(BaseGroup):
    def make_matches(self):
        import random
        pairs = []  # a list where I store pairs
        unmatched = [1, 2, 3, 4, 5, 6, 7, 8]  # keep track of who's left unmatched
        k = 0  # count number of matches
        # randomly choose participants and rounds for check
        partset = random.sample([1, 2, 3, 4, 5, 6, 7, 8], 8)
        rdset = random.sample([1, 2, 3, 4, 5, 6, 7], 7)
        print('Participants set (1st participants match is checked first):', partset)
        print('Round set (participants match is checked in this order)', rdset)
        for i in partset:
            # group structure rd1: [[1, 2], [3, 4], [5, 6], [7, 8]]
            # group structure rd2: [[2, 3], [4, 5], [6, 7], [8, 1]]
            # group structure rd3: [[1, 3], [5, 7], [2, 4], [6, 8]]
            # group structure rd4: [[1, 7], [2, 8], [3, 5], [4, 6]]
            # group structure rd5: [[1, 4], [7, 2], [5, 8], [3, 6]]
            # group structure rd6: [[4, 7], [2, 5], [8, 3], [6, 1]]
            # group structure rd7: [[1, 5], [2, 6], [3, 7], [4, 8]]
            if i == 1:
                my_partners = [2, 8, 3, 7, 4, 6, 5]
            if i == 2:
                my_partners = [1, 3, 4, 8, 7, 5, 6]
            if i == 3:
                my_partners = [4, 2, 1, 5, 6, 8, 7]
            if i == 4:
                my_partners = [3, 5, 2, 6, 1, 7, 8]
            if i == 5:
                my_partners = [6, 4, 7, 3, 8, 2, 1]
            if i == 6:
                my_partners = [5, 7, 8, 4, 3, 1, 2]
            if i == 7:
                my_partners = [8, 6, 5, 1, 2, 4, 3]
            if i == 8:
                my_partners = [7, 1, 6, 2, 5, 3, 4]
            p0 = self.get_player_by_id(i)  # chosen player object
            # retrieve match variables from pt2
            my_matches = [p0.participant.vars[i] for i in
                          ['match_rd1', 'match_rd2', 'match_rd3', 'match_rd4',
                           'match_rd5', 'match_rd6', 'match_rd7']]
            print('Player', i, 's matches, ordered from rd1 to rd7:', my_matches)
            print('Player', i, 's partners, ordered from rd1 to rd7:', my_partners)
            for t in rdset:
                if i in unmatched and my_partners[t-1] in unmatched and my_matches[t-1] == 1:
                    pairs.append(i)
                    pairs.append(my_partners[t - 1])
                    unmatched.remove(i)
                    unmatched.remove(my_partners[t-1])
                    print('WE FOUND A MATCH IN ROUND', t, ', SO WE PAIR THEM:', [i, my_partners[t-1]])
                    print('Players not yet matched', unmatched)
                else:
                    print('No match in round', t, ', so check next round.')
        if len(unmatched) > 0:
            print('The following players could not find a pair, so match them randomly:', unmatched)
            random.shuffle(unmatched)
            k = len(unmatched)
            while k > 0:
                print('WE PAIR THE FOLLOWING PLAYERS', [self.get_player_by_id(unmatched[0]),
                                                        self.get_player_by_id(unmatched[1])])
                pairs.append(unmatched[0])
                pairs.append(unmatched[1])
                unmatched.pop(0)
                unmatched.pop(0)
                k -= 2
        # store the matches in a participant.vars, which we will restore in pt1_VA
        for p in self.get_players():
            p.participant.vars['mypairs'] = str(pairs)
        self.mypairs = self.get_player_by_id(1).participant.vars['mypairs']

    # a variable just to show the final matches in the data
    mypairs = models.StringField()


class Player(BasePlayer):
    ...
