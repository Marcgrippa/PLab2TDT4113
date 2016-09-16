from abc import ABCMeta
import random
import matplotlib.pyplot as plt
import numpy as np

RPS = ("rock", "paper", "scissors")


def move_to_number(move):
    if move == "rock":
        return 0
    elif move == "paper":
        return 1
    elif move == "scissors":
        return 2
    else:
        raise Exception("Don't you know the game...? child.... ")


class Player:
    # Er en abstrakt klasse som blir ferdig implementert i de andre spillertypene
    __metaclass__ = ABCMeta

    def __init__(self):
        self.points = 0
        self.stat = []

    def choose_action(self):
        raise NotImplementedError

    def receive_result(self, result):
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError


class RandomPlayer(Player):
    #Velger et random trekk som skal bli spilt
    def choose_action(self):
        action = random.randint(0,2)
        if action == 0:
            return "rock"
        elif action == 1:
            return "paper"
        else:
            return "scissors"

    def receive_result(self, result):
        self.points += result
        number_of_games = float(len(self.stat) + 1)
        self.stat.append(self.points/number_of_games)

    def __str__(self):
        return "Random Player"

class SeqentialPlayer(Player):

    def __init__(self):
        super(SeqentialPlayer, self).__init__()
        self.number_of_games = 0

    def choose_action(self):
        #Tar modulo for å hele tiden ta neste i rekken av mulige valg.
        action = self.number_of_games % 3
        self.number_of_games += 1
        if action == 0:
            return "rock"
        elif action == 1:
            return "paper"
        else:
            return "scissors"

    def receive_result(self, result):
        self.points += result
        number_of_games = float(len(self.stat) + 1)
        self.stat.append(self.points/number_of_games)

    def __str__(self):
        return "Sequential Player"


class MostRegular(Player):

    def __init__(self):
        super(MostRegular, self).__init__()
        self.enemy_actions = [0,0,0]
        #Er en String
        self.action = None

    # Finne indexen til det trekket som er spilt mest i forhold til listen RPS
    def highest_action(self):
        highest = 0
        index_of_highest = 0
        for i in range(3):
            if self.enemy_actions[i] > highest:
                highest = self.enemy_actions[i]
                index_of_highest = i
        return index_of_highest

    def choose_action(self):
        sign = self.highest_action()
        self.action = RPS[sign]
        return self.action

    def counter_for_enemy(self, result):
        # Uavgjort
        if result == 1:
            return self.action
        elif result == 2:
            if self.action == "rock":
                return "scissors"
            elif self.action == "paper":
                return "rock"
            else:
                return "paper"

        else:
            if self.action == "rock":
                return "paper"
            elif self.action == "paper" :
                return "scissors"
            else:
                return "rock"

    def receive_result(self, result):
        self.points += result
        number_of_games = float(len(self.stat) + 1)
        self.stat.append(self.points/number_of_games)
        opponents_last_choise = self.counter_for_enemy(result)
        self.enemy_actions[move_to_number(opponents_last_choise)] += 1

    def __str__(self):
        return "MostRegular"


class HistorianPlayer(Player):

    def __init__(self, remember):
        super(HistorianPlayer, self).__init__()
        self.remember = remember
        self.enemy_action = []
        self.action = None

    def choose_action(self):
        # Henter ut det siste trekket
        enemy_last_action = self.enemy_action[-self.remember:len(self.enemy_action)]

        counter = 0
        # Bibliotek
        number_of_sign = {}
        number_after_sequence = []

        highest = 0
        highest_key = 0

        for i in range(len(self.enemy_action)):
            if self.enemy_action[i] == enemy_last_action[counter]:
                counter += 1
                if counter == len(enemy_last_action):
                    try:
                        number_after_sequence.append(self.enemy_action[i+1])
                    except IndexError:
                        break
                    counter = 0
        for sign in number_after_sequence:
            try:
                number_of_sign[sign] += 1
            except:
                number_of_sign[sign] = 1

        for key in number_of_sign:
            if number_of_sign[key] > highest:
                highest = number_of_sign[key]
                highest_key = move_to_number(key)
        self.action = RPS[highest_key]

        return self.action

    def counter_for_enemy(self, result):
        # Uavgjort
        if result == 1:
            return self.action
        elif result == 2:
            if self.action == "rock":
                return "scissors"
            elif self.action == "paper":
                return "rock"
            else:
                return "paper"

        else:
            if self.action == "rock":
                return "paper"
            elif self.action == "paper" :
                return "scissors"
            else:
                return "rock"

    def receive_result(self, result):
        self.points += result
        number_of_games = float(len(self.stat) + 1)
        self.stat.append(self.points/number_of_games)
        enemy_last_action = self.counter_for_enemy(result)
        self.enemy_action.append(enemy_last_action)

    def __str__(self):
        return "Historian"


class Action:

    def __init__(self, action):
        self.action = action

    # Bestemmer hvem som vinner
    def __gt__(self, other):
        if (self.action == "rock" and other.action == "scissors" or
            self.action == "scissors" and other.action == "paper" or
            self.action == "paper" and other.action == "rock"):
            return True
        else:
            return False


    def __lt__(self, other):
        return (not self.__gt__(other) and self != other)

class SingelPlayerGame:
    #Spiller et spill

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.action1 = player1.choose_action()
        self.action2 = player2.choose_action()
        self.winner = None
        self.looser = None



    #Sender resultatet om hvem som vinner og taper
    def send_results(self, winner, looser):
        self.winner.receive_result(1)
        self.looser.receive_result(0)

    def send_results_tie(self):
        self.player1.receive_result(0.5)
        self.player2.receive_result(0.5)


    #Finner ut hvem som vinner av player 1 og player 2
    def find_winner(self):
        #Hvis player 1 vinner over player 2
        if Action(self.action1) > Action(self.action2):
            self.winner = self.player1
            self.looser = self.player2

        #Hvis player 2 vinner over player 1
        elif Action(self.action2) > Action(self.action1):
            self.winner = self.player2
            self.looser = self.player1

    def play_game(self):
        self.find_winner()
        if (self.winner == None):
            self.send_results_tie()
        else:
            self.send_results(self.winner, self.looser)

    def __str__(self):
        if(self.winner == None):
            result = "Tie \n"
        else:
            result = "%s is tha WINNER! " % self.winner + "\n"

        return "%s: " % self.player1 + self.action1 + "\n%s: " % self.player2 + self.action2 + "\n" +  result


class MultipleGames:
    def __init__(self, player1, player2, number_of_games):
        self.player1 = player1
        self.player2 = player2
        self.number_of_games = number_of_games

    def play_single_game(self):
        s_game = SingelPlayerGame(self.player1, self.player2)
        s_game.play_game()
        print(s_game)

    def play_turnament(self):
        winner = None
        for i in range(self.number_of_games):
            self.play_single_game()

        print("%s won " % self.player1 + str(self.player1.points/self.number_of_games*100) + "% of the games")
        print("%s won " % self.player2 + str(self.player2.points/self.number_of_games*100) + "% of the games")


        if self.player1.points > self.player2.points:
            winner = self.player1
        if self.player1.points < self.player2.points:
            winner = self.player2
        if winner != None:
            print("The winner is %s" %winner)
        else:
            print("It's a tie")

    def print_results(self, player):
        x = np.arange(0,self.number_of_games,1)
        plt.plot(x,player.stat)
        plt.ylabel("Points / Game")
        plt.xlabel("Game")
        plt.title("Average points after each game for %s" % player)
        y = np.arange(0,1)
        plt.show()

p1 = RandomPlayer()
p2 = SeqentialPlayer()
p3 = MostRegular()
p4 = HistorianPlayer(2)

mg = MultipleGames(p2,p4, 1000)
mg.play_turnament()

mg.print_results(p4)