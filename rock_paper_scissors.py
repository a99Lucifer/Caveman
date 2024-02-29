
class Player:
    def __init__(self):
        self.name = ""
        self.points = 0
        self.choice = ""

    def choose(self):
        self.choice = input(f"{self.name}, select rock, paper, scissors, lizard, or Spock: ")
        print(f"{self.name} selects {self.choice}.")

    def enterName(self):
        self.name = input("Enter your name: ")
        print(f"Good luck, {self.name}!")

    def toNumericalChoice(self):
        switcher = {
            "rock": 0,
            "paper": 1,
            "scissors":2,
            "lizard": 3,
            "spock": 4
        }
        return switcher[self.choice.lower()]

    def incrementPoint(self):
        self.points += 1

class Round:
    def __init__(self, p1, p2):
        self.rules = [
            [0, -1, 1, 1, -1],
            [1, 0, -1, -1, 1],
            [-1, 1, 0, 1, -1],
            [-1, 1, -1, 0, 1],
            [1, -1, 1, -1, 0]
        ]

        self.adjectives = [
            [None, None, "Crushes", "Smashes", None],
            ["Covers", None, None, None, "Disproves"],
            [None, "Cuts", None, "decapitates", None],
            [None, "Eats", None, None, "Poisons"],
            ["Vaporizes", None, "breaks", None, None]
        ]

        p1.enterName()
        p1.choose()
        p2.enterName()
        p2.choose()
        adjective = self.getResultAdjective(p1, p2)
        result = self.compareChoices(p1, p2)
        string_result = self.getResultAsString(result)
        if self.rules[p1.toNumericalChoice()] != self.rules[p2.toNumericalChoice()]:
            print(f"{p1.choice} {adjective} {p2.choice}")
        print(f"Round resulted in a {string_result}!")
        if result > 0:
            p1.incrementPoint()
        elif result < 0:
            p2.incrementPoint()

    def compareChoices(self, p1, p2):
        return self.rules[p1.toNumericalChoice()][p2.toNumericalChoice()]

    def getResultAsString(self, result):
        res = {
            0: "draw",
            1: "win",
            -1: "loss"
        }
        return res[result]

    def getResultAdjective(self, p1, p2):
        return self.adjectives[p1.toNumericalChoice()][p2.toNumericalChoice()]
        
        #adjective = ["crushes", "smashes", "covers", "disproves", "cuts", "decapitates", "poisons", "eats", "breaks", "vaporizes"]


class Game:
    def __init__(self):
        self.endGame = False
        self.player1 = Player()
        self.player2 = Player()

    def start(self):
        while not self.endGame:
            Round(self.player1, self.player2)
            self.checkEndCondition()

    def checkEndCondition(self):
        answer = input("Continue game y/n: ")
        if answer == "y":
            Round(self.player1, self.player2)
            self.checkEndCondition()
        else:
            print(f"GAME ENDED. {self.player1.name} has {self.player1.points}. {self.player2.name} has {self.player2.points}")
            self.determineWinner()
            self.endGame = True

    def determineWinner(self):
        resultString = "It's a Draw."
        if self.player1.points > self.player2.points:
            resultString = f"{self.player1.name} is the winner!!!"
        elif self.player1.points < self.player2.points:
            resultString = f"{self.player2.name} is the winner!!!"
        print(resultString)

game = Game()
game.start()