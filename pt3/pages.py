from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class RetrieveVars(WaitPage):
    group_by_arrival_time = True

    def is_displayed(self):
        return self.round_number == 1

    def after_all_players_arrive(self):
        for p in self.group.get_players():
            p.pass_variable()


class Partner(Page):
    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        return self.player.vars_for_template()


class Intro(Page):
    def is_displayed(self):
        return self.round_number == 1

    form_model = 'player'
    form_fields = ['uq1', 'uq2']


class WaitPartner(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_starting_player()


class Ready(Page):
    timeout_seconds = 5  # 5 seconds

    def is_displayed(self):
        return self.round_number == 1

    def before_next_page(self):
        import time
        # set global timer here
        if self.session.config['test'] == 1:
            self.participant.vars['expiry'] = time.time() + 60  # 1 minute if test session
        if self.session.config['test'] == 0:
            self.participant.vars['expiry'] = time.time() + 60*12  # 12 minutes if real session


class Game(Page):
    form_model = 'player'
    form_fields = ['puzzle_solved', 'move_history']

    # display manual timer text
    timer_text = 'Time left to complete this part:'

    # call up global timer
    def get_timeout_seconds(self):
        import time
        return self.participant.vars['expiry'] - time.time()

    # skip all the remaining pages if the time is over
    def is_displayed(self):
        return self.get_timeout_seconds() > 0

    def vars_for_template(self):
        return self.player.vars_for_template()

    def js_vars(self):
        if self.group.round_number == 1:
            return {
                'game_id': "%s_%s" % (self.subsession.id, self.group.id),
                'player_id': self.player.id_in_group,
                'starting_player': self.player.id_in_group == self.group.starting_player,
                'board': self.group.puzzle_to_play(formatting=0),
                'first_player': self.player.id_in_group == 1
            }
        if self.group.round_number == 2:
            return {
                'game_id': "%s_%s" % (self.subsession.id, self.group.id),
                'player_id': self.player.id_in_group,
                'starting_player': self.player.id_in_group == self.group.starting_player,
                'board': self.group.puzzle_to_play(formatting=0),
                'first_player': self.player.id_in_group == 1
            }
        if self.group.round_number == 3:
            return {
                'game_id': "%s_%s" % (self.subsession.id, self.group.id),
                'player_id': self.player.id_in_group,
                'starting_player': self.player.id_in_group == self.group.starting_player,
                'board': self.group.puzzle_to_play(formatting=0),
                'first_player': self.player.id_in_group == 1
            }
        if self.group.round_number == 4:
            return {
                'game_id': "%s_%s" % (self.subsession.id, self.group.id),
                'player_id': self.player.id_in_group,
                'starting_player': self.player.id_in_group == self.group.starting_player,
                'board': self.group.puzzle_to_play(formatting=0),
                'first_player': self.player.id_in_group == 1
            }
        if self.group.round_number == 5:
            return {
                'game_id': "%s_%s" % (self.subsession.id, self.group.id),
                'player_id': self.player.id_in_group,
                'starting_player': self.player.id_in_group == self.group.starting_player,
                'board': self.group.puzzle_to_play(formatting=0),
                'first_player': self.player.id_in_group == 1
            }
        if self.group.round_number == 6:
            return {
                'game_id': "%s_%s" % (self.subsession.id, self.group.id),
                'player_id': self.player.id_in_group,
                'starting_player': self.player.id_in_group == self.group.starting_player,
                'board': self.group.puzzle_to_play(formatting=0),
                'first_player': self.player.id_in_group == 1
            }
        if self.group.round_number == 7:
            return {
                'game_id': "%s_%s" % (self.subsession.id, self.group.id),
                'player_id': self.player.id_in_group,
                'starting_player': self.player.id_in_group == self.group.starting_player,
                'board': self.group.puzzle_to_play(formatting=0),
                'first_player': self.player.id_in_group == 1
            }
        if self.group.round_number == 8:
            return {
                'game_id': "%s_%s" % (self.subsession.id, self.group.id),
                'player_id': self.player.id_in_group,
                'starting_player': self.player.id_in_group == self.group.starting_player,
                'board': self.group.puzzle_to_play(formatting=0),
                'first_player': self.player.id_in_group == 1
            }
        if self.group.round_number == 9:
            return {
                'game_id': "%s_%s" % (self.subsession.id, self.group.id),
                'player_id': self.player.id_in_group,
                'starting_player': self.player.id_in_group == self.group.starting_player,
                'board': self.group.puzzle_to_play(formatting=0),
                'first_player': self.player.id_in_group == 1
            }
        if self.group.round_number == 10:
            return {
                'game_id': "%s_%s" % (self.subsession.id, self.group.id),
                'player_id': self.player.id_in_group,
                'starting_player': self.player.id_in_group == self.group.starting_player,
                'board': self.group.puzzle_to_play(formatting=0),
                'first_player': self.player.id_in_group == 1
            }
        if self.group.round_number == 11:
            return {
                'game_id': "%s_%s" % (self.subsession.id, self.group.id),
                'player_id': self.player.id_in_group,
                'starting_player': self.player.id_in_group == self.group.starting_player,
                'board': self.group.puzzle_to_play(formatting=0),
                'first_player': self.player.id_in_group == 1
            }
        if self.group.round_number == 12:
            return {
                'game_id': "%s_%s" % (self.subsession.id, self.group.id),
                'player_id': self.player.id_in_group,
                'starting_player': self.player.id_in_group == self.group.starting_player,
                'board': self.group.puzzle_to_play(formatting=0),
                'first_player': self.player.id_in_group == 1
            }
        if self.group.round_number == 13:
            return {
                'game_id': "%s_%s" % (self.subsession.id, self.group.id),
                'player_id': self.player.id_in_group,
                'starting_player': self.player.id_in_group == self.group.starting_player,
                'board': self.group.puzzle_to_play(formatting=0),
                'first_player': self.player.id_in_group == 1
            }
        if self.group.round_number == 14:
            return {
                'game_id': "%s_%s" % (self.subsession.id, self.group.id),
                'player_id': self.player.id_in_group,
                'starting_player': self.player.id_in_group == self.group.starting_player,
                'board': self.group.puzzle_to_play(formatting=0),
                'first_player': self.player.id_in_group == 1
            }
        if self.group.round_number == 15:
            return {
                'game_id': "%s_%s" % (self.subsession.id, self.group.id),
                'player_id': self.player.id_in_group,
                'starting_player': self.player.id_in_group == self.group.starting_player,
                'board': self.group.puzzle_to_play(formatting=0),
                'first_player': self.player.id_in_group == 1
            }
        if self.group.round_number == 16:
            return {
                'game_id': "%s_%s" % (self.subsession.id, self.group.id),
                'player_id': self.player.id_in_group,
                'starting_player': self.player.id_in_group == self.group.starting_player,
                'board': self.group.puzzle_to_play(formatting=0),
                'first_player': self.player.id_in_group == 1
            }
        if self.group.round_number == 17:
            return {
                'game_id': "%s_%s" % (self.subsession.id, self.group.id),
                'player_id': self.player.id_in_group,
                'starting_player': self.player.id_in_group == self.group.starting_player,
                'board': self.group.puzzle_to_play(formatting=0),
                'first_player': self.player.id_in_group == 1
            }
        if self.group.round_number == 18:
            return {
                'game_id': "%s_%s" % (self.subsession.id, self.group.id),
                'player_id': self.player.id_in_group,
                'starting_player': self.player.id_in_group == self.group.starting_player,
                'board': self.group.puzzle_to_play(formatting=0),
                'first_player': self.player.id_in_group == 1
            }
        if self.group.round_number == 19:
            return {
                'game_id': "%s_%s" % (self.subsession.id, self.group.id),
                'player_id': self.player.id_in_group,
                'starting_player': self.player.id_in_group == self.group.starting_player,
                'board': self.group.puzzle_to_play(formatting=0),
                'first_player': self.player.id_in_group == 1
            }
        if self.group.round_number == 20:
            return {
                'game_id': "%s_%s" % (self.subsession.id, self.group.id),
                'player_id': self.player.id_in_group,
                'starting_player': self.player.id_in_group == self.group.starting_player,
                'board': self.group.puzzle_to_play(formatting=0),
                'first_player': self.player.id_in_group == 1
            }


class CheckResults(WaitPage):
    after_all_players_arrive = 'check_results'


class Proceed(Page):
    def is_displayed(self):
        return self.group.last_round == 1

    def vars_for_template(self):
        num_solved = self.player.participant.vars['puzzles_solved_pt3']
        return dict(num_solved=num_solved)

    def app_after_this_page(self, upcoming_apps): # send players to the next app after timeout
        return "pt4"


page_sequence = [RetrieveVars,
                 Partner,
                 Intro,
                 WaitPartner,
                 Ready,
                 Game,
                 CheckResults,
                 Proceed]
