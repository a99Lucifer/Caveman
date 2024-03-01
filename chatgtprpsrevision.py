class Player:
    def __init__(self):
        self.name = ""
        self.points = 0
        self._choice = ""

    @property
    def choice(self):
        return self._choice

    @choice.setter
    def choice(self, value):
        self._choice = value.lower()

    def choose(self):
        self.choice = input(f"{self.name}, select rock, paper, scissors, lizard, or Spock: ")
        print(f"{self.name} selects {self.choice}.")

    def enter_name(self):
        self.name = input("Enter your name: ")
        print(f"Good luck, {self.name}!")


class Round:
    RULES = [
        [0, -1, 1, 1, -1],
        [1, 0, -1, -1, 1],
        [-1, 1, 0, 1, -1],
        [-1, 1, -1, 0, 1],
        [1, -1, 1, -1, 0]
    ]

    ADJECTIVES = [
        [None, "covers", "crushes", "smashes", "vaporizes"],
        ["covers", None, "cuts", "eats", "disproves"],
        ["crushes", "cuts", None, "decapitates", "breaks"],
        ["smashes", "eats", "decapitates", None, "poisons"],
        ["vaporizes", "disproves", "breaks", "poisons", None]
    ]

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def to_numerical_choice(self):
        switcher = {
            "rock": 0,
            "paper": 1,
            "scissors":2,
            "lizard": 3,
            "spock": 4
        }
        return switcher[self.choice.lower()]

    def compare_choices(self):
        return self.RULES[p1.to_numerical_choice()][p2.to_numerical_choice()]

    def get_result_adjective(self):
        return self.ADJECTIVES[p1.to_numerical_choice()][p2.to_numerical_choice()]

    def print_round_result(self, result, adjective):
        if result > 0:
            print(f"{self.p1.choice} {adjective} {self.p2.choice}")
        elif result < 0:
            print(f"{self.p2.choice} {adjective} {self.p1.choice}")
        print(f"Round resulted in a {self.get_result_as_string(result)}!")

    @staticmethod
    def get_result_as_string(result):
        res = {
            0: "draw",
            1: "win",
            -1: "loss"
        }
        return res[result]


class Game:
    def __init__(self):
        self.end_game = False
        self.player1 = Player()
        self.player2 = Player()

    def start(self):
        self.player1.enter_name()
        self.player2.enter_name()

        while not self.end_game:
            round = Round(self.player1, self.player2)
            round.p1.choose()
            round.p2.choose()
            result = round.compare_choices()
            adjective = round.get_result_adjective()
            round.print_round_result(result, adjective)
            self.update_scores(result)
            self.check_end_condition()

    def update_scores(self, result):
        if result > 0:
            self.player1.points += 1
        elif result < 0:
            self.player2.points += 1

    def check_end_condition(self):
        answer = input("Continue game y/n: ")
        if answer != "y":
            print(f"GAME ENDED. {self.player1.name} has {self.player1.points}. {self.player2.name} has {self.player2.points}")
            self.determine_winner()
            self.end_game = True

    def determine_winner(self):
        result_string = "It's a Draw."
        if self.player1.points > self.player2.points:
            result_string = f"{self.player1.name} is the winner!!!"
        elif self.player1.points < self.player2.points:
            result_string = f"{self.player2.name} is the winner!!!"
        print(result_string)


if __name__ == "__main__":
    game = Game()
    game.start()