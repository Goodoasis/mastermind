

class Texts:

    texts = {
        "title" : f"{'#'*55}\n\tMasterstermind! 1.0  By: GoodOasis\n{'#'*55}",
        "choose": "Choose your langage:\
                    \nChoisissez votre langage:\
                    \n\t1: FranΓ§ais\
                    \n\t2: English\
                    \n(1/2)?",
        "colors_letter": ["b", "g", "y", "o", "r", "p", "w", "d"],
        "emoji_colors": ["π΅", "π’", "π‘", "π ", "π΄", "π£", "βͺ", "β«"],
        "emoji_clues": [" β«οΈ", "β¬", "β¬"],
        "en" : {
            "colors": ["blue", "green", "yellow", "orange", "red", "pink", "white", "black"],
            "clues": ["blank", "white", "black"],
            "welcom": "Welcome to the mastermind game!",
            "start": "Search the secret code!\n",
            "intro" : """\
                \nThe goal is to find the secret code. This code usually consists of four to five colored balls.\
                \nClues will be given to each of your proposals in order to find the solution before the end of the twelfth round.\
                \nHere are the colors you will be playing with:\

                \n\tπ΅   π’   π‘   π    π΄   π£   βͺ   β«\

                \nand here are the clue pawns:\

                \n\t        β«οΈ          β¬           β¬\

                \nEmpty: No match; White: Good color but bad place; Black: Right color in right place!\
                """,
            "custom": "It is possible to configure the following parameters:\
                \n\t- Put the game in easy mode.\
                \n\t- Change the length of the secret code.\
                \n\t- Change the maximum number of rounds to guess the secret code.\
                \n\t- Allow the code to use the same color more than once.\
                \n\t- Refuse the use of emojis to have only text.\
                \n\nDo you want to configure your game? (Yes/No)\
                \n(Leave the field blank to answer 'No')\n",
            "easy": "Are you putting the game in easy mode? (Type 'help' to know the differences)\
                \n(Leaving the field blank will leave the default choice.)\n",
            "lenght": "Do you want to change the length of the secret code? (Default = {})\
                \n(Leaving the field blank will leave the default choice.)\n",
            "repeat": "Do you want to allow the secret code to use the same color more than once? (Yes/No)\
                \n(Leave the field blank to answer 'No')\n",
            "round": "Do you want to change the maximum number of rounds? (Default = {})\
                \n(Leaving the field blank will leave the default choice.)\n",
            "emoji": "Do you want to deny the use of emoji? (Yes/No)\
                \n(Leave the field blank to answer 'No')\n",
            "value_error": "Be sure to enter a number.",
            "howto": """\
                \nTo play, you just have to write the colors in full:\
                \n\tblue, red, green yellow, orange, pink, white, black\n\
                \nYou can separate your colors with a space or any punctuation you like.\
                \nIt is possible to use only the first letters of colors. Here they are in the same order as before:\
                \n\tb, g, y, o, r, p, w, d\
                \n("black" changes to "dark" to avoid a duplicate)\n\
                """,
            "ready": "The secret code is ready! You must find it in {} maximum moves!\n",
            "proposal": "What's your {}Β° proposal?  ",
            "bad_proposal": "\
                It's not correct. Recall:\
                \n\t'blue blue blue blue'   or   'b b b b'",
            "find": "Congratulations! You found the secret code in {} rounds.",
            "not_find": "Whoops! You did not find the secret code.",
            "help": """\
                \nThe secret code can be composed of several balls of the same color.\
                \nIn easy difficulty, the clue pawns are placed just below.\
                \nExample:\

                \nπ΄  π’  π΅  π£\
                \nβ¬  β¬   β«οΈ   β«οΈ\

                \nThe red ball is well positioned, on the other hand the green one is present but not in this position.\
                \nBlue and pink, on the other hand, are to be excluded.\
                \n----------------------------------------------
                \nIn normal difficulty mode, the clue pawns are placed to the right of your balls.\
                \nThe order of the clue pawns does not match the order of your balls.\
                \nExample:\

                \nπ‘  π΄  π΄  π    β   β¬  β¬  β¬  β«οΈ\

                \nThere is a ball which is well placed, two ball which are present but badly placed and a ball to be excluded.\
                \nThe order here doesn't matter and will always be black, white, empty.\
                """,
            "point": "You have {} points!",
            "stop": "Do you want to stop playing?\
                \n(Leaving the field blank will leave the default choice.)\n",
            "bye": "\nSee you!\n"
                },
        "fr":{
            "colors": ["bleu", "vert", "jaune", "orange", "rouge", "rose", "blanc", "noir"],
            "clues": ["vide", "white", "black"],
            "welcom" : "Bienvenue au jeu du mastermind!",
            "start" : "Trouve le code secret!\n",
            "intro" : """\
                \nLe but est de trouver le code secret. Ce code est constituΓ© habituellement de quatre Γ  cinq billes de couleurs.\
                \nDes indices seront donnΓ©es Γ  chacune de vos propostion afin de trouver la solution avant la fin de la douzieme manche.\
                \nVoici les couleurs avec lesquels vous allez jouer:\

                \nπ΅   π’   π‘   π    π΄   π£   βͺ   β«\

                \net voici les pions indices:\

                \n        β«οΈ          β¬           β¬\

                \nVide: Aucune correspondance; Blanc: Bonne couleur mais mauvaise place; Noir: Bonne couleur Γ  la bonne place!\n\
                """,
            "custom": "Il est possible de configurer les paramΓ¨tres suivant:\
                \n\t- Mettre le jeu en mode facile.\
                \n\t- Changer la longueur du code secret.\
                \n\t- Changer le nombre de round maximum pour deviner le code secret.\
                \n\t- Autoriser le code Γ  utiliser plusieurs fois la mΓͺme couleur.\
                \n\t- Refuser l'utilisation des emojis pour n'avoir que du texte.\
                \n\nVoulez-vous configurer votre partie? (Oui / Non)\
                \n(Laisser le champs vide pour rΓ©pondre 'Non')\n",
            "easy": "Vous-vous mettre le jeu en mode facile? (Oui / Non)\
                \n(Laisser le champs vide pour rΓ©pondre 'Non')\n",
            "lenght": "Voulez-vous changer la longueur du code secret? (dΓ©faut = {})\
                \n(Laisser le champs vide laissera le choix par dΓ©faut.)\n",
            "repeat": "Voulez-vous autoriser le code secret Γ  utiliser plusieurs fois la mΓͺme couleur? (Oui / Non)\
                \n(Laisser le champs vide pour rΓ©pondre 'Non')\n",
            "round": "Voulez-vous changer le nombre de round maximum? (dΓ©faut = {})\
                \n(Laisser le champs vide laissera le choix par dΓ©faut.)\n",
            "emoji": "Voulez-vous refuser l'utilisation des emoji? (Oui / Non)\
                \n(Laisser le champs vide pour rΓ©pondre 'Non')\n",
            "value_error": "Veuillez entrer un chiffre.",
            "howto" : """\
                \nPour jouer, il vous suffira d'Γ©crire en toutes lettres les couleurs:\
                \n\tbleu, vert, jaune, orange, rouge, rose, blanc, noir\n\
                \nVous pouvez sΓ©parer vos couleurs par un espace ou par une ponctuation qui vous plait.\
                \nIl est possible de n'utiliser que les premiΓ¨res lettres des couleurs anglaise. Les voici dans le mΓͺme ordre que prΓ©cΓ©demment:\
                \n\tb, g, y, o, r, p, w, d\
                \n("black" passe Γ  "dark" pour Γ©viter un doublon)\n\
                """,
            "ready": "Le code secret est prΓͺt! Vous devez le trouver en {} coups maximum!\n",
            "proposal": "Quelle est votre {}Β° proposition?  ",
            "bad_proposal": "Ceci n'est pas correct.Rappel:\
                            \n\t'bleu bleu bleu bleu'  ou  'b b b b'",
            "find": "FΓ©licitation! Vous avez trouvΓ© le code secret en {} coups.",
            "not_find": "Oups! Vous n'avez pas trouvΓ© le code secret.",
            "help": """\
                \nLe code secret peut-Γͺtre composΓ© de plusieurs billes de la mΓͺme couleur.\
                \nEn mode de difficultΓ© facile, les pions d'incides sont placΓ©s juste en dessous.\
                \nExemple:\
                \n\tπ΄  π’  π΅  π£\
                \n\tβ¬  β¬   β«οΈ   β«οΈ\

                \nLa bille rouge est bien positionnΓ©e, par contre la verte est prΓ©sente mais pas Γ  cette position.\
                \nLa bleu et la rose par contre sont Γ  exclure.\
                \n----------------------------------------------\
                \nEn mode de difficultΓ© normale, les pions indices sont placΓ©s Γ  droite de vos billes.\
                \nL'odre des pions indices ne cooresponde pas a l'ordre de vos billes.\
                \nExemple:\

                \n\tπ‘  π΄  π΄  π    β   β¬  β¬  β¬  β«οΈ\

                \nIl ya une bille qui est bien placΓ©e, deux billes sont prΓ©sente mais mal placΓ©es et une bille est Γ  exclure.\
                \nL'ordre ici n'a pas d'importance et sera toujours noir, blanc, vide.\
                """,
            "point": "Vous avez {} points.",
            "stop": "Voulez-vous arrΓͺter de jouer? (Oui / Non)\
                \n(Laisser le champs vide pour rΓ©pondre 'Non')\n",
            "bye": "\nA bientΓ΄t!\n"
            }
        }

    def __init__(self, langage: str = "fr"):
        self.langage = langage
        self.title   = self.__class__.texts["title"]
        self._text   = self.__class__.texts[langage]

        for k, v in self._text.items():
            self.__setattr__(k, v)

