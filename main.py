from game_cli import GameCli, CODE_LENGHT, MAX_ROUND
from langage import Langage

class main():

    def __init__(self):
        langage_chosen = self.langage_choice()
        self.lang = Langage(langage_chosen)
        self.welcom()
        diff, lenght, round, emoji = self.custom()
        self.game = GameCli(self.lang, only_text=emoji, easy_off=diff, code_lenght=lenght, max_round=round)
        print(self.lang.howto)
        self.game.main_loop()
    
    def customize(self) -> bool:
        chosen = False
        while not chosen:
            choice = input()
            choice = choice[:].lower().strip()
            if choice in ("", "non", "n", "oui", "o"):
                chosen = True
        return False if choice in ("", "non", "n") else True

    def custom(self):
        print(self.lang.custom)
        customize = self.customize()
        diff_chosen   = True
        emoji_choosen = bool()
        lenght_chosen = CODE_LENGHT
        round_chosen  = MAX_ROUND
        if customize:
            diff_chosen = self.diff_choice()
            lenght_chosen = self.define_number(self.lang.lenght, CODE_LENGHT)
            round_chosen = self.define_number(self.lang.round, MAX_ROUND)
            emoji_chosen = self.choice_emoji()
        return diff_chosen, lenght_chosen, round_chosen, emoji_chosen

    def define_number(self,text, default_data):
        message = text.format(default_data)
        chosen = False
        while not chosen:
            choice = input(message)
            if choice == "":
                break
            try:
                if (default_data/2) <= int(choice) <= (default_data*2):
                    chosen = True
            except ValueError:
                print(self.lang.value_error)
        return int(choice)

    def diff_choice(self) -> bool:
        chosen = False
        while not chosen:
            print(self.lang.diff)
            choice = input()
            choice = choice[:].lower().strip()
            if choice in ("", "n", "no", "non", "y", "yes", "o", "oui"):
                chosen = True
        if choice in ("", "n", "no", "non"):
            choice = True
        else:
            choice = False
        return choice
    

    def choice_emoji(self) -> bool:
        chosen = False
        while not chosen:
            print(self.lang.emoji)
            choice = input()
            choice = choice[:].lower().strip()
            if choice in ("", "n", "no", "non", "y", "yes", "o", "oui"):
                chosen = True
        if choice in ("", "n", "no", "non"):
            choice = True
        else:
            choice = False
        return choice
        
    def welcom(self):
        print(Langage.texts["title"])
        print(self.lang.welcom)
        print(self.lang.intro)

    def langage_choice(self) -> str:
        chosen = False
        while not chosen:
            print(Langage.texts["choose"])
            choice = input()
            choice = choice[:].lower().strip()
            if choice in ("", "1", "2", "en", "fr", "english", "français"):
                chosen = True
        if choice in ("", "1", "fr", "français"):
            choice = "fr"
        else:
            choice = "en"
        return choice
        
APP = main()
