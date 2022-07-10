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
from radiogrid import RadioGridField


author = 'Yuki Takahashi'

doc = """
Follow up survey
"""


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1

    bigfive = dict(extraversion=[0, 5],
                   agreeableness=[6, 1],
                   conscientiousness=[2, 7],
                   neuroticism=[3, 8],
                   openness=[4, 9])
    bigfive_categories = bigfive.keys()
    genderatt = dict(sexism=[0, 1, 2, 3, 4, 5])
    genderatt_categories = genderatt.keys()


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    ...


class Player(BasePlayer):
    # a variable to store payment
    payment = models.FloatField()
    # survey questions demographics
    age = models.IntegerField(label='Età:')
    female = models.BooleanField(
        label='Sesso:', choices=[[0, 'Uomo'], [1, 'Donna'], ])
    region = models.IntegerField(
        label='Regione di origine:',
        choices=[[1, 'Nord-Ovest'], [2, 'Nord-Est'], [3, 'Centro'], [4, 'Sud'],
                 [5, 'Isole'], [6, 'Estero'], ])
    major = models.IntegerField(
        label='Campo di studi principale:',
        choices=[[1, 'Studi umanistici'], [2, 'Giurisprudenza'],
                 [3, 'Scienze sociali'], [4, 'Scienze naturali / Matematica'],
                 [5, 'Medicina'], [6, 'Ingegneria'], ])
    prog = models.IntegerField(
        label='Tipo di corso:',
        choices=[[1, 'Laurea'], [2, 'Laurea Magistrale/Post-Laurea'],
                 [3, 'Ciclo Unico (1 °, 2 ° o 3 ° anno)'],
                 [4, 'Ciclo Unico (4 ° anno o oltre)'],
                 [5, 'Dottorato'], ])
    freeq1 = models.StringField(
        label='Cosa pensi di questo studio?')
    freeq2 = models.StringField(
        label="C'era qualcosa di poco chiaro o di confuso in questo studio?")
    freeq3 = models.StringField(
        label='Hai qualche altro commento? (opzionale)', blank=True)
    puzzle_difficulty = models.IntegerField(
        label='I puzzle erano difficili?',
        choices=[[1, 'Difficili'], [2, 'Abbastanza difficili'],
                 [3, 'Giusto'], [4, 'Abbastanza facili'],
                 [5, 'Facili'], ])

    # survey questions BFI
    bigfive = RadioGridField(
        rows=(
            (1, " è riservata"),
            (2, " generalmente si fida"),
            (3, " tende a essere pigra"),
            (4, " è rilassata, sopporta bene lo stress"),
            (5, " ha pochi interessi artistici"),
            (6, " è spigliata, socievole"),
            (7, " tende a trovare i difetti negli altri"),
            (8, ' è coscienziosa nel lavoro'),
            (9, ' si agita facilmente'),
            (10, ' ha una fervida immaginazione'),
        ),
        values=(
            (4, "Del tutto d’accordo"),
            (3, "Abbastanza d’accordo"),
            (2, "Nè d'accordo né in disaccordo"),
            (1, "Abbastanza in disaccordo"),
            (0, "Per niente d’accordo"),
        ),
        require_all_fields=True, verbose_name='Mi vedo come una persona che...',
    null=True)

    extraversion = models.FloatField()
    agreeableness = models.FloatField()
    conscientiousness = models.FloatField()
    neuroticism = models.FloatField()
    openness = models.FloatField()

    def conversion(self, method):
        i, j = Constants.bigfive[method]
        return (6 - int(self.bigfive[i]) + int(self.bigfive[j]))/2

    # survey questions ASI
    genderatt = RadioGridField(
        rows=(
            (1, " Le donne si offendono troppo facilmente."),
            (2, " Molte donne, sotto la veste dell’uguaglianza, cercano in realtà favoritismi, come per esempio politiche di assunzione che le favoriscano rispetto agli uomini."),
            (3, " Per mantenere economicamente le loro donne, gli uomini dovrebbero essere disposti a sacrificare il proprio benessere."),
            (4, " Molte donne hanno una qualità di purezza che pochi uomini posseggono."),
            (5, " Per quanto realizzato sia, un uomo non è mai veramente completo come persona se non ha l’amore di una donna."),
            (6, " Le donne tendono a ingigantire i problemi che hanno sul lavoro."),
        ),
        values=(
            (4, "Del tutto d’accordo"),
            (3, "Abbastanza d’accordo"),
            (2, "Nè d'accordo né in disaccordo"),
            (1, "Abbastanza in disaccordo"),
            (0, "Per niente d’accordo"),
        ),
        require_all_fields=True, verbose_name='',
        null=True)

    sexism = models.FloatField()

    def conversion_gender(self, method):
        q1, q2, q3, q4, q5, q6 = Constants.genderatt[method]
        index = (int(self.genderatt[q1]) + int(self.genderatt[q2]) +
                 int(self.genderatt[q3]) + int(self.genderatt[q4]) +
                 int(self.genderatt[q5]) + int(self.genderatt[q6])) / 24
        return index

    # payment calculation
    def calc_payment(self):
        self.payment = round(
            self.session.config['partfee'] +
            self.participant.vars['puzzles_solved_pt1'] * self.session.config['pt1rate'] +
            self.participant.vars['puzzles_solved_pt3'] * self.session.config['pt3rate'],
            2)
        self.payoff += self.participant.vars['puzzles_solved_pt3'] * self.session.config['pt3rate']

    # optional question (disclosure of the results)
    send_results = models.BooleanField()
