from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class FormGrp(WaitPage):
    template_name = 'pt2/MyWaitPage.html'
    group_by_arrival_time = True

    body_text = 'Waiting for the other participants to finish the puzzle. '\
                'This may take a few minutes.'


class Intro(Page):
    def is_displayed(self):
        return self.round_number == 1

    form_model = 'player'
    form_fields = ['uq1', 'uq2', 'uq3', 'uq4',
                   'uq5', 'uq6', 'uq7', 'uq8', 'uq9']


class WaitPartners(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_starting_player()


class Game(Page):
    form_model = 'player'
    form_fields = ['puzzle_solved', 'move_history']

    def get_timeout_seconds(self):
        if self.session.config['test'] == 1:
            return 20  # 20 seconds if test session
        if self.session.config['test'] == 0:
            return 2*60  # 2 minutes if real session

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


class Pref(Page):
    def vars_for_template(self):
        return self.player.vars_for_template()

    form_model = 'player'
    form_fields = ['pref']


class CheckMatch(WaitPage):
    def after_all_players_arrive(self):
        self.group.check_matches()
        self.group.pass_matches()
        self.group.verify_stored_moves()


page_sequence = [FormGrp,
                 Intro,
                 WaitPartners,
                 Game,
                 Pref,
                 CheckMatch]
