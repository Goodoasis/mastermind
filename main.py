from texts import Texts
from game_cli import GameCli, CODE_LENGHT, MAX_ROUND


class main():

    def __init__(self):
        self.points = 0
        langage_chosen = self.langage_choice()
        self.txt = Texts(langage_chosen)
        easy, lenght, round, repeat, emoji = self.custom()
        self.game = GameCli(self.txt, only_text=emoji, easy=easy, code_lenght=lenght, max_round=round, repeat=repeat)
        
        self.welcom()
        self.main_loop()
        self.goodbye()

    def main_loop(self):
        stop = False
        while not stop:
            not_find = self.game.game_loop()
            if not not_find:
                self.points += (self.game.max_round - self.game.round)
            print(self.txt.point.format(self.points))
            stop = self.define_bool(self.txt.stop)
    
    def goodbye(self):
        print(self.txt.bye)
        print(Texts.texts["title"])

    def custom(self) -> tuple:
        customize = self.define_bool(self.txt.custom)
        easy_chosen  = bool()
        repeat_chosen = bool()
        emoji_chosen = bool()
        lenght_chosen = CODE_LENGHT
        round_chosen  = MAX_ROUND
        if customize:
            easy_chosen = self.define_bool(self.txt.easy)
            lenght_chosen = self.define_number(self.txt.lenght, CODE_LENGHT)
            repeat_chosen = self.define_bool(self.txt.repeat)
            round_chosen = self.define_number(self.txt.round, MAX_ROUND)
            emoji_chosen = self.define_bool(self.txt.emoji)
        return easy_chosen, lenght_chosen, round_chosen, repeat_chosen, emoji_chosen

    def define_number(self,text, default_data) -> int:
        message = text.format(default_data)
        chosen = False
        while not chosen:
            choice = input(message)
            if choice:
                try:
                    if (default_data/2) <= int(choice) <= (default_data*2):
                        chosen = True
                except ValueError:
                    print(self.txt.value_error)
            else:
                chosen = True
                choice = bool(choice)
        return int(choice) or default_data
    
    def define_bool(self, text) -> bool:
        chosen = False
        while not chosen:
            choice = input(text)
            choice = choice[:].lower().strip()
            if choice in ("", "n", "no", "non", "y", "yes", "o", "oui"):
                chosen = True
        return choice in ("o", "y", "oui", "yes")
        
    def welcom(self):
        print(Texts.texts["title"])
        print(self.txt.intro)
        print(self.txt.howto)

    def langage_choice(self) -> str:
        chosen = False
        while not chosen:
            print(Texts.texts["choose"])
            choice = input()
            choice = choice[:].lower().strip()
            if choice in ("", "1", "2", "en", "fr", "english", "français"):
                chosen = True
        return "fr" if choice in ("", "1", "fr", "français") else "en"
        
APP = main()
