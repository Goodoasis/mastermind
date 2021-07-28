from api import Computer
from string import punctuation


SEP = ','
MAX_ROUND = 12
CODE_LENGHT = 4
#                0       1       2         3        4        5        6        7
PAWN_COLORS = ["blue", "red", "green", "yellow", "orange", "pink", "white", "black"]
PAWN_LETTER = ["b", "r", "g", "y", "o", "p", "w", "d"]
PAWN_EMOJI = ["🔵", "🔴", "🟢", "🟡", "🟠", "🟣", "⚪", "⚫"]
CLUE_COLORS = ["blank", "white", "black"]
CLUE_EMOJI = [" ▫️", "⬜", "⬛"]


class Main():
     
    def __init__(self,  
                easy_off: bool = True,
                max_round: int = MAX_ROUND,
                code_lenght: int = CODE_LENGHT,
                pawn_colors: list[str] = PAWN_COLORS,
                pawn_letter: list[str] = PAWN_LETTER,
                pawn_emoji: list[str] = PAWN_EMOJI,
                clue_colors: list[str] = CLUE_COLORS,
                clue_emoji: list[str] = CLUE_EMOJI,
                sep: str = SEP
                ):
        self.easy_off = easy_off
        self.sep = sep
        self.punctuation = punctuation.replace(self.sep, '')
        self.round = 0
        self.max_round = max_round
        self.code_lenght = code_lenght
        self.computer = Computer(code_lenght, difficulty=easy_off)
        self.pawn_colors = pawn_colors
        self.pawn_letter = pawn_letter
        self.pawn_emoji = pawn_emoji
        self.clue_colors = clue_colors
        self.clue_emoji = clue_emoji

    def main_loop(self):
        secret_code = self.new_game()
        ### Objet a part genre GameConfig
        ### TITLE
        ### CHOIX DE LA LANGUE EN/FR
        ### MESSAGE BIENVENUE
        ### PAR DEFAUT OU PERSONNALISE OU HELP:
            ### CHOIX DU NIVEAU DE DIFFICULTE
            ### CHOIX DU NOMBRE DE COULEURS
            ### CHOIX DE LA LONGUEUR DU CODE SECRET
            ### CHOIX EMOJI
        ### START
        

        not_find = True
        while not_find and self.round < self.max_round:
            self.round += 1 # Fin du round.
            # Proposition en tout lettre exemple: pink, yellow ,black, Green.
            # CHOIX DE LA LANGUE!!
            proposal_msg = f"What's your {self.round}° proposal?\n\t"
            proposal_correct = False
            while not proposal_correct:
                brut_proposal = input(proposal_msg)
                # cleanned: ["pink", "yellow", "black", "green"].
                clean_proposal = self.clean_proposal(brut_proposal.lower())
                # True if colors are writed correctly.
                proposal_correct = self.verify_proposal(clean_proposal)
                if not proposal_correct:
                    # CHOIX DE LA LANGUE
                    print("not correct!")
            # Formated: [5, 3, 7, 2].
            formated_proposal = self.format_proposal(clean_proposal)
            # Réponse brut: [1, 0, 2, 1] ou {0:1, 1:2, 2:1}.
            brut_answer = self.get_api_answer(formated_proposal)
            # Formated Réponse = 'white  blanck  black  white' ou 'black  white  white  blanck'.
            # formated_answer = self.format_answer(brut_answer)
            emoji_repr = self.emoji_repr(formated_proposal, brut_answer)
            print("\n", emoji_repr, '\n')
            #print(f"Answer: {' '.join(formated_answer)}\n\n")
            if formated_proposal == self.computer.code: # Si code proposé == code secret.
                not_find = False
                
        if not_find:
            # CHOIX DE LA LANGUE
            print("Oops! You didn't find the secret code!")
            print(self.emoji_repr(secret_code))
        else:
            # CHOIX DE LA LANGUE
            print(f"Finish you find the secret code in {self.round} rounds!")
    
    def verify_proposal(self, proposal: list[int]) -> bool:
        pawns = self.pawn_colors + self.pawn_letter
        if len(proposal) == self.code_lenght:
            return all([(i in pawns) for i in proposal]) 
        else:
            return False

    def emoji_repr(self, proposal: list[str], answer: list[str] = []) -> str:
        emoji_proposal = self._swap_emoji_proposal(proposal)
        emoji_answer = self._swap_emoji_answer(answer)
        if self.easy_off:
            emoji_repr = f"\t{' '.join(emoji_proposal)}  ░  {' '.join(emoji_answer)}"
        else:
            emoji_repr = f"\t{' '.join(emoji_proposal)}\n\t{' '.join(emoji_answer)}"
        return emoji_repr

    
    def _swap_emoji_proposal(self, proposal: list[str]) -> list[str]:
        return [self.pawn_emoji[i] for i in proposal]
    
    def _swap_emoji_answer(self, answer: list[str]) -> list[str]:
        if isinstance(answer, list):
            emoji_answer = [self.clue_emoji[i] for i in answer]
        else:
            emoji_answer = []
            for k, v in answer.items():
                for _ in range(v):
                    emoji_answer.append(self.clue_emoji[k])
        return emoji_answer
    
    def clean_proposal(self, brut_proposal:str) -> list[str]:
        brut_proposal = brut_proposal.replace(" ", self.sep)
        for i in brut_proposal:
            if i in self.punctuation:
                brut_proposal = brut_proposal.replace(i, self.sep)
        result = [word.strip() for word in brut_proposal.split(self.sep) if word.strip()]
        return result
    
    def format_proposal(self, proposal: list[str]) -> list[int]:
        return [self.pawn_colors.index(i) if len(i)>1 else self.pawn_letter.index(i) for i in proposal]

    def get_api_answer(self, proposal:list) -> list:
        answer_brut = self.computer.answer(proposal)
        return answer_brut
    
    def format_answer(self, answer_brut) -> list:
        if isinstance(answer_brut, dict):
            answer_brut = self._anwserdict_tolist(answer_brut)
        return [self.clue_colors[i] for i in answer_brut]

    def _anwserdict_tolist(self, answerdict:dict) -> list:
        answer = []
        for k, v in answerdict.items():
            for _ in range(v):
                answer.append(k)
        return answer

    def new_game(self) -> list[int]:
        secret_code = self.computer.new_code()
        self.round = 0
        return secret_code



APP = Main(easy_off=False)
APP.main_loop()

# test for inputs fragilities
# proposals = ["blue,blue,blue,blue",
#             "blue blue blue blue",
#             "blue ,blue ,blue, blue",
#             "blue blue blue blue",
#             "?blue blue blue blue!",
#             " blue,blue blue;:, blue",
#             " ,  ,,,   ,,;,,,,,, blue,,  blue; ,blue ,,,blue:  ,!"     
#             ]
# good = ["blue","blue","blue","blue"]
# for i in proposals:
#     o = APP.clean_proposal(i)
#     if o == good:
#         print(f"YEAH! result = {o}")
#     else:
#         print(f"OOps! result = {o}")