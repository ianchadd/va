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

import random


author = 'Yuki Takahashi'

doc = """
Meeting and matching (main part)
"""


class Constants(BaseConstants):
    name_in_url = 'pt2'
    players_per_group = 2  # 8 people participating in each supergroup, so 4 groups.
    num_rounds = 7  # should be 7 rounds


class Subsession(BaseSubsession):
    # define variables to keep track of remaining players in each group in each round
    # we can increase the number of groups
    grp1ctr = models.IntegerField(initial=8)
    grp2ctr = models.IntegerField(initial=8)
    grp3ctr = models.IntegerField(initial=8)
    grp4ctr = models.IntegerField(initial=8)

    # perfect stranger matching based on the group membership and id within the group
    # defined in pt1grp, which was based on group_by_arrival_time()
    def group_by_arrival_time_method(self, waiting_players):
        import itertools  # import itertools for groupby()
        # define several functions to be used as sorting keys
        def sorting_key_both(pl):  # sort players by mygrp and mygid
            return [pl.participant.vars['mygrp'], pl.participant.vars['mygid']]
        def sorting_key_grp(pl):  # sort players by mygrp
            return pl.participant.vars['mygrp']
        def sorting_key_gid(pl):  # sort players by mygid
            return pl.participant.vars['mygid']
        waiting_players.sort(key=sorting_key_both)
        # create a list in which each element is a list of players belonging to the same mygrp, from grp1 to grpN
        waiting_players_grped = [list(g) for k, g in itertools.groupby(waiting_players, key=sorting_key_grp)]
        # sort the list so that longest list group comes first
        waiting_players_grped.sort(reverse=True, key=lambda x: len(x))
        print('waiting players with the largest group in the first:', waiting_players_grped)
        # create a list of mygrp
        waiting_players_key = [int(k) for k, g in itertools.groupby(waiting_players, key=sorting_key_grp)]
        print('waiting groups:', waiting_players_key)
        # choose the first group
        waiting_grp = waiting_players_grped[0]
        waiting_grp_num = waiting_players_grped[0][0].participant.vars['mygrp']
        # Make reference to group counter (shallow copy NOT working!)
        if waiting_grp_num == 1:
            grp_ctr = self.grp1ctr
        if waiting_grp_num == 2:
            grp_ctr = self.grp2ctr
        if waiting_grp_num == 3:
            grp_ctr = self.grp3ctr
        if waiting_grp_num == 4:
            grp_ctr = self.grp4ctr
        print('waiting players in the largest group:', waiting_grp)
        if len(waiting_grp) == grp_ctr:
            print('ALL THE REMAINING PLAYERS IN THIS GROUP ARE WAITING. SO WE WILL NOW DO MATCHING. THIS IS GROUP', waiting_grp_num, 'WITH THE NUMBER OF WAITNG PLAYERS', grp_ctr, 'IN ROUND', self.round_number)
            # deduct counter from grp counter
            if waiting_grp_num == 1:
                self.grp1ctr -= 2
            if waiting_grp_num == 2:
                self.grp2ctr -= 2
            if waiting_grp_num == 3:
                self.grp3ctr -= 2
            if waiting_grp_num == 4:
                self.grp4ctr -= 2
            waiting_grp.sort(key=sorting_key_gid)
            ind = [i.participant.vars['mygid'] for i in waiting_grp]
            print('Group ID indices (gid for remaining players in this group):', ind)
            if self.round_number == 1:
                # group structure: [[1, 2], [3, 4], [5, 6], [7, 8]]
                if 1 in ind and 2 in ind:
                    to_be_grpd = [waiting_grp[ind.index(1)], waiting_grp[ind.index(2)]]
                elif 3 in ind and 4 in ind:
                    to_be_grpd = [waiting_grp[ind.index(3)], waiting_grp[ind.index(4)]]
                elif 5 in ind and 6 in ind:
                    to_be_grpd = [waiting_grp[ind.index(5)], waiting_grp[ind.index(6)]]
                elif 7 in ind and 8 in ind:
                    to_be_grpd = [waiting_grp[ind.index(7)], waiting_grp[ind.index(8)]]
                else:
                    print('ERROR - CHECK CODE!')
            if self.round_number == 2:
                # group structure: [[2, 3], [4, 5], [6, 7], [8, 1]]
                if 2 in ind and 3 in ind:
                    to_be_grpd = [waiting_grp[ind.index(2)], waiting_grp[ind.index(3)]]
                elif 4 in ind and 5 in ind:
                    to_be_grpd = [waiting_grp[ind.index(4)], waiting_grp[ind.index(5)]]
                elif 6 in ind and 7 in ind:
                    to_be_grpd = [waiting_grp[ind.index(6)], waiting_grp[ind.index(7)]]
                elif 8 in ind and 1 in ind:
                    to_be_grpd = [waiting_grp[ind.index(8)], waiting_grp[ind.index(1)]]
                else:
                    print('ERROR - CHECK CODE!')
            if self.round_number == 3:
                # group structure: [[1, 3], [5, 7], [2, 4], [6, 8]]
                if 1 in ind and 3 in ind:
                    to_be_grpd = [waiting_grp[ind.index(1)], waiting_grp[ind.index(3)]]
                elif 5 in ind and 7 in ind:
                    to_be_grpd = [waiting_grp[ind.index(5)], waiting_grp[ind.index(7)]]
                elif 2 in ind and 4 in ind:
                    to_be_grpd = [waiting_grp[ind.index(2)], waiting_grp[ind.index(4)]]
                elif 6 in ind and 8 in ind:
                    to_be_grpd = [waiting_grp[ind.index(6)], waiting_grp[ind.index(8)]]
                else:
                    print('ERROR - CHECK CODE!')
            if self.round_number == 4:
                # group structure: [[1, 7], [2, 8], [3, 5], [4, 6]]
                if 1 in ind and 7 in ind:
                    to_be_grpd = [waiting_grp[ind.index(1)], waiting_grp[ind.index(7)]]
                elif 2 in ind and 8 in ind:
                    to_be_grpd = [waiting_grp[ind.index(2)], waiting_grp[ind.index(8)]]
                elif 3 in ind and 5 in ind:
                    to_be_grpd = [waiting_grp[ind.index(3)], waiting_grp[ind.index(5)]]
                elif 4 in ind and 6 in ind:
                    to_be_grpd = [waiting_grp[ind.index(4)], waiting_grp[ind.index(6)]]
                else:
                    print('ERROR - CHECK CODE!')
            if self.round_number == 5:
                # group structure: [[1, 4], [7, 2], [5, 8], [3, 6]]
                if 1 in ind and 4 in ind:
                    to_be_grpd = [waiting_grp[ind.index(1)], waiting_grp[ind.index(4)]]
                elif 7 in ind and 2 in ind:
                    to_be_grpd = [waiting_grp[ind.index(7)], waiting_grp[ind.index(2)]]
                elif 5 in ind and 8 in ind:
                    to_be_grpd = [waiting_grp[ind.index(5)], waiting_grp[ind.index(8)]]
                elif 3 in ind and 6 in ind:
                    to_be_grpd = [waiting_grp[ind.index(3)], waiting_grp[ind.index(6)]]
                else:
                    print('ERROR - CHECK CODE!')
            if self.round_number == 6:
                # group structure: [[4, 7], [2, 5], [8, 3], [6, 1]]
                if 4 in ind and 7 in ind:
                    to_be_grpd = [waiting_grp[ind.index(4)], waiting_grp[ind.index(7)]]
                elif 2 in ind and 5 in ind:
                    to_be_grpd = [waiting_grp[ind.index(2)], waiting_grp[ind.index(5)]]
                elif 8 in ind and 3 in ind:
                    to_be_grpd = [waiting_grp[ind.index(8)], waiting_grp[ind.index(3)]]
                elif 6 in ind and 1 in ind:
                    to_be_grpd = [waiting_grp[ind.index(6)], waiting_grp[ind.index(1)]]
                else:
                    print('ERROR - CHECK CODE!')
            if self.round_number == 7:
                # group structure: [[1, 5], [2, 6], [3, 7], [4, 8]]
                if 1 in ind and 5 in ind:
                    to_be_grpd = [waiting_grp[ind.index(1)], waiting_grp[ind.index(5)]]
                elif 2 in ind and 6 in ind:
                    to_be_grpd = [waiting_grp[ind.index(2)], waiting_grp[ind.index(6)]]
                elif 3 in ind and 7 in ind:
                    to_be_grpd = [waiting_grp[ind.index(3)], waiting_grp[ind.index(7)]]
                elif 4 in ind and 8 in ind:
                    to_be_grpd = [waiting_grp[ind.index(4)], waiting_grp[ind.index(8)]]
                else:
                    print('ERROR - CHECK CODE!')
            print('WE MATCH THE FOLLOWING PLAYERS:', to_be_grpd)
            return to_be_grpd


class Group(BaseGroup):
    # variables for the puzzle
    starting_player = models.IntegerField()
    move_history = models.LongStringField()
    move_histories_disagree = models.BooleanField()
    puzzle_solved = models.BooleanField(initial=False)

    # verify that the moves are stored correctly
    def verify_stored_moves(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        if p1.move_history == p2.move_history:
            self.move_history = p1.move_history
            self.move_histories_disagree = False
        else:
            self.move_histories_disagree = True
        if p1.puzzle_solved or p2.puzzle_solved:
            self.puzzle_solved = True
            p1.puzzle_solved = True
            p2.puzzle_solved = True
        else:
            self.puzzle_solved = False


    # define puzzles to play
    def puzzle_to_play(self, formatting):
        if self.round_number == 1:
            my_puzzle = [[2, 4, 3], [1, 5, 6], [7, 8, None]]
        if self.round_number == 2:
            my_puzzle = [[None, 1, 5], [4, 3, 2], [7, 8, 6]]
        if self.round_number == 3:
            my_puzzle = [[2, 3, None], [1, 8, 5], [4, 7, 6]]
        if self.round_number == 4:
            my_puzzle = [[1, 6, 2], [4, 3, 8], [7, 5, None]]
        if self.round_number == 5:
            my_puzzle = [[1, 3, 6], [5, 2, 8], [4, 7, None]]
        if self.round_number == 6:
            my_puzzle = [[1, 2, 3], [5, 6, 8], [None, 4, 7]]
        if self.round_number == 7:
            my_puzzle = [[4, 1, 3], [7, None, 6], [5, 2, 8]]
        if formatting == 0:  # returns board
            return my_puzzle
        if formatting == 1:  # returns string
            my_puzzle_str = ''
            for i in range(0, 3):
                for j in range(0, 3):
                    my_puzzle_str = my_puzzle_str + str(my_puzzle[i][j])
            my_puzzle_str = my_puzzle_str.replace('None', '_')
            return my_puzzle_str

    # randomly choose 1 player as the starting player
    def set_starting_player(self):
        self.starting_player = random.choice([player.id_in_group for player in self.get_players()])
        for player in self.get_players():
            player.is_starting_player = self.starting_player == player.id_in_group

    def check_matches(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        if p1.pref == 1 and p2.pref == 1:
            p1.match = 1
            p2.match = 1
        if p1.pref == 0 or p2.pref == 0:
            p1.match = 0
            p2.match = 0

    def pass_matches(self):
        for p in self.get_players():
            if self.round_number == 1:
                p.participant.vars['match_rd1'] = p.match
            if self.round_number == 2:
                p.participant.vars['match_rd2'] = p.match
            if self.round_number == 3:
                p.participant.vars['match_rd3'] = p.match
            if self.round_number == 4:
                p.participant.vars['match_rd4'] = p.match
            if self.round_number == 5:
                p.participant.vars['match_rd5'] = p.match
            if self.round_number == 6:
                p.participant.vars['match_rd6'] = p.match
            if self.round_number == 7:
                p.participant.vars['match_rd7'] = p.match


class Player(BasePlayer):
    # variables for the puzzle
    move_history = models.LongStringField()
    is_starting_player = models.BooleanField()
    puzzle_solved = models.BooleanField(initial=False)
    # variable to store preference and matches
    pref = models.BooleanField(label='',
                               choices=[[1, 'Sì'], [0, 'No'], ])
    match = models.BooleanField()
    # understanding questions
    uq1 = models.IntegerField (
        label = '1. Which of the following statements is true? ',
        widget = widgets.RadioSelect,
        choices = [
            [1, 'In this part, I will choose my partner for part 3.'],
            [2, 'In this part, I will work on the puzzles for 12 minutes in pairs by moving the tiles in turn.'],])
    uq2 = models.IntegerField (
        label = '2. How many people can you choose who you want to work with in Part 3? ',
        widget = widgets.RadioSelect,
        choices = [[1, '1 person.'],
                 [2, '2 persons.'],
                 [3, 'All the people you want.'],])
    uq3 = models.IntegerField (
        label = '3. Why is it important to choose the best partner for part 3? ',
        widget = widgets.RadioSelect,
        choices = [[1, "because how many puzzles I can solve in part 3 depends on my partner's moves."],
                 [2, 'because my partner will solve the puzzles for me.'],])
    uq4 = models.IntegerField (
        label = '4. Suppose you have chosen Giovanni and Valeria. However, while Valeria chose you, Giovanni did not. If we randomly picked you first, who will be your partner for Part 3? ',
        widget = widgets.RadioSelect,
        choices = [[1, 'John'],
                 [2, 'Valeria'],
                 [3, "Someone on the Waiting List"],
                 [4, 'Chosen at random by Giovanni and Valeria'],])
    uq5 = models.IntegerField (
        label = '5. Suppose you have chosen Giovanni and Valeria. However, unlike question 4, while Giovanni chose you, Valeria did not. If we randomly picked you first, who will be your partner for Part 3? ',
        widget = widgets.RadioSelect,
        choices = [[1, 'John'],
                 [2, 'Valeria'],
                 [3, "Someone on the Waiting List"],
                 [4, 'Chosen at random by Giovanni and Valeria'],])
    uq6 = models.IntegerField (
        label = '6. Suppose you have chosen Giovanni and Valeria. Also, both Giovanni and Valeria have chosen you. If we randomly picked you first, who will be your partner for Part 3? ',
        widget = widgets.RadioSelect,
        choices = [[1, 'John'],
                 [2, 'Valeria'],
                 [3, "Someone on the Waiting List"],
                 [4, 'Chosen at random by Giovanni and Valeria'],])
    uq7 = models.IntegerField (
        label = '7. Suppose you have chosen Giovanni and Valeria. Also, both Giovanni and Valeria have chosen you. However, we have already paired Valeria with Giovanni before choosing you. Who will be your partner for part 3? ',
        widget = widgets.RadioSelect,
        choices = [[1, 'John'],
                 [2, 'Valeria'],
                 [3, "Someone on the Waiting List"],
                 [4, 'Chosen at random by Giovanni and Valeria'],])
    uq8 = models.IntegerField (
        label = "8. Suppose you haven't chosen anyone. Also, both Giovanni and Valeria have chosen you. If we randomly picked you first, who will be your partner for Part 3? ",
        widget = widgets.RadioSelect,
        choices = [[1, 'John'],
                 [2, 'Valeria'],
                 [3, "Someone on the Waiting List"],
                 [4, 'Chosen at random by Giovanni and Valeria'],])
    uq9 = models.IntegerField (
        label = '9. Suppose you have chosen Giovanni and Valeria. However, neither Giovanni nor Valeria chose you. If we randomly picked you first, who will be your partner for Part 3? ',
        widget = widgets.RadioSelect,
        choices = [[1, 'John'],
                 [2, 'Valeria'],
                 [3, "Someone on the Waiting List"],
                 [4, 'Chosen at random by Giovanni and Valeria'],])
    # error messages
    def uq1_error_message(self, uq1):
        print(uq1)
        if uq1 != 1:
            return self.session.config['uq_error']

    def uq2_error_message(self, uq2):
        print(uq2)
        if uq2 != 3:
            return self.session.config['uq_error']

    def uq3_error_message(self, uq3):
        print(uq3)
        if uq3 != 1:
            return self.session.config['uq_error']

    def uq4_error_message(self, uq4):
        print(uq4)
        if uq4 != 2:
            return self.session.config['uq_error']

    def uq5_error_message(self, uq5):
        print(uq5)
        if uq5 != 1:
            return self.session.config['uq_error']

    def uq6_error_message(self, uq6):
        print(uq6)
        if uq6 != 4:
            return self.session.config['uq_error']

    def uq7_error_message(self, uq7):
        print(uq7)
        if uq7 != 3:
            return self.session.config['uq_error']

    def uq8_error_message(self, uq8):
        print(uq8)
        if uq8 != 3:
            return self.session.config['uq_error']

    def uq9_error_message(self, uq9):
        print(uq9)
        if uq9 != 3:
            return self.session.config['uq_error']

    def vars_for_template(self):
        otherid = self.get_others_in_group()[0].participant.label
        return dict(otherid=otherid)
