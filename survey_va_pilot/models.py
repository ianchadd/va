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
    name_in_url = 'demographics_va'
    players_per_group = None
    num_rounds = 1
    decision_template = 'survey_va_pilot/decision_template.html'


states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}
state_list = []
for key in states:
    if key != 'NA':
        state_list.append(key + ' (' + states[key] + ')')

live_state_list = state_list + ['Other (please state below)']
grew_up_state_list = state_list + ['Other (please state below)']

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
#age
    age = models.IntegerField(label='What is your age?', min=13, max=125)
    yob = models.IntegerField(
        label='What is your year of birth?',
        min=1900,
        max=2005
        )

#sex assigned at birth
    sex = models.StringField(
        label = 'What sex were you assigned at birth, on your original birth certificate?',
        choices = ['Male', 'Female']
        )
#gender
    male = models.BooleanField(
        label = 'Male',
        widget=widgets.CheckboxInput,
        blank = True)
    female = models.BooleanField(
        label = 'Female',
        widget=widgets.CheckboxInput,
        initial = False,
        blank = True)
    t_male = models.BooleanField(
        label = 'Trans male / Trans man',
        widget=widgets.CheckboxInput,
        initial = False,
        blank = True)
    t_female = models.BooleanField(
        label = 'Trans female / Trans woman',
        widget=widgets.CheckboxInput,
        initial = False,
        blank = True)
    gnc = models.BooleanField(
        label = 'Genderqueer / Gender non-conforming',
        widget=widgets.CheckboxInput,
        initial = False,
        blank = True)
    nb = models.BooleanField(
        label = 'Nonbinary',
        widget=widgets.CheckboxInput,
        initial = False,
        blank = True)
    other_g = models.BooleanField(
        label = 'Other (please state below)',
        widget=widgets.CheckboxInput,
        initial = False,
        blank = True)
    diff_gend = models.StringField(
        label = '',
        initial = '',
        blank = True)

    def diff_gend_error_message(self,value):
        if self.other_g and type(value) == type(None):
            return 'If you select Other, you must specify in the provided field'

#sexual orientation
    orientation = models.StringField(
        label = 'Which do you consider yourself to be:',
        choices = [
            'Heterosexual or straight',
            'Gay or lesbian',
            'Bisexual',
            'Other (please state below)'
            ],
        widget = widgets.RadioSelect,
        )
    other_orientation = models.StringField(
        label = '',
        initial = '',
        blank = True
        )
#sexual history and attraction
    sex_hist = models.StringField(
        label = 'In the past year, who have you had sex with?',
        choices = [
            'Men only',
            'Women only',
            'Both men and women',
            'I have not had sex',
            'I prefer not to say'],
        widget = widgets.RadioSelect,
        )
    attracted_men = models.BooleanField(
        label = 'Are you sexually attracted to men?',
        choices = [[True,'Yes'],[False,'No']],
        widget = widgets.RadioSelect,
        )
    attracted_women = models.BooleanField(
        label = 'Are you sexually attracted to women?',
        choices = [[True,'Yes'],[False,'No']],
        widget = widgets.RadioSelect,
        )
#relationship status
    relationship = models.StringField(
        label = 'Please indicate your current relationship status',
        choices = [
            'Single',
            'Partnership (not living in the same home)',
            'Domestic Partnership (living in the same home)',
            'Married',
            'Other (please state below)'
            ],
        widget = widgets.RadioSelect
        )
    other_relationship = models.StringField(
        label = '',
        initial = '',
        blank = True)
    primary_earner = models.StringField(
        label = 'Are you the primary earner in the household?',
        choices = [
            'Yes',
            'No',
            'Multiple primary earners in household'
            ],
        widget = widgets.RadioSelect
        )
#income
    income = models.StringField(
        label = "Please select your household annual income from the options below",
        choices = ['less than $20,000','$20,000 - $39,999','$40,000 - $59,999','$60,000 - $79,999','$80,000 - $99,999','$100,000 or more'],
        widget = widgets.RadioSelect
        )
#race
    ethnicity = models.StringField(
        label='What is your ethnicity?',
        choices = [
            'White',
            'Black or African American',
            'American Indian and Alaskan Native',
            'Asian',
            'Native Hawaiian or Pacific Islander',
            'Hispanic or Latino',
            'Middle Eastern or Arab',
            'Other (please state below)'
            ],
        widget = widgets.RadioSelect
        )
    other_ethnicity = models.StringField(
        label = '',
        blank = True
        )
#religion
    religion = models.StringField(
        label = 'What is your religious affiliation?',
        choices = [
            'Christian (any denomination)',
            'Hindu',
            'Buddhist',
            'Jewish',
            'Muslim',
            'Asian Folk Religion (e.g. Taoist, Confucian)',
            'I am not religious',
            'Some other religious affiliation (please specify below)'
            ],
        widget = widgets.RadioSelect
        )
    other_religion = models.StringField(
        label = '',
        blank = True
        )

#politics
    econ_politics = models.StringField(
        label = '',
        choices = ['More conservative than liberal', 'Equally conservative and liberal', 'More liberal than conservative'],
        widget = widgets.RadioSelect
        )

    social_politics = models.StringField(
        label = '',
        choices = ['More conservative than liberal', 'Equally conservative and liberal', 'More liberal than conservative'],
        widget = widgets.RadioSelect
        )
#lgbt_attitude
    #used in Aksoy et al. EER paper
    lgbt_free = models.IntegerField(
        label = 'Do you believe that gay men and lesbians should be free to live their own lives as they wish?',
        choices = [[5,'Strongly Agree'],
                   [4,'Agree'],
                   [3,'Neither Agree nor Disagree'],
                   [2,'Disagree'],
                   [1,'Strongly Disagree']
                   ],
        widget = widgets.RadioSelect
        )


#locations
    live_in = models.StringField(
        label = 'In which US state/territory do you currently live?',
        choices = live_state_list
        )
    grew_up_in = models.StringField(
        label = 'In which US state/territory did you spend the most time in for the first 18 years of your life?',
        choices = grew_up_state_list
        )
    other_live_location = models.StringField(
        label = '',
        blank = True
        )
    other_grew_up_location = models.StringField(
        label = '',
        blank = True
        )
#attention check
    attn_check_1 = models.IntegerField(
        label = '(Attention Check) Please select 1 in the list below.',
        choices = [1,2,3,4,5],
        blank = True
        )

#allyship questions
    consider_lgbt_ally = models.IntegerField(
        label = 'Do you consider yourself to be an ally to the LGBTQ+ community?',
        choices = [[1, 'Yes'],[0,'No']],
        widget = widgets.RadioSelect
        )
    program_lgbt_ally = models.IntegerField(
        label = 'Are you formally registered as an LGBTQ+ ally (e.g. Safe Zone Training, Campus Ally programs, etc.) in your workplace, school, university, or other institution?',
        choices = [[1, 'Yes'],[0,'No']],
        widget = widgets.RadioSelect
        )

#gender attitudes
    #used in Charles et al. (2023)
    FEWORK = models.IntegerField(
        label = 'Do you approve or disapprove of a married woman earning money in business or industry if she has a husband capable of supporting her?',
        choices = [[5,'Strongly Approve'],
                   [4,'Approve'],
                   [3,'Neither Approve nor Disapprove'],
                   [2,'Disapprove'],
                   [1,'Strongly Disapprove']
                   ],
        widget = widgets.RadioSelect
        )

    FEHOME = models.IntegerField(
        label = 'Do you agree or disagree with this statement? Women should take care of running their home and leave running the country up to men.',
        choices = [[5,'Strongly Agree'],
                   [4,'Agree'],
                   [3,'Neither Agree nor Disagree'],
                   [2,'Disagree'],
                   [1,'Strongly Disagree']
                   ],
        widget = widgets.RadioSelect
        )

    FEPRES = models.IntegerField(
        label = 'If your party nominated a woman for president, would you vote for her if she were qualified for the job?',
        choices = [[1,'Yes'],
                   [0,'No'],
                   [-1,"Wouldn't vote"]
                   ],
        widget = widgets.RadioSelect
        )

    FEPOL = models.IntegerField(
        label = 'Do you agree or disagree with this statement? Most men are better suited emotionally for politics than are most women.',
        choices = [[5,'Strongly Agree'],
                   [4,'Agree'],
                   [3,'Neither Agree nor Disagree'],
                   [2,'Disagree'],
                   [1,'Strongly Disagree']
                   ],
        widget = widgets.RadioSelect
        )

    FECHILD = models.IntegerField(
        label = 'Do you agree or disagree with this statement? A working mother can establish just as warm and secure a relationship with her children as a mother who does not work.',
        choices = [[5,'Strongly Agree'],
                   [4,'Agree'],
                   [3,'Neither Agree nor Disagree'],
                   [2,'Disagree'],
                   [1,'Strongly Disagree']
                   ],
        widget = widgets.RadioSelect
        )

    FEPRESCH = models.IntegerField(
        label = 'Do you agree or disagree with this statement? A preschool child is likely to suffer if his or her mother works.',
        choices = [[5,'Strongly Agree'],
                   [4,'Agree'],
                   [3,'Neither Agree nor Disagree'],
                   [2,'Disagree'],
                   [1,'Strongly Disagree']
                   ],
        widget = widgets.RadioSelect
        )

    FEHELP = models.IntegerField(
        label = 'Do you agree or disagree with this statement? It is more important for a wife to help her husband`s career than to have one herself.',
        choices = [[5,'Strongly Agree'],
                   [4,'Agree'],
                   [3,'Neither Agree nor Disagree'],
                   [2,'Disagree'],
                   [1,'Strongly Disagree']
                   ],
        widget = widgets.RadioSelect
        )

    FEFAM = models.IntegerField(
        label = 'Do you agree or disagree with this statement? It is much better for everyone involved if the man is the achiever outside the home and the women takes care of the home and family.',
        choices = [[5,'Strongly Agree'],
                   [4,'Agree'],
                   [3,'Neither Agree nor Disagree'],
                   [2,'Disagree'],
                   [1,'Strongly Disagree']
                   ],
        widget = widgets.RadioSelect
        )

#gender perceptions of VA
    #used in Brenoe et al.
    CGI = models.IntegerField(
        choices = [ [1, 'Very masculine'],
                    [2, 'Somewhat masculine'],
                    [3, 'A little masculine'],
                    [4, 'Neither masculine nor feminine'],
                    [5, 'A little feminine'],
                    [6, 'Somewhat feminine'],
                    [7, 'Very feminine']
        ],
        widget = widgets.RadioSelect
    )
    #BSRI short form

#VA performance perceptions, from Exley and Kessler (2022, QJE)
    #performance bucket, 6 point likert scale, terrible to exceptional
    va_performance_bucket = models.IntegerField(
        choices = [ [1, 'Terrible'],
                    [2, 'Very Poor'],
                    [3, 'Neutral'],
                    [4, 'Good'],
                    [5, 'Very Good'],
                    [6, 'Exceptional'],
        ],
        widget = widgets.RadioSelect
    )
    #continuous response, 0 to 100, agree or disagree with 'The Virtual Assistant Performed Well in the Slider Task'
    va_performance_cts = models.IntegerField(
        min = 0,
        max = 100
    )

#VA/AI Usage questions
    # ChatGPT Questions
    VAFREQ = models.IntegerField(
        label = 'How often do you interact with a virtual voice assistant (e.g., Siri, Alexa, Google Home)?',
        choices = [[5,'Daily'],
                   [4,'Several times a week'],
                   [3,'Once a week'],
                   [2,'Once a month'],
                   [1,'Rarely or never']
        ],
        widget = widgets.RadioSelect
    )

    VAACCESS = models.IntegerField(
        label = 'Do you feel like you have access to VA technology??',
        choices = [[4,'Yes, using a VA is easy and accessible for me'],
                   [3,'No, using a VA hard and unaccessible for me'],
                   [2,'Neutral, I do not feel like VA is neither easy and accesible nor hard an unaccessible']
                   ],
        widget = widgets.RadioSelect()
    )


    VAWORK = models.IntegerField(
        label='Is VA use encouraged at your workplace??',
        choices=[[4, 'Yes, using a VA is encouraged'],
                 [3, 'No, VA use is discouraged'],
                 [2, 'Neutral, VA use is neither discouraged nor encouraged']
                 ],
            widget = widgets.RadioSelect()
    )

    VAGEN = models.IntegerField(
        label='What is the gender of the voice you use for your virtual assistant??',
        choices=[[3, 'Female'],
                 [2, 'Male'],
                 [1, 'Neutal/Robot']
                 ],
        widget=widgets.RadioSelect
    )

    AI_alarms = models.BooleanField(
        label = 'Setting reminders and alarms',
        widget=widgets.CheckboxInput,
        initial = False,
        blank = True)
    AI_info = models.BooleanField(
        label = 'Answering questions and providing information',
        widget=widgets.CheckboxInput,
        initial = False,
        blank = True)
    AI_music = models.BooleanField(
        label = 'Playing music and controlling smart home devices',
        widget=widgets.CheckboxInput,
        initial = False,
        blank = True)
    AI_calls = models.BooleanField(
        label = 'Sending messages and making calls',
        widget=widgets.CheckboxInput,
        initial = False,
        blank = True)
    AI_sched = models.BooleanField(
        label = 'Creating and managing schedules',
        widget=widgets.CheckboxInput,
        initial = False,
        blank = True)
    AI_recs = models.BooleanField(
        label = 'Providing recommendations and suggestions',
        widget=widgets.CheckboxInput,
        initial = False,
        blank = True)
    AI_calcs = models.BooleanField(
        label = 'Performing simple tasks like conversions and calculations',
        widget=widgets.CheckboxInput,
        initial = False,
        blank = True)
    AI_other = models.BooleanField(
        label = 'Other (please state below)',
        widget=widgets.CheckboxInput,
        initial = False,
        blank = True)
    diff_AI = models.StringField(
        label = '',
        initial = '',
        blank = True)

    VATRUST = models.IntegerField(
        label = 'How often much do you trust and follow the output of your virtual voice assistant (e.g., Siri, Alexa, Google Home)?',
        choices = [[6,'Completely, I never double-check'],
                   [5,'I tend to trust what my VA says, but sometimes, I double-check to make sure'],
                   [4,'I double check to make sure about half the time'],
                   [3,'I am more likely to not trust my VA, and more often than not double-check their answer'],
                   [2,'I never trust my VA, and always make sure to double-check'],
                   [1,'I am not a VA user']
                   ],
        widget = widgets.RadioSelect()
    )

    AI_trust_conv = models.BooleanField(
        label = 'Convenience',
        widget=widgets.CheckboxInput,
        initial = False,
        blank = True)
    AI_trust_eff = models.BooleanField(
        label = 'Efficiency',
        widget=widgets.CheckboxInput,
        initial = False,
        blank = True)
    AI_trust_prod = models.BooleanField(
        label = 'Productivity',
        widget=widgets.CheckboxInput,
        initial = False,
        blank = True)
    AI_trust_help = models.BooleanField(
        label = 'Helpful for tasks',
        widget=widgets.CheckboxInput,
        initial = False,
        blank = True)
    AI_trust_acc = models.BooleanField(
        label = 'Accurate responses',
        widget=widgets.CheckboxInput,
        initial = False,
        blank = True)
    AI_trust_rel = models.BooleanField(
        label = 'Technology is reliable',
        widget=widgets.CheckboxInput,
        initial = False,
        blank = True)
    AI_trust_priv = models.BooleanField(
        label = 'Privacy concerns',
        widget=widgets.CheckboxInput,
        initial = False,
        blank = True)
    AI_trust_sec = models.BooleanField(
        label = 'Security concerns',
        widget=widgets.CheckboxInput,
        initial = False,
        blank = True)
    AI_trust_human = models.BooleanField(
        label = 'Lack of human interaction',
        widget=widgets.CheckboxInput,
        initial = False,
        blank = True)
    AI_trust_other = models.BooleanField(
        label='Other (please state below)',
        widget=widgets.CheckboxInput,
        initial=False,
        blank=True)
    diff_AI_trust = models.StringField(
        label='',
        initial='',
        blank=True)


    AI_distrust_conv = models.BooleanField(
        label='Convenience',
        widget=widgets.CheckboxInput,
        initial=False,
        blank=True)
    AI_distrust_eff = models.BooleanField(
        label='Efficiency',
        widget=widgets.CheckboxInput,
        initial=False,
        blank=True)
    AI_distrust_prod = models.BooleanField(
        label='Productivity',
        widget=widgets.CheckboxInput,
        initial=False,
        blank=True)
    AI_distrust_help = models.BooleanField(
        label='Helpful for tasks',
        widget=widgets.CheckboxInput,
        initial=False,
        blank=True)
    AI_distrust_acc = models.BooleanField(
        label='Accurate responses',
        widget=widgets.CheckboxInput,
        initial=False,
        blank=True)
    AI_distrust_rel = models.BooleanField(
        label='Technology is reliable',
        widget=widgets.CheckboxInput,
        initial=False,
        blank=True)

    AI_distrust_priv = models.BooleanField(
        label='Privacy concerns',
        widget=widgets.CheckboxInput,
        initial=False,
        blank=True)
    AI_distrust_sec = models.BooleanField(
        label='Security concerns',
        widget=widgets.CheckboxInput,
        initial=False,
        blank=True)
    AI_distrust_human = models.BooleanField(
        label='Lack of human interaction',
        widget=widgets.CheckboxInput,
        initial=False,
        blank=True)
    AI_distrust_other = models.BooleanField(
        label='Other (please state below)',
        widget=widgets.CheckboxInput,
        initial=False,
        blank=True)
    diff_AI_distrust = models.StringField(
        label='',
        initial='',
        blank=True)

    VAHAPPY = models.IntegerField(
        label='Do you feel happier when using VAs as compared to doing things on your own?',
        choices=[[4, 'Yes, using a VA makes me feel happier'],
                 [3, 'No, using a VA makes me feel less happy'],
                 [2, 'Neutral, using a VA does not affect my happiness'],
                 [1, 'I am not a VA user']
                 ],
        widget=widgets.RadioSelect()
    )

    VAPROD = models.IntegerField(
        label='Do you feel more productive when using VAs as compared to doing things on your own?',
        choices=[[4, 'Yes, using a VA makes me feel more productive'],
                 [3, 'No, using a VA makes me feel less productive'],
                 [2, 'Neutral, using a VA does not affect my productivity'],
                 [1, 'I am not a VA user']
                 ],
        widget=widgets.RadioSelect()
    )

### CHATGPT Questions From CATA

    GPTFAM = models.IntegerField(
        label = "How familiar are you with ChatGPT?",
        choices = [
            [1, "I have not heard of it"],
            [2, "I have heard of it but have not used it myself"],
            [3, "I use it occasionally"],
            [4, "I use it all the time"]
        ],
        widget = widgets.RadioSelect()
    )

    GPTSTART = models.IntegerField(
        label = 'Around when did you start using ChatGPT? Please select your best guess if you do not remember.',
        choices = [
            [1, 'December 2022'],
            [2, 'January 2023'],
            [3, 'February 2023'],
            [4, 'March 2023'],
            [5, 'April 2023'],
            [6, "I don't use it"]
        ],
        widget = widgets.RadioSelect()
    )

    GPTPROL = models.IntegerField(
        label = 'Have you used ChatGPT in your Prolific work?',
        choices = [
            [1, "No, ChatGPT cannot help me in my Prolific work"],
            [2, "No, I do not use ChatGPT even though it is possible to use it in my Prolific work"],
            [3, "Yes, I have used ChatGPT occasionally in my Prolific work"],
            [4, "Yes, ChatGPT is a main resource for my Prolific work"]
        ],
        widget = widgets.RadioSelect()
    )

    GPT_USE_time = models.BooleanField(
        label='Save time',
        widget=widgets.CheckboxInput,
        initial=False,
        blank=True)
    GPT_USE_accu = models.BooleanField(
        label='Increase accuracy or work quality',
        widget=widgets.CheckboxInput,
        initial=False,
        blank=True)
    GPT_USE_comp = models.BooleanField(
        label='Increasing chances of beating others in tasks that involve competition',
        widget=widgets.CheckboxInput,
        initial=False,
        blank=True)
    GPT_USE_bonus = models.BooleanField(
        label='Increasing chances of earning bonuses',
        widget=widgets.CheckboxInput,
        initial=False,
        blank=True)
    GPT_USE_none = models.BooleanField(
        label='I do not see any advantages',
        widget=widgets.CheckboxInput,
        initial=False,
        blank=True)
    GPT_USE_other = models.BooleanField(
        label='Other. Please write down:',
        widget=widgets.CheckboxInput,
        initial=False,
        blank=True)
    diff_GPT_USE = models.StringField(
        label='',
        initial='',
        blank=True)

    GPTCHEAT_PRO = models.IntegerField(
        label = 'Using ChatGPT as an aid in Prolific work is equivalent to cheating',
        choices = [
            [5, 'Completely agree'],
            [4, 'Somewhat agree'],
            [3, 'Neither agree nor disagree'],
            [2, 'Somewhat disagree'],
            [1, 'Completely disagree']
        ],
        widget = widgets.RadioSelect()
    )

    GPTCHEAT_EDU = models.IntegerField(
        label = 'Using ChatGPT as an aid in schoolwork is equivalent to cheating',
        choices = [
            [5, 'Completely agree'],
            [4, 'Somewhat agree'],
            [3, 'Neither agree nor disagree'],
            [2, 'Somewhat disagree'],
            [1, 'Completely disagree']
        ],
        widget = widgets.RadioSelect()
    )

    GPTPROD_PRO = models.IntegerField(
        label = 'ChatGPT is a tool to increase productivity in Prolific work',
        choices = [
            [5, 'Completely agree'],
            [4, 'Somewhat agree'],
            [3, 'Neither agree nor disagree'],
            [2, 'Somewhat disagree'],
            [1, 'Completely disagree']
        ],
        widget = widgets.RadioSelect()
    )

    GPTLEARN_EDU = models.IntegerField(
        label = 'ChatGPT is a tool to enhance learning in school',
        choices = [
            [5, 'Completely agree'],
            [4, 'Somewhat agree'],
            [3, 'Neither agree nor disagree'],
            [2, 'Somewhat disagree'],
            [1, 'Completely disagree']
        ],
        widget = widgets.RadioSelect()
    )

    GPTFAIR_PRO = models.IntegerField(
        label = 'Using ChatGPT as an aid in Prolific work is unfair to other Prolific workers',
        choices = [
            [5, 'Completely agree'],
            [4, 'Somewhat agree'],
            [3, 'Neither agree nor disagree'],
            [2, 'Somewhat disagree'],
            [1, 'Completely disagree']
        ],
        widget = widgets.RadioSelect()
    )

    GPTFAIR_EDU = models.IntegerField(
        label = 'Using ChatGPT as an aid in schoolwork is unfair to other students',
        choices = [
            [5, 'Completely agree'],
            [4, 'Somewhat agree'],
            [3, 'Neither agree nor disagree'],
            [2, 'Somewhat disagree'],
            [1, 'Completely disagree']
        ],
        widget = widgets.RadioSelect()
    )

    GPTFAIR_COMP = models.IntegerField(
        label = 'Using ChatGPT as an aid is fair game when competing against others',
        choices = [
            [5, 'Completely agree'],
            [4, 'Somewhat agree'],
            [3, 'Neither agree nor disagree'],
            [2, 'Somewhat disagree'],
            [1, 'Completely disagree']
        ],
        widget = widgets.RadioSelect()
    )

    GPTABILITY = models.IntegerField(
        label = 'Lower-ability workers are helped more by ChatGPT than higher-ability workers',
        choices = [
            [5, 'Completely agree'],
            [4, 'Somewhat agree'],
            [3, 'Neither agree nor disagree'],
            [2, 'Somewhat disagree'],
            [1, 'Completely disagree']
        ],
        widget = widgets.RadioSelect()
    )

    GPTGENDER = models.IntegerField(
        label = 'My general sense is that female workers are more likely to use ChatGPT as an aid in Prolific work than male workers',
        choices = [
            [5, 'Completely agree'],
            [4, 'Somewhat agree'],
            [3, 'Neither agree nor disagree'],
            [2, 'Somewhat disagree'],
            [1, 'Completely disagree']
        ],
        widget = widgets.RadioSelect()
    )

    GPTSKILLS = models.IntegerField(
        label = 'ChatGPT is mostly a tool complementing skills rather than substituting effort',
        choices = [
            [5, 'Completely agree'],
            [4, 'Somewhat agree'],
            [3, 'Neither agree nor disagree'],
            [2, 'Somewhat disagree'],
            [1, 'Completely disagree']
        ],
        widget = widgets.RadioSelect()
    )


    GPTCREATIVE = models.IntegerField(
        label = 'I feel like using ChatGPT makes me more creative',
        choices = [
            [5, 'Completely agree'],
            [4, 'Somewhat agree'],
            [3, 'Neither agree nor disagree'],
            [2, 'Somewhat disagree'],
            [1, 'Completely disagree']
        ],
        widget = widgets.RadioSelect()
    )


#what did you think this study was about?

#
