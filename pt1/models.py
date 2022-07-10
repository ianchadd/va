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
Individual round
"""


class Constants(BaseConstants):
    name_in_url = 'pt1'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # define puzzles to play
    def puzzle_to_play(self, formatting):
        my_boards = [
            [[1, 2, 3], [4, 5, 6], [7, None, 8]],
            [[1, 2, 3], [4, None, 5], [7, 8, 6]],
            [[1, 2, 3], [4, 6, None], [7, 5, 8]],
            [[None, 2, 3], [1, 4, 5], [7, 8, 6]],
            [[1, 3, 6], [4, 2, None], [7, 5, 8]],
            [[1, 2, 3], [7, 4, 6], [5, 8, None]],
            [[1, 2, 3], [7, 4, None], [5, 8, 6]],
            [[2, 5, 3], [1, 7, 6], [4, 8, None]],
            [[4, 1, 3], [7, 2, None], [8, 6, 5]],
            [[None, 1, 3], [5, 2, 7], [4, 8, 6]],
            [[2, None, 6], [1, 3, 8], [4, 5, 7]],
            [[4, 1, None], [8, 3, 2], [5, 7, 6]],
            [[1, 5, 2], [None, 7, 6], [3, 4, 8]],
            [[2, 3, 8], [7, 1, 4], [None, 6, 5]],
            [[2, 7, 3], [5, 1, None], [4, 8, 6]],
        ]
        if formatting == 0:  # returns board
            return my_boards
        if formatting == 1:  # returns string
            my_boards_str = []
            for k in range(0, 15):
                my_puzzle_str = ''
                for i in range(0, 3):
                    for j in range(0, 3):
                        my_puzzle_str = my_puzzle_str + str(my_boards[k][i][j])
                my_puzzle_str = my_puzzle_str.replace('None', '_')
                my_boards_str.append(my_puzzle_str)
            return my_boards_str

    # puzzle info
    puzzles_solved_pt1 = models.IntegerField()
    puzzle_histories = models.LongStringField()
    # understanding questions
    uq1 = models.IntegerField(
        label='1. Quale delle seguenti affermazioni è vera?',
        widget=widgets.RadioSelect,
        choices=[
            [1, 'In questa parte, lavorerò sui puzzle individualmente per 4 minuti e guadagnerò 0,2€ per ogni puzzle che risolvo.'],
            [2, 'In questa parte, lavorerò sugli enigmi in coppia per 4 minuti e guadagnerò 0,2€ per ogni puzzle che risolviamo.'],
            [3, 'In questa parte, lavorerò individualmente sui puzzle per 4 minuti, ma non guadagnerò nulla.'], ])
    uq2 = models.IntegerField(
        label="2. Quale dei seguenti puzzle è nell'ordine corretto?",
        widget=widgets.RadioSelect,
        choices=[[1, 'A.'], [2, 'B.'], ])
    uq3 = models.IntegerField(
        label='3. Qual è la strategia da utilizzare per risolvere il puzzle il più velocemente possibile?',
        widget=widgets.RadioSelect,
        choices=[
            [1, "Per prima cosa, sistema le celle della colonna di sinistra nell'ordine corretto, quindi quelle della riga in basso. Riduci sempre al minimo il numero di mosse da fare."],
            [2, "Per prima cosa, sistema le celle della riga superiore nell'ordine corretto, quindi quelle della colonna di destra. Riduci sempre al minimo il numero di mosse da fare."],
            [3, "In primo luogo, sistema le celle della riga superiore nell'ordine corretto, quindi quelle della colonna di sinistra. Riduci sempre al minimo il numero di mosse da fare."], ])
    uq4 = models.IntegerField(
        label='4. Guarda il seguente puzzle. Qual è la mossa giusta?',
        widget=widgets.RadioSelect,
        choices=[[1, 'Sposta il 4 in basso.'], [2, 'Spostare il 7 a sinistra.'], ])
    uq5 = models.IntegerField(
        label='5. Considera il puzzle in questione 4. Qual è il numero minimo di mosse per risolvere il puzzle?',
        widget=widgets.RadioSelect,
        choices=[[1, '2'], [2, '3'], [3, '4'], ])
    uq6 = models.IntegerField(
        label='6. Guarda il seguente puzzle. Qual è la mossa giusta?',
        widget=widgets.RadioSelect,
        choices=[[1, 'Spostare il 5 a sinistra.'], [2, 'Sposta l’8 in alto.'], ])
    uq7 = models.IntegerField(
        label='7. Considera il puzzle in questione 6. Qual è il numero minimo di mosse per risolvere il puzzle?',
        widget=widgets.RadioSelect,
        choices=[[1, '2'], [2, '3'], [3, '4'], ])

    # error messages
    def uq1_error_message(self, uq1):
        print(uq1)
        if uq1 != 1:
            return self.session.config['uq_error']

    def uq2_error_message(self, uq2):
        print(uq2)
        if uq2 != 2:
            return self.session.config['uq_error']

    def uq3_error_message(self, uq3):
        print(uq3)
        if uq3 != 3:
            return self.session.config['uq_error']

    def uq4_error_message(self, uq4):
        print(uq4)
        if uq4 != 2:
            return self.session.config['uq_error']

    def uq5_error_message(self, uq5):
        print(uq5)
        if uq5 != 3:
            return self.session.config['uq_error']

    def uq6_error_message(self, uq6):
        print(uq6)
        if uq6 != 1:
            return self.session.config['uq_error']

    def uq7_error_message(self, uq7):
        print(uq7)
        if uq7 != 1:
            return self.session.config['uq_error']

    # a function to pass vars for later apps
    def pass_variable(self):
        self.participant.vars['puzzles_solved_pt1'] = self.puzzles_solved_pt1

    # a function to add tentative earnings to the build-in payff variable
    def add_payoff(self):
        self.payoff += round(self.session.config['pt1rate'] * self.puzzles_solved_pt1, 2)
