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
    age = models.IntegerField (label = 'Age:')
    female = models.BooleanField (
        label = 'Gender:', choices = [[0, 'Male'], [1, 'Female'],])
    region = models.IntegerField (
        label = 'Region of origin:',
        choices = [[1, 'North-West'], [2, 'North-East'], [3, 'Center'], [4, 'South'],
                 [5, 'Islands'], [6, 'Abroad'],])
    major = models.IntegerField (
        label = 'Main field of study:',
        choices = [[1, 'Humanities'], [2, 'Law'],
                 [3, 'Social sciences'], [4, 'Natural sciences / Mathematics'],
                 [5, 'Medicine'], [6, 'Engineering'],])
    prog = models.IntegerField (
        label = 'Course type:',
        choices = [[1, 'Bachelor'], [2, "Master's / Postgraduate"],
                 [3, 'Single cycle (1st, 2nd or 3rd year)'],
                 [4, 'Single cycle (4th year or more)'],
                 [5, 'Doctorate'],])
    freeq1 = models.StringField (
        label = 'What do you think about this study?')
    freeq2 = models.StringField (
        label = "Was there anything unclear or confusing about this study?")
    freeq3 = models.StringField (
        label = 'Do you have any other comments? (optional) ', blank = True)
    puzzle_difficulty = models.IntegerField (
        label = 'Were the puzzles difficult?',
        choices = [[1, 'Difficult'], [2, 'Fairly difficult'],
                 [3, 'Right'], [4, 'Easy enough'],
                 [5, 'Easy'],])

    # survey questions BFI
    bigfive = RadioGridField (
        rows = (
            (1, "is reserved"),
            (2, "generally trusts"),
            (3, "tends to be lazy"),
            (4, "she's relaxed, she tolerates stress well"),
            (5, "has few artistic interests"),
            (6, "is self-confident, sociable"),
            (7, "tends to find faults in others"),
            (8, 'she is conscientious in her work'),
            (9, 'easily stirred'),
            (10, 'has a vivid imagination'),
        ),
        values = (
            (4, "Totally agree"),
            (3, "Fairly agree"),
            (2, "Neither Agree nor Disagree"),
            (1, "Quite Disagree"),
            (0, "Disagree"),
        ),
        require_all_fields = True, verbose_name = 'I see myself as a person who ...',
    null = True)

    extraversion = models.FloatField()
    agreeableness = models.FloatField()
    conscientiousness = models.FloatField()
    neuroticism = models.FloatField()
    openness = models.FloatField()

    def conversion(self, method):
        i, j = Constants.bigfive[method]
        return (6 - int(self.bigfive[i]) + int(self.bigfive[j]))/2

    # survey questions ASI
    genderatt = RadioGridField (
        rows = (
            (1, "Women are too easily offended."),
            (2, "Many women, under the guise of equality, actually seek favoritism, such as employment policies that favor them over men."),
            (3, "To keep their women financially, men should be willing to sacrifice their own well-being."),
            (4, "Many women have a quality of purity that few men possess."),
            (5, "However accomplished he may be, a man is never truly complete as a person if he does not have the love of a woman."),
            (6, "Women tend to exaggerate the problems they have at work."),
        ),
        values = (
            (4, "Totally agree"),
            (3, "Fairly agree"),
            (2, "Neither Agree nor Disagree"),
            (1, "Quite Disagree"),
            (0, "Disagree"),
        ),
        require_all_fields = True, verbose_name = '',
        null = True)

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
