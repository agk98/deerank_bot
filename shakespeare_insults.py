import random
class Insults:
    def __init__(self):
        self.insults=[
                'Thou art like a toad; ugly and venomous.',
                'Villain, I have done thy mother.',
                'A weasel hath not such a deal of spleen as you are toss’d with.',
                'Thou dost infect my eyes.',
                'You scullion! You rampallian! You fustilarian! I’ll tickle your catastrophe!',
                'Away, you three-inch fool!',
                'Thy tongue outvenoms all the worms of Nile.',
                'Thou art as loathsome as a toad.',
                'Methink\'st thou art a general offence and every man should beat thee',
                'You starveling, you eel-skin, you dried neat’s-tongue, you bull’s-pizzle, you stock-fish–O for breath to utter what is like thee!-you tailor’s-yard, you sheath, you bow-case, you vile standing tuck!',
                'Thou art as fat as butter.',
                'More of your conversation would infect my brain.',
                'Thou sodden-witted lord! Thou hast no more brain than I have in mine elbows!',
                'Your brain is as dry as the remainder biscuit after voyage.',
                'If you spend word for word with me, I shall make your wit bankrupt.',
                'I’ll beat thee, but I would infect my hands.',
                'Thou has not so much brain as ear-wax.',
                'You, minion, are too saucy.',
                'Away, you mouldy rogue, away!',
                'I do desire that we may be better strangers.',
                'Threadbare juggler!',
                'Thou is an eater of broken meats!',
                'There’s no more faith in thee than in a stewed prune.',
                'What a thrice-double ass!',
                'Thou cream faced loon! Where got\'st thou that goose look?',
                'I am sick when I do look on thee.',
                'Your mom\'s a hoe',
                'The sight of thou dost infect my eyes!',
                'Thou have a plentiful lack of wit',
                'Away, you starvelling, you elf-skin, you dried neat\'s-tongue,bull\'s-pizzle, you stock-dish',
                'I scorn you, scurvy companion',
                'Methink\'st thou art a general offence and every man should beat thee.',
                'Thine face is not worth sunburning.',
                'Thou art a boil, a plague sore',
                'Thou is like the toad; ugly and venomous.'
                'Thou damned and luxurious mountain goat.',
                'Thou whoreson zed , thou unnecessary letter!'
        ]

def get_insult():
    insult_object=Insults()
    insult=insult_object.insults[random.randint(0, len(insult_object.insults))]
    return insult