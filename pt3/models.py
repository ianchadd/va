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
Group round.
"""


class Constants(BaseConstants):
    name_in_url = 'pt1_VA'
    players_per_group = 2
    num_rounds = 20


class Subsession(BaseSubsession):
    def group_by_arrival_time_method(self, waiting_players):
        import itertools  # import itertools for groupby()
        import json  # import json for loads
        # define several functions to be used as sorting keys
        def sorting_key_both(pl):  # sort players by mygrp and mygid
            return [pl.participant.vars['mygrp'], pl.participant.vars['mygid']]
        def sorting_key_grp(pl):  # sort players by mygrp
            return pl.participant.vars['mygrp']
        def sorting_key_gid(pl):  # sort players by mygid
            return pl.participant.vars['mygid']
        waiting_players.sort(key=sorting_key_both)
        # create a list in which each element is a list of players belonging to the same mygrp, from grp2 to grpN
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
        pairs = [int(i) for i in json.loads(waiting_players_grped[0][0].participant.vars['mypairs'])]
        waiting_grp.sort(key=sorting_key_gid)
        ind = [i.participant.vars['mygid'] for i in waiting_grp]
        print('Check if there is any match among waiting players of group', waiting_grp_num)
        if pairs[0] in ind and pairs[1] in ind:
            to_be_grpd = [waiting_grp[ind.index(pairs[0])], waiting_grp[ind.index(pairs[1])]]
        elif pairs[2] in ind and pairs[3] in ind:
            to_be_grpd = [waiting_grp[ind.index(pairs[2])], waiting_grp[ind.index(pairs[3])]]
        elif pairs[4] in ind and pairs[5] in ind:
            to_be_grpd = [waiting_grp[ind.index(pairs[4])], waiting_grp[ind.index(pairs[5])]]
        elif pairs[6] in ind and pairs[7] in ind:
            to_be_grpd = [waiting_grp[ind.index(pairs[6])], waiting_grp[ind.index(pairs[7])]]
        else:
            to_be_grpd = []
        if len(to_be_grpd) == 2:
            print('WE PAIR GROUP', waiting_grp_num, 's FOLLOWING PLAYERS:', to_be_grpd)
            return to_be_grpd


class Group(BaseGroup):
    # a variable to flag last round
    last_round = models.BooleanField()
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


    # functions to flag the last round, this occurs when a puzzle is unsolved due to timeout
    def check_results(self):
        self.verify_stored_moves()
        if self.puzzle_solved == 1:
            for p in self.get_players():
                p.puzzles_solved_pt3 = self.round_number
                p.pass_variable()
        if self.puzzle_solved == 0:
            self.last_round = 1

    def puzzle_to_play(self, formatting):
        if self.round_number == 1:
            my_puzzle = [[1, 2, None], [7, 5, 3], [8, 4, 6]]
        if self.round_number == 2:
            my_puzzle = [[4, 1, 2], [7, 5, 3], [8, 6, None]]
        if self.round_number == 3:
            my_puzzle = [[1, 2, 3], [None, 7, 4], [8, 6, 5]]
        if self.round_number == 4:
            my_puzzle = [[1, 2, 3], [5, 8, 7], [4, None, 6]]
        if self.round_number == 5:
            my_puzzle = [[2, 7, 3], [1, None, 6], [5, 4, 8]]
        if self.round_number == 6:
            my_puzzle = [[5, 1, 3], [4, None, 6], [7, 2, 8]]
        if self.round_number == 7:
            my_puzzle = [[1, 5, 2], [7, 3, 6], [8, None, 4]]
        if self.round_number == 8:
            my_puzzle = [[1, 2, 3], [None, 7, 6], [8, 5, 4]]
        if self.round_number == 9:
            my_puzzle = [[1, 7, 3], [4, None, 5], [8, 2, 6]]
        if self.round_number == 10:
            my_puzzle = [[2, 3, 6], [4, None, 5], [7, 1, 8]]
        if self.round_number == 11:
            my_puzzle = [[2, 3, 6], [7, 5, None], [1, 4, 8]]
        if self.round_number == 12:
            my_puzzle = [[1, 3, 4], [None, 7, 2], [8, 6, 5]]
        if self.round_number == 13:
            my_puzzle = [[4, 6, 1], [7, None, 2], [5, 8, 3]]
        if self.round_number == 14:
            my_puzzle = [[7, 4, 1], [3, None, 2], [8, 5, 6]]
        if self.round_number == 15:
            my_puzzle = [[7, 1, 3], [None, 2, 4], [6, 5, 8]]
        if self.round_number == 16:
            my_puzzle = [[4, 1, 2], [None, 3, 6], [8, 5, 7]]
        if self.round_number == 17:
            my_puzzle = [[4, 3, 1], [7, 6, 2], [5, 8, None]]
        if self.round_number == 18:
            my_puzzle = [[None, 4, 1], [3, 8, 5], [7, 6, 2]]
        if self.round_number == 19:
            my_puzzle = [[1, 3, 2], [4, 6, None], [7, 8, 5]]
        if self.round_number == 20:
            my_puzzle = [[7, 4, 1], [None, 3, 2], [6, 8, 5]]
        if formatting == 0:  # returns board
            return my_puzzle
        if formatting == 1:  # returns string
            my_puzzle_str = ''
            for i in range(0, 3):
                for j in range(0, 3):
                    my_puzzle_str = my_puzzle_str + str(my_puzzle[i][j])
            my_puzzle_str = my_puzzle_str.replace('None', '_')
            return my_puzzle_str

    def set_starting_player(self):
        self.starting_player = random.choice([player.id_in_group for player in self.get_players()])
        for player in self.get_players():
            player.is_starting_player = self.starting_player == player.id_in_group


class Player(BasePlayer):
    # variables for the puzzle
    move_history = models.LongStringField()
    is_starting_player = models.BooleanField()
    puzzle_solved = models.BooleanField(initial=False)
    # understanding questions
    uq1 = models.IntegerField (
        label = '1. Which of the following statements is true? ',
        widget = widgets.RadioSelect,
        choices = [[1, 'In this part, you and your partner will earn € 1 for each puzzle solved, which means you will earn € 1 for each puzzle solved.'],
                 [2, 'In this part, you and your partner will earn € 1 for each puzzle solved by the two of you, which means you will earn € 0.5 for each puzzle solved.'],])
    uq2 = models.IntegerField (
        label = '2. You and your partner ... ',
        widget = widgets.RadioSelect,
        choices = [[1, "you will work on the puzzles for 12 minutes by moving the tiles in turn. Which of you will make the first move is determined randomly at the beginning of each puzzle."],
                 [2, "You will work on the puzzles for 12 minutes. Which of you will make the first move is randomly determined at the beginning of this part and fixed later."],])    # count number of puzzles solved
    puzzles_solved_pt3 = models.IntegerField(initial=0)

    # error messages
    def uq1_error_message(self, uq1):
        print(uq1)
        if uq1 != 1:
            return self.session.config['uq_error']

    def uq2_error_message(self, uq2):
        print(uq2)
        if uq2 != 1:
            return self.session.config['uq_error']

    # a function to pass vars for later apps
    def pass_variable(self):
        self.participant.vars['puzzles_solved_pt3'] = self.puzzles_solved_pt3

    def vars_for_template(self):
        otherid = self.get_others_in_group()[0].participant.label
        return dict(otherid=otherid)
