from os import environ
import json

if environ.get('OTREE_PRODUCTION') not in {None, '', '0'}:
    DEBUG = False
    APPS_DEBUG = False
else:
    DEBUG = True
    APPS_DEBUG = True   # also enables random fill in of forms


# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']
sample_participants = []
with open('sample_participants.json') as sample_participants:
    sample_participants=json.load(sample_participants)
SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=1.50, doc="",
    data_pages_enabled=True,
    sample_participants=sample_participants,
    num_sample_participants=10,
    consent_additional_message = """""",
    round_values = ["1.00"],
    piece_rate = 0.25,
    seconds_for_counting_task=5,
    guess_rate = 0.20,
    delay = False,
    consent_link = False,
    consent_url = 'xxxxx'
)


SESSION_CONFIGS = [
    dict(
        name='main_session',
        display_name='Full session',
        num_demo_participants=24,
        app_sequence=['pt0', 'slider_training', 
                      'pt1grp', 'pt2', 'pt2grp',
                      'pt3', 'pt4', 'pt99'
                     ],
        test=0,
        va_probs=[100],
        participation_fee=0,  # this is set to 0 b/c this is added to payoff
        real_world_currency_per_point=1,
        partfee=2,
        pt1rate=0.2,
        pt1qbonus=1, # bonus for answering accuracy question accurately, in usd
        pt3rate=1,
        pt1gender=0, # 0 for male, 1 for female
        failure_tracking=0, # 0 for no move, 1 for bad move
        turnlength=10, # in seconds
        roundlength=4*60, # in seconds, must be divisible by turnlength
        num_part=16,
        max_earning=25,
        uq_error='Check your answer.',
        doc="""
        Program for gender differences in the cost of contradictions.
        Number of participants: multiple of 8.
        Max number of participants: 32 (can be larger, but need to modify codes)
        """
    ),
    dict(
        name='main_session_test',
        display_name='Full session (Shorter version)',
        num_demo_participants=1,
        app_sequence=[
                      #'pt0',
                      'pt1_VA2',
                      #'slider_training',
                      #'pt1grp',
                      #'pt2',
                      #'pt2grp',
                      #'pt3',
                      #'pt4',
                      'pt99'
                     ],
        test=0,
        va_probs=[0, 25, 50, 75, 100],
        participation_fee=0,  # this is set to 0 b/c this is added to payoff
        real_world_currency_per_point=1,
        partfee=2,
        pt1rate=0.2,
        pt1qbonus=1, # bonus for answering accuracy question accurately, in usd
        pt3rate=1,
        pt1gender=1, # 0 for male, 1 for female
        failure_tracking=0, # 0 for no move, 1 for bad move
        turnlength=10, # in seconds
        roundlength=4*60, # in seconds, must be divisible by turnlength
        num_part=16,
        max_earning=25,
        uq_error='Check your answer.',
        doc="""
        Program for gender differences in the cost of contradictions.
        Number of participants: multiple of 8.
        Max number of participants: 32 (can be larger, but need to modify codes)
        """
    ),
]

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
    dict(name='prolific_qsp', display_name='Prolific Room for QSP (no participant labels)'),
    dict(
        name='rpi_lab',
        display_name='RPI Virtual Econ Laboratory'
    ),
    dict(
        name='rpi_lab_qsp_1',
        display_name='RPI Virtual Econ Laboratory: QSP 1'
    ),
    dict(
        name='rpi_lab_qsp_2',
        display_name='RPI Virtual Econ Laboratory: QSP 2'
    ),
    dict(
        name='rpi_lab_qsp_3',
        display_name='RPI Virtual Econ Laboratory: QSP 3'
    ),
    dict(
        name='rpi_lab_qsp_4',
        display_name='RPI Virtual Econ Laboratory: QSP 4'
    ),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""
# extra settings for otreeutils
# ROOT_URLCONF = 'iat_so.urls'
# CHANNEL_ROUTING = 'iat_so.routing.channel_routing'
# don't share this with anybody.
SECRET_KEY = '7vfsh(zo@d)v)zizkf#@xqzb3q%juzu65zoh4r+#$tckdfji5r'

INSTALLED_APPS = ['otree',
                  'custom_templates',
                  'django.contrib.humanize',
                  'otreeutils',
                  'radiogrid'
                  ]
EXTENSION_APPS = ['slider_puzzle']
# inactive session configs
# dict(name='trust', display_name="Trust Game", num_demo_participants=2, app_sequence=['trust', 'payment_info']),
# dict(name='prisoner', display_name="Prisoner's Dilemma", num_demo_participants=2,
#      app_sequence=['prisoner', 'payment_info']),
# dict(name='volunteer_dilemma', display_name="Volunteer's Dilemma", num_demo_participants=3,
#      app_sequence=['volunteer_dilemma', 'payment_info']),
# dict(name='cournot', display_name="Cournot Competition", num_demo_participants=2, app_sequence=[
#     'cournot', 'payment_info'
# ]),
# dict(name='dictator', display_name="Dictator Game", num_demo_participants=2,
#      app_sequence=['dictator', 'payment_info']),
# dict(name='matching_pennies', display_name="Matching Pennies", num_demo_participants=2, app_sequence=[
#     'matching_pennies',
# ]),
# dict(name='traveler_dilemma', display_name="Traveler's Dilemma", num_demo_participants=2,
#      app_sequence=['traveler_dilemma', 'payment_info']),
# dict(name='bargaining', display_name="Bargaining Game", num_demo_participants=2,
#      app_sequence=['bargaining', 'payment_info']),
# dict(name='common_value_auction', display_name="Common Value Auction", num_demo_participants=3,
#      app_sequence=['common_value_auction', 'payment_info']),
# dict(name='bertrand', display_name="Bertrand Competition", num_demo_participants=2, app_sequence=[
#     'bertrand', 'payment_info'
# ]),
# dict(name='public_goods_simple', display_name="Public Goods (simple version from tutorial)",
#      num_demo_participants=3, app_sequence=['public_goods_simple', 'payment_info']),
# dict(name='trust_simple', display_name="Trust Game (simple version from tutorial)", num_demo_participants=2,
#      app_sequence=['trust_simple']),
