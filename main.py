from texts import Texts
from game_cli import GameCli, CODE_LENGHT, MAX_ROUND


class Main():
    
    valid_input = ("", "n", "no", "non", "y", "yes", "o", "oui")
    say_yes = ("o", "y", "oui", "yes")

    def __init__(self):
        self.points = int()
        self.txt = Texts(Main.langage_choice())
        easy, lenght, round, repeat, emoji = self.custom()
        self.game = GameCli(self.txt, only_text=emoji, easy=easy, code_lenght=lenght, max_round=round, repeat=repeat)
    
    @staticmethod
    def langage_choice() -> str:
        choice = None
        while not choice in ("", "1", "2", "e", "f", "en", "fr", "english", "français"):
            print(Texts.texts["choose"])
            choice = input().lower().strip()
        return "fr" if choice in ("", "1", "f", "fr", "français") else "en"

    def custom(self) -> tuple[int, bool]:
        customize       = Main._define_bool(self.txt.custom)
        easy_chosen     = bool()
        repeat_chosen   = bool()
        emoji_chosen    = bool()
        lenght_chosen   = CODE_LENGHT
        round_chosen    = MAX_ROUND
        if customize:
            easy_chosen   = Main._define_bool(self.txt.easy)
            lenght_chosen = Main._define_number(self.txt.lenght, CODE_LENGHT, self.txt.value_error)
            repeat_chosen = Main._define_bool(self.txt.repeat)
            round_chosen  = Main._define_number(self.txt.round, MAX_ROUND, self.txt.value_error)
            emoji_chosen  = Main._define_bool(self.txt.emoji)
        return easy_chosen, lenght_chosen, round_chosen, repeat_chosen, emoji_chosen

    def start(self):
        Main.welcom(Texts.texts["title"], self.txt.intro, self.txt.howto)
        self.main_loop(self.game, self.points, self.txt.point, self.txt.stop)
        self.goodbye(self.txt.bye, Texts.texts["title"])
    
    @staticmethod
    def welcom(title: str, intro:str, howto:str):
        print(title)
        print(intro)
        print(howto)

    @staticmethod
    def main_loop(game:GameCli, points:int, txt_point:str, txt_stop:str):
        stop = False
        while not stop:
            not_find = game.game_loop()
            if not not_find:
                points += (game.max_round - game.round)
            print(txt_point.format(points))
            stop = Main._define_bool(txt_stop)
    
    @staticmethod
    def goodbye(bye:str, title:str):
        print(bye)
        print(title)

    @staticmethod
    def _define_number(text, default_data, error) -> int:
        message = text.format(default_data)
        chosen = False
        while not chosen:
            choice = input(message).lower().strip()
            if choice:
                try:
                    if (default_data/2) <= int(choice) <= (default_data*2):
                        chosen = True
                except ValueError:
                    print(error)
            else:
                chosen = True
                choice = bool(choice)
        return int(choice) or default_data
    
    @staticmethod
    def _define_bool(text) -> bool:
        choice = None
        while not choice in Main.valid_input:
            choice = input(text).lower().strip()
        return choice in Main.say_yes

        
APP = Main()
APP.start()