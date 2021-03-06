from random import randint, sample

class Computer():
    def __init__(self,
                    lenght:         int = 4,
                    nb_colors:      int = 7,
                    easy:           bool = False,
                    repeat_color:   bool = False):
        """Class Computer, to Generate secret codes, with any length and any number of colors.
            Can compare proposals with secret code and give an answer.
            The answer in easy mode gives an answer in order for each pawn of the proposition.
            In normal mode only the number of perfect and partial matches are given.

        Args:
            lenght (int, optional): Length of the secret code to be discovered. Defaults to 4.
            nb_colors (int, optional): Select the color number of pawns. Defaults to 8.
            easy (bool, optional): False to easy mode and True to normalmode. Defaults to True.
            repeat_color (bool, optional): TTrue to allow the code to repeat a color. Defaults to False
        """
        self.lenght         = lenght
        self.easy           = easy
        self.colors         = range(nb_colors)
        self.repeat_color   = repeat_color
        self.code           = Computer.create_code(self.colors, lenght, repeat_color)
    
    def answer(self, proposal: list):
        """Call the method corresponding to the chosen difficulty level.

        Args:
            proposal (list): Interger list: Code proposal to analyze.

        Returns:
            List or Dict: Integer list if easy and dict for normal difficulty.
        """
        if self.easy:
            answer = Computer._easy_answer_proposal(self.code, proposal)
        else:
            answer = Computer._answer_proposal(self, self.code, proposal)
        return answer
    
    def new_code(self):
        return Computer.create_code(self.colors, self.lenght)
    
    @staticmethod
    def create_code(colors: list, lenght: int, repeat_color: bool = False) -> list[int]:
        """Generate a random secret code. Heach pawn is defined by a number.

        Args:
            colors (Iterator): Use n time random.randint (n=lenght).
            lenght (Integer): Lenght of code (number of pawn in code).

        Returns:
            List: List with n random pawn.
        """
        if repeat_color:
            return [randint(0, len(colors)) for _ in range(lenght)]
        else:
            return sample(range(len(colors)),k=lenght)
    
    @staticmethod
    def _easy_answer_proposal(code:list, proposal:list) -> list[int]:
        """Compare the proposal with the secret code to return a response.

        Args:
            code (List): Actual secret code.
            proposal (List): list of proposal pawn.

        Returns:
            List: match type(2=perfect match, 1=color match, 0=no) for each proposal pawn.
        """
        answer = []
        matched_index = []
        # find all perfect matches and keep indexes.
        for index, pawn in enumerate(proposal):
            if pawn == code[index]:
                matched_index.append(index)
                answer.append(2)
        # remove pawn already matched.
        clean_code = [j for e, j in enumerate(code) if e not in matched_index]
        for index, pawn in enumerate(proposal):
            if index in matched_index: # If this pawn has already had match, we skip.
                continue
            if pawn in clean_code:
                answer.insert(index, 1) # partiel match.
                clean_code.remove(pawn) # To avoid duplicates.
            else: # If none match the match type is 0.
                answer.insert(index, 0)
        return answer
    
    @staticmethod
    def _answer_proposal(self, code:list, proposal:list) -> dict[int]:
        """Compare the proposal with the secret code to return a response.

        Args:
            code (List): Actual secret code.
            proposal (List): list of proposal pawn.

        Returns:
            Dict: key = match type(2=perfect match, 1=color match, 0=no)value = match number.
        """
        perfects = [i for i, p in enumerate(proposal) if p == code[i]]
        clean_code, clean_proposal = code[:], proposal[:]
        for i in perfects:
            clean_proposal[i] = -2 # Set an invalide number
            clean_code[i] = -1 # again
        matchs = [i for i, p in enumerate(clean_proposal) if p in clean_code]
        nb_blanks = self.lenght - (len(perfects) + len(matchs))
        return {2:len(perfects), 1:len(matchs), 0: nb_blanks}


if __name__ == '__main__':
    test = Computer(4, 7, 0)
    for i in range(10):
        proposal = Computer.create_code(test.colors, test.lenght)
        print("="*26, "\n")
        print(f"Secret Code = {test.code}")
        print(f"Proposal =    {proposal}")
        print("-"*14, "|", " "*10, "|", sep='')
        print(f"Answer =      {test.answer(proposal)}")

