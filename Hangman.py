import random
from time import sleep

word_list = [
    'wares',
    'soup',
    'mount',
    'extend',
    'brown',
    'expert',
    'tired',
    'humidity',
    'backpack',
    'crust',
    'dent',
    'market',
    'knock',
    'smite',
    'windy',
    'coin',
    'throw',
    'silence',
    'bluff',
    'downfall',
    'climb',
    'lying',
    'weaver',
    'snob',
    'kickoff',
    'match',
    'quaker',
    'foreman',
    'excite',
    'thinking',
    'mend',
    'allergen',
    'pruning',
    'coat',
    'emerald',
    'coherent',
    'manic',
    'multiple',
    'square',
    'funded',
    'funnel',
    'sailing',
    'dream',
    'mutation',
    'strict',
    'mystic',
    'film',
    'guide',
    'strain',
    'bishop',
    'settle',
    'plateau',
    'emigrate',
    'marching',
    'optimal',
    'medley',
    'endanger',
    'wick',
    'condone',
    'schema',
    'rage',
    'figure',
    'plague',
    'aloof',
    'there',
    'reusable',
    'refinery',
    'suffer',
    'affirm',
    'captive',
    'flipping',
    'prolong',
    'main',
    'coral',
    'dinner',
    'rabbit',
    'chill',
    'seed',
    'born',
    'shampoo',
    'italian',
    'giggle',
    'roost',
    'palm',
    'globe',
    'wise',
    'grandson',
    'running',
    'sunlight',
    'spending',
    'crunch',
    'tangle',
    'forego',
    'tailor',
    'divinity',
    'probe',
    'bearded',
    'premium',
    'featured',
    'serve',
    'borrower',
    'examine',
    'legal',
    'outlive',
    'unnamed',
    'unending',
    'snow',
    'whisper',
    'bundle',
    'bracket',
    'deny',
    'blurred',
    'pentagon',
    'reformed',
    'polarity',
    'jumping',
    'gain',
    'laundry',
    'hobble',
    'culture',
    'whittle',
    'docket',
    'mayhem',
    'build',
    'peel',
    'board',
    'keen',
    'glorious',
    'singular',
    'cavalry',
    'present',
    'cold',
    'hook',
    'salted',
    'just',
    'dumpling',
    'glimmer',
    'drowning',
    'admiral',
    'sketch',
    'subject',
    'upright',
    'sunshine',
    'slide',
    'calamity',
    'gurney',
    'adult',
    'adore',
    'weld',
    'masking',
    'print',
    'wishful',
    'foyer',
    'tofu',
    'machete',
    'diced',
    'behemoth',
    'rout',
    'midwife',
    'neglect',
    'mass',
    'game',
    'stocking',
    'folly',
    'action',
    'bubbling',
    'scented',
    'sprinter',
    'bingo',
    'egyptian',
    'comedy',
    'rung',
    'outdated',
    'radical',
    'escalate',
    'mutter',
    'desert',
    'memento',
    'kayak',
    'talon',
    'portion',
    'affirm',
    'dashing',
    'fare',
    'battle',
    'pupil',
    'rite',
    'smash',
    'true',
    'entrance',
    'counting',
    'peruse',
    'dioxide',
    'hermit',
    'carving',
    'backyard',
    'homeless',
    'medley',
    'packet',
    'tickle',
    'coming',
    'leave',
    'swing',
    'thicket',
    'reserve',
    'murder',
    'costly',
    'corduroy',
    'bump',
    'oncology',
    'swatch',
    'rundown',
    'steal',
    'teller',
    'cable',
    'oily',
    'official',
    'abyss',
    'schism',
    'failing',
    'guru',
    'trim',
    'alfalfa',
    'doubt',
    'booming',
    'bruised',
    'playful',
    'kicker',
    'jockey',
    'handmade',
    'landfall',
    'rhythm',
    'keep',
    'reassure',
    'garland',
    'sauna',
    'idiom',
    'fluent',
    'lope',
    'gland',
    'amend',
    'fashion',
    'treaty',
    'standing',
    'current',
    'sharpen',
    'cinder',
    'idealist',
    'festive',
    'frame',
    'molten',
    'sill',
    'glisten',
    'fearful',
    'basement',
    'minutia',
    'coin',
    'stick',
    'featured',
    'soot',
    'static',
    'crazed',
    'upset',
    'robotics',
    'dwarf',
    'shield',
    'butler',
    'stitch',
    'stub',
    'sabotage',
    'parlor',
    'prompt',
    'heady',
    'horn',
    'bygone',
    'rework',
    'painful',
    'composer',
    'glance',
    'acquit',
    'eagle',
    'solvent',
    'backbone',
    'smart',
    'atlas',
    'leap',
    'danger',
    'bruise',
    'seminar',
    'tinge',
    'trip',
    'narrow',
    'while',
    'jaguar',
    'seminary',
    'command',
    'cassette',
    'draw',
    'anchovy',
    'scream',
    'blush',
    'organic',
    'applause',
    'parallel',
    'trolley',
    'pathos',
    'origin',
    'hang',
    'pungent',
    'angular',
    'stubble',
    'painted',
    'forward',
    'saddle',
    'muddy',
    'orchid',
    'prudence',
    'disprove',
    'yiddish',
    'lobbying',
    'neuron',
    'tumor',
    'haitian',
    'swift',
    'mantel',
    'wardrobe',
    'consist',
    'storied',
    'extreme',
    'payback',
    'control',
    'dummy',
    'influx',
    'realtor',
    'detach',
    'flake',
    'consign',
    'adjunct',
    'stylized',
    'weep',
    'prepare',
    'pioneer',
    'tail',
    'platoon',
    'exercise',
    'dummy',
    'clap',
    'actor',
    'spark',
    'dope',
    'phrase',
    'welsh',
    'wall',
    'whine',
    'fickle',
    'wrong',
    'stamina',
    'dazed',
    'cramp',
    'filet',
    'foresee',
    'seller',
    'award',
    'mare',
    'uncover',
    'drowning',
    'ease',
    'buttery',
    'luxury',
    'bigotry',
    'muddy',
    'photon',
    'snow',
    'oppress',
    'blessed',
    'call',
    'stain',
    'amber',
    'rental',
    'nominee',
    'township',
    'adhesive',
    'lengthy',
    'swarm',
    'court',
    'baguette',
    'leper',
    'vital',
    'push',
    'digger',
    'setback',
    'accused',
    'taker',
    'genie',
    'reverse',
    'fake',
    'widowed',
    'renewed',
    'goodness',
    'featured',
    'curse',
    'shocked',
    'shove',
    'marked',
    'interact',
    'mane',
    'hawk',
    'kidnap',
    'noble',
    'proton',
    'effort',
    'patriot',
    'showcase',
    'parish',
    'mosaic',
    'coil',
    'aide',
    'breeder',
    'concoct',
    'pathway',
    'hearing',
    'bayou',
    'regimen',
    'drain',
    'bereft',
    'matte',
    'bill',
    'medal',
    'prickly',
    'sarcasm',
    'stuffy',
    'allege',
    'monopoly',
    'lighter',
    'repair',
    'worship',
    'vent',
    'hybrid',
    'buffet',
    'lively']


def get_word():
    w = random.choice(word_list)
    return w


def hangman():
    stages = [
        "           --------\n"
        "           |      |\n"
        "           |      o\n"
        "           |     /|\\\n"
        "           |      |\n"
        "           |     / \\\n"
        "           -\n",
        "           --------\n"
        "           |      |\n"
        "           |      o\n"
        "           |     /|\\\n"
        "           |      |\n"
        "           |     /\n"
        "           -\n",
        "           --------\n"
        "           |      |\n"
        "           |      o\n"
        "           |     /|\\\n"
        "           |      |\n"
        "           |     \n"
        "           -\n",
        "           --------\n"
        "           |      |\n"
        "           |      o\n"
        "           |     /|\n"
        "           |      |\n"
        "           |     \n"
        "           -\n",
        "           --------\n"
        "           |      |\n"
        "           |      o\n"
        "           |      |\n"
        "           |      |\n"
        "           |     \n"
        "           -\n",
        "           --------\n"
        "           |      |\n"
        "           |      o\n"
        "           |     \n"
        "           |     \n"
        "           |     \n"
        "           -\n",
        "           --------\n"
        "           |      |\n"
        "           |      \n"
        "           |     \n"
        "           |      \n"
        "           |     \n"
        "           -\n"
    ]
    return stages[tries]


win = 0
hanged = False
pa = "Y"
name = input("Hey,What's your name? ")
while win == 1 or hanged != False or pa == "Y":
    tries = 6
    word = get_word().upper()
    guessed_letters = []
    sleep(1)
    print(f"Let's start Hangman! {name}")
    dashes = "-" * len(word)
    while tries != 0:
        print(hangman())
        print(dashes)
        guess = input("Please guess a letter:").upper()
        sleep(1)
        if guess in guessed_letters and guess in word:
            print("Sorry! You already guessed this letter")
            sleep(1)
        elif guess in word:
            print("Good job!Your guess is right")
            dash_as_list = list(dashes)
            index = word.index(guess)
            dash_as_list[index] = guess
            dashes = "".join(dash_as_list)
            guessed_letters.append(guess)
            sleep(1)
        else:
            print("Sorry!Your guess is wrong")
            tries = tries - 1
            sleep(1)
        if dashes.count("-") == 0:
            print("Hurray!You won the game")
            win = 1
            sleep(1)
        if tries == 0:
            print(hangman())
            hanged = True
            print(f"Sorry!You are hanged {name}.")
            print(word)
            sleep(1)
    pa = input("Play again Y/N")
