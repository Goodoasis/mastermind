from texts import Texts
from api import Computer
from string import punctuation


MAX_ROUND = 12
CODE_LENGHT = 4

PAWN_COLORS = ["blue", "green", "yellow", "orange", "red", "pink", "white", "black"]
PAWN_LETTER = ["b", "g", "y", "o", "r", "p", "w", "d"]
PAWN_EMOJI = Texts.texts["emoji_colors"]
CLUE_COLORS = ["blank", "white", "black"]
CLUE_EMOJI = Texts.texts["emoji_clues"]


class GameCli():
    punc = punctuation.replace(",", '')
     
    def __init__(self,  
                    langage:     Texts,
                    easy:        bool      = False,
                    repeat:      bool      = False,
                    only_text:   bool      = False,
                    max_round:   int       = MAX_ROUND,
                    code_lenght: int       = CODE_LENGHT,
                    pawn_colors: list[str] = PAWN_COLORS,
                    pawn_letter: list[str] = PAWN_LETTER,
                    pawn_emoji:  list[str] = PAWN_EMOJI,
                    clue_colors: list[str] = CLUE_COLORS,
                    clue_emoji:  list[str] = CLUE_EMOJI):

        self.computer       = Computer(code_lenght, easy=easy, repeat_color=repeat)
        self.easy           = easy
        self.code_lenght    = code_lenght
        self.max_round      = max_round
        self.pawn_colors    = pawn_colors
        self.pawn_letter    = pawn_letter
        self.pawn_emoji     = pawn_emoji
        self.clue_colors    = clue_colors
        self.clue_emoji     = clue_emoji
        self.txt            = langage
        self.only_text      = only_text
        self.round          = 0

    def game_loop(self) -> bool:
        self.new_game() 
        not_find = True
        while not_find and self.round < self.max_round:
            self.round += 1
            # Shouble be: 'pink yellow blue green' or 'p y b g'.
            proposal_msg = self.txt.proposal.format(self.round)
            proposal_correct = False
            while not proposal_correct:
                raw_proposal = input(proposal_msg)
                # Get cleanned: ["p", "y", "b", "g"].
                clean_proposal = GameCli.clean_proposal(raw_proposal.lower())
                # True if proposal is writed correctly.
                proposal_correct = self.verify_proposal(clean_proposal)
                if not proposal_correct:
                    print(self.txt.bad_proposal)
            # Formated: [5, 3, 7, 2].
            formated_proposal = self.format_proposal(clean_proposal)
            # Answer raw: [1, 0, 2, 1] ou {0:1, 1:2, 2:1}.
            raw_answer = self.get_api_answer(formated_proposal)
            print("\n", self.repr(formated_proposal, raw_answer), '\n')
            not_find = formated_proposal != self.computer.code  
        if not_find:
            print(self.txt.not_find)
            print(self.repr(self.computer.code).strip(' ░',))
        else:
            print(self.txt.find.format(self.round))
        return not_find
    
    def verify_proposal(self, proposal: list[int]) -> bool:
        pawns = self.pawn_colors + self.pawn_letter
        if len(proposal) == self.code_lenght:
            return all([(i in pawns) for i in proposal])

    def repr(self, proposal: list[int], answer: list[int] = []) -> str:
        visual_proposal = self._swap_proposal(proposal)
        visual_answer = self._swap_answer(answer)
        if not self.easy:
            repr = f"\t{' '.join(visual_proposal)}  ░  {' '.join(visual_answer)}"
        else:
            repr = f"\t{' '.join(visual_proposal)}\n\t{' '.join(visual_answer)}"
        return repr

    def _swap_proposal(self, proposal: list[int]) -> list[str]:
        source = self.pawn_emoji if not self.only_text else self.txt.colors
        return [source[i] for i in proposal]

    def _swap_answer(self, answer: list[int]) -> list[str]:
        source = self.clue_emoji if not self.only_text else self.txt.clues
        if isinstance(answer, list):
            swap_answer = [source[i] for i in answer]
        else:
            swap_answer = []
            for k, v in answer.items():
                for _ in range(v):
                    swap_answer.append(source[k])
        return swap_answer

    @staticmethod
    def clean_proposal(raw_proposal:str) -> list[str]:
        raw_proposal = raw_proposal.replace(" ", ",")
        for i in raw_proposal:
            if i in GameCli.punc:
                raw_proposal = raw_proposal.replace(i, ",")
        result = [word.strip() for word in raw_proposal.split(",") if word.strip()]
        return result
    
    def format_proposal(self, proposal: list[str]) -> list[int]:
        return [self.pawn_colors.index(i) if len(i)>1 else self.pawn_letter.index(i) for i in proposal]

    def get_api_answer(self, proposal:list) -> list:
        answer_raw = self.computer.answer(proposal)
        return answer_raw
    
    def format_answer(self, answer_raw) -> list:
        if isinstance(answer_raw, dict):
            answer_raw = GameCli._anwserdict_tolist(answer_raw)
        return [self.clue_colors[i] for i in answer_raw]

    @staticmethod
    def _anwserdict_tolist(answerdict:dict) -> list:
        answer = []
        for k, v in answerdict.items():
            for _ in range(v):
                answer.append(k)
        return answer

    def new_game(self) -> list[int]:
        secret_code = self.computer.new_code()
        self.round = 0
        print(self.txt.ready.format(self.max_round))
        return secret_code


if __name__ == "__main__":
    txt = Texts("fr")
    TEST = GameCli(easy=True, langage=txt)
    TEST.game_loop()

