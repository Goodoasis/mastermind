

class Langage:
    texts = {
    "title" : f"{'#'*55}\n\tMasterstermind! 1.0  By: GoodOasis\n{'#'*55}",
    "choose": "Choose your langage:\
                \nChoisissez votre langage:\
                \n\t1: Français\
                \n\t2: English\
                \n(1/2)?",
    "en" : {
        "welcom": "Welcome to the mastermind game!",
        "start": "Search the secret code!\n",
        "intro" : """\
            \nThe goal is to find the secret code. This code usually consists of four to five colored balls.\
            \nClues will be given to each of your proposals in order to find the solution before the end of the twelfth round.\
            \nHere are the colors you will be playing with:\

            \n\t🔵   🔴   🟢   🟡   🟠   🟣   ⚪   ⚫\

            \nand here are the clue pawns:\

            \n\t        ▫️          ⬜           ⬛\

            \nEmpty: No match; White: Good color but bad place; Black: Right color in right place!\
            """,
        "custom": "It is possible to configure the following parameters:\
            \n\t- Put the game in easy mode.\
            \n\t- Change the length of the secret code.\
            \n\t- Change the maximum number of rounds to guess the secret code.\
            \n\t- Refuse the use of emojis to have only text.\
            \n\nDo you want to configure your game? (Yes/No)\
            \n(Leave the field blank to answer 'No')",
        "diff": "Are you putting the game in easy mode? (Type 'help' to know the differences)\
            \n(Leaving the field blank will leave the default choice.)\n",
        "lenght": "Do you want to change the length of the secret code? (Default = {})\
            \n(Leaving the field blank will leave the default choice.)\n",
        "round": "Do you want to change the maximum number of rounds? (Default = {})\
            \n(Leaving the field blank will leave the default choice.)\n",
        "emoji": "Do you want to deny the use of emoji?\
            \n(Leaving the field blank will leave the default choice.)\n",
        "value_error": "Be sure to enter a number.",
        "howto": """\
            \nTo play, you just have to write the colors in full:\
            \n\tblue, red, green yellow, orange, pink, white, black\n\
            \nYou can separate your colors with a space or any punctuation you like.\
            \nIt is possible to use only the first letters of colors. Here they are in the same order as before:\
            \n\tb, r, g, y, o, p, w, d\
            \n("black" changes to "dark" to avoid a duplicate)\
            """,
        "proposal": "What's your {}° proposal?  ",
        "bad_proposal": "\
            It's not correct. Recall:\
            \n\t'blue blue blue blue'   or   'b b b b'",
        "find": "Congratulations! You found the secret code in {} rounds.",
        "not_find": "Whoops! You did not find the secret code.",
        "help": """\
            \nThe secret code can be composed of several balls of the same color.\
            \nIn easy difficulty, the clue pawns are placed just below.\
            \nExample:\

            \n🔴  🟢  🔵  🟣\
            \n⬛  ⬜   ▫️   ▫️\

            \nThe red ball is well positioned, on the other hand the green one is present but not in this position.\
            \nBlue and pink, on the other hand, are to be excluded.\
            \n----------------------------------------------
            \nIn normal difficulty mode, the clue pawns are placed to the right of your balls.\
            \nThe order of the clue pawns does not match the order of your balls.\
            \nExample:\

            \n🟡  🔴  🔴  🟠   ░   ⬛  ⬜  ⬜  ▫️\

            \nThere is a ball which is well placed, two ball which are present but badly placed and a ball to be excluded.\
            \nThe order here doesn't matter and will always be black, white, empty.\
            """
            },
    "fr":{
        "welcom" : "Bienvenue au jeu du mastermind!",
        "start" : "Trouve le code secret!\n",
        "intro" : """\
            \nLe but est de trouver le code secret. Ce code est constitué habituellement de quatre à cinq billes de couleurs.\
            \nDes indices seront données à chacune de vos propostion afin de trouver la solution avant la fin de la douzieme manche.\
            \nVoici les couleurs avec lesquels vous allez jouer:\

            \n🔵   🔴   🟢   🟡   🟠   🟣   ⚪   ⚫\

            \net voici les pions indices:\

            \n        ▫️          ⬜           ⬛\

            \nVide: Aucune correspondance; Blanc: Bonne couleur mais mauvaise place; Noir: Bonne couleur a la bonne place!\
            """,
        "custom": "Il est possible de configurer les paramètres suivant:\
            \n\t- Mettre le jeu en mode facile.\
            \n\t- Changer la longueur du code secret.\
            \n\t- Changer le nombre de round maximum pour deviner le code secret.\
            \n\t- Refuser l'utilisation des emojis pour n'avoir que du texte.\
            \n\nVoulez-vous configurer votre partie? Oui / Non\
            \n(Laisser le champs vide pour répondre 'Non')",
        "diff": "Vous-vous mettre le jeu en mode facile? (tapez 'help' pour connaitre les différences)\
            \n(Laisser le champs vide laissera le choix par défaut.)\n",
        "lenght": "Voulez-vous changer la longueur du code secret? (défaut = {})\
            \n(Laisser le champs vide laissera le choix par défaut.)\n",
        "round": "Voulez-vous changer le nombre de round maximum?  (défaut = {})\
            \n(Laisser le champs vide laissera le choix par défaut.)\n",
        "emoji": "Voulez-vous refuser l'utilisation des emoji?\
            \n(Laisser le champs vide laissera le choix par défaut.)\n",
        "value_error": "Veuillez entrer un chiffre.",
        "howto" : """\
            \nPour jouer, il vous suffira d'écrire en toute lettre les couleurs:\
            \n\tbleu, rouge, vert jaune, orange, rose, blanc, noir\n\
            \nVous pouvez séparer vos couleurs par un espace ou par une ponctuation qui vous plait.\
            \nIl est possible de n'utiliser que les premieres lettres des couleurs anglaise. Les voici dans le même ordre que précédemment:\
            \n\tb, r, g, y, o, p, w, d\
            \n("black" passe à "dark" pour éviter un doublon)\
            """,
        "proposal": "Quelle est votre {}° proposition?  ",
        "bad_proposal": "Ceci n'est pas correct.Rappel:\
                        \n\t'bleu bleu bleu bleu'  ou  'b b b b'",
        "find": "Félicitation! Vous avez trouvé le code secret en {} coups.",
        "not_find": "Oups! Vous n'avez pas trouvé le code secret.",
        "help": """\
            \nLe code secret peut-être composé de plusieurs billes de la même couleur.\
            \nEn mode de difficulté facile, les pions d'incides sont placés juste en dessous.\
            \nExemple:\
            \n\t🔴  🟢  🔵  🟣\
            \n\t⬛  ⬜   ▫️   ▫️\

            \nLa bille rouge est bien positionnée, par contre la verte est présente mais pas à cette position.\
            \nLa bleu et la rose par contre sont à exclure.\
            \n----------------------------------------------\
            \nEn mode de difficulté normale, les pions indices sont placés à droite de vos billes.\
            \nL'odre des pions indices ne cooresponde pas a l'ordre de vos billes.\
            \nExemple:\

            \n\t🟡  🔴  🔴  🟠   ░   ⬛  ⬜  ⬜  ▫️\

            \nIl ya une bille qui est bien placée, deux billes sont présente mais mal placées et une bille est à exclure.\
            \nL'ordre ici n'a pas d'importance et sera toujours noir, blanc, vide.\
            """
        }
    }

    def __init__(self, langage: str ="fr"):
        self.langage = langage
        self.title = self.__class__.texts["title"]
        self.text = self.__class__.texts[langage]

        for k, v in self.text.items():
            self.__setattr__(k, v)

if __name__ == '__main__':
    APP = Langage()
    print(APP.howto)
