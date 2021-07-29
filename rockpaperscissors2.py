import random
import getpass
class RockPaperScissors :
    '''class for game Rock, paper, scissors'''

    __counter = 0 # count number of played games
    __computer_score = 0 # computer score after each game
    __player_1_score = 0 # player_1 score after each game
    __player_2_score = 0  # player_2 score after each game
    __tie_game = 0       # number of tie game
       
    def __init__(self):
        ''' method for initializing a Rock, Paper, Scissors .
        Attributes :
        player_selection  (list) : reresent list of three elements '0'Rock, '1'Paper, '2'Scissors.
        '''
        self.player_selection = ["Rock", "Paper", "Scissors"]
        
    def start(self):
        ''' method that ask user if he wants to play a game.
        Args :
            None
        Returns :
            player_answer(int) : 1 if you want to play a game and 0 if you don't
        '''
        user_answer = int(input("Do you want to play a game? select 1 to play 0 no thanks : "))
        if user_answer == 1 :
            self.player_select()
            return self.player_answer
        else :
            print("thanks for you")
            exit()

    def player_select(self) :
        ''' method that ask player to select who's plays with .
        Args :
            None
        Returns :
            None
        '''
        self.player_answer = int(input("Do you want to play vs pc ? select '1' to play vs pc '2' to play vs your friend : "))
        self.players = [0]
        if self.player_answer == 1:
            self.computer_selection = self.player_selection[random.randint(0, 2)]

            self.player_1_selection = int(getpass.getpass("player_1 please select '0' for Rock '1' for paper '2' for Scissors : "))

        elif self.player_answer == 2 :
            self.player_1_selection = int(getpass.getpass("player_1 please select '0' for Rock '1' for paper '2' for Scissors : "))
            self.player_2_selection = int(getpass.getpass("player_2 please select '0' for Rock '1' for paper '2' for Scissors : "))

    def check_winner_computer_vs_you(self):
        ''' method that check who's win the game .
         rock beats scissors and scissors beats paper and paper beats rock
        Args :
            None
        Returns :
            text (str) that tell us who is win the game and the number of played games and the score of each player
        '''
        if self.computer_selection == self.player_selection[self.player_1_selection] :
            RockPaperScissors.__counter += 1
            RockPaperScissors.__tie_game += 1
            RockPaperScissors.__player_1_score = RockPaperScissors.__player_1_score
            RockPaperScissors.__computer_score = RockPaperScissors.__computer_score   
            return f"no winner computer select {self.computer_selection} and you select {self.player_selection[self.player_1_selection]}\n"\
                f"number of game : {RockPaperScissors.__counter}\nnumber of tie game : {RockPaperScissors.__tie_game}\nplayer_score : {RockPaperScissors.__player_1_score}\ncomputer_score : {RockPaperScissors.__computer_score}"
        elif self.computer_selection == 'Rock' :
            if self.player_selection[self.player_1_selection] == 'Sciccors' :
                RockPaperScissors.__counter += 1
                RockPaperScissors.__computer_score += 1
                return f'computer wins! computer select {self.computer_selection} and you select {self.player_selection[self.player_1_selection]}\n'\
                    f"number of game : {RockPaperScissors.__counter}\nnumber of tie game : {RockPaperScissors.__tie_game}\nplayer_score : {RockPaperScissors.__player_1_score}\ncomputer_score : {RockPaperScissors.__computer_score}"
            else :
                RockPaperScissors.__counter += 1
                RockPaperScissors.__player_1_score += 1
                return f'you are winner! you select {self.player_selection[self.player_1_selection]} and computer select {self.computer_selection}\n'\
                    f"number of game : {RockPaperScissors.__counter}\nnumber of tie game : {RockPaperScissors.__tie_game}\nplayer_score : {RockPaperScissors.__player_1_score}\ncomputer_score : {RockPaperScissors.__computer_score}"
        elif self.computer_selection == 'Paper':
            if self.player_selection[self.player_1_selection] == 'Rock':
                RockPaperScissors.__counter += 1
                RockPaperScissors.__computer_score += 1
                return f'computer wins! computer select {self.computer_selection} and you select {self.player_selection[self.player_1_selection]}\n'\
                    f"number of game : {RockPaperScissors.__counter}\nnumber of tie game : {RockPaperScissors.__tie_game}\nplayer_score : {RockPaperScissors.__player_1_score}\ncomputer_score : {RockPaperScissors.__computer_score}"
            else :
                RockPaperScissors.__counter += 1
                RockPaperScissors.__player_1_score += 1
                return f'you are winner! you select {self.player_selection[self.player_1_selection]} and computer select {self.computer_selection}\n'\
                    f"number of game : {RockPaperScissors.__counter}\nnumber of tie game : {RockPaperScissors.__tie_game}\nplayer_score : {RockPaperScissors.__player_1_score}\ncomputer_score : {RockPaperScissors.__computer_score}"
        elif self.computer_selection == 'Scissors':
            if self.player_selection[self.player_1_selection] == 'Paper':
                RockPaperScissors.__counter += 1
                RockPaperScissors.__computer_score += 1
                return f'computer wins! computer select {self.computer_selection} and you select {self.player_selection[self.player_1_selection]}\n'\
                    f"number of game : {RockPaperScissors.__counter}\nnumber of tie game : {RockPaperScissors.__tie_game}\nplayer_score : {RockPaperScissors.__player_1_score}\ncomputer_score : {RockPaperScissors.__computer_score}"
            else :
                RockPaperScissors.__counter += 1
                RockPaperScissors.__player_1_score += 1
                return f'you are winner! you select {self.player_selection[self.player_1_selection]} and computer select {self.computer_selection}\n'\
                    f"number of game : {RockPaperScissors.__counter}\nnumber of tie game : {RockPaperScissors.__tie_game}\nplayer_score : {RockPaperScissors.__player_1_score}\ncomputer_score : {RockPaperScissors.__computer_score}"
        else :
            return " something error try agin "
            exit()

    def check_winner_you_vs_friend(self):
        ''' method that check who's win the game .
        rock beats scissors and scissors beats paper and paper beats rock
        Args :
            None
        Returns :
            text (str) that tell us who is win the game and the number of played games and the score of each player
        '''
        if self.player_selection[self.player_2_selection] == self.player_selection[self.player_1_selection] :
            RockPaperScissors.__counter += 1
            RockPaperScissors.__tie_game += 1
            RockPaperScissors.__player_1_score = RockPaperScissors.__player_1_score
            RockPaperScissors.__player_2_score = RockPaperScissors.__player_2_score   
            return f"no winner player_1 select {self.player_selection[self.player_1_selection]} and player_2 select {self.player_selection[self.player_2_selection]}\n"\
                f"number of game : {RockPaperScissors.__counter}\nnumber of tie game : {RockPaperScissors.__tie_game}\nplayer_score : {RockPaperScissors.__player_1_score}\nplayer_2_score : {RockPaperScissors.__player_2_score}"

        elif self.player_selection[self.player_2_selection] == 'Rock' :
            if self.player_selection[self.player_1_selection] == 'Sciccors' :
                RockPaperScissors.__counter += 1
                RockPaperScissors.__player_2_score += 1 
                return f'player_2 wins! player_2 select {self.player_selection[self.player_2_selection]} and player_1 select {self.player_selection[self.player_1_selection]}\n'\
                    f"number of game : {RockPaperScissors.__counter}\nnumber of tie game : {RockPaperScissors.__tie_game}\nplayer_score : {RockPaperScissors.__player_1_score}\nplayer_2_score : {RockPaperScissors.__player_2_score}"

            else :
                RockPaperScissors.__counter += 1
                RockPaperScissors.__player_1_score += 1
                return f'player_1 wins! player_1 select {self.player_selection[self.player_1_selection]} and player_2 select {self.player_selection[self.player_2_selection]}\n'\
                    f"number of game : {RockPaperScissors.__counter}\nnumber of tie game : {RockPaperScissors.__tie_game}\nplayer_score : {RockPaperScissors.__player_1_score}\nplayer_2_score : {RockPaperScissors.__player_2_score}"

        elif self.player_selection[self.player_2_selection] == 'Paper':
            if self.player_selection[self.player_1_selection] == 'Rock':
                RockPaperScissors.__counter += 1
                RockPaperScissors.__player_2_score += 1
                return f'player_2 wins! player_2 select {self.player_selection[self.player_2_selection]} and player_1 select {self.player_selection[self.player_1_selection]}\n'\
                    f"number of game : {RockPaperScissors.__counter}\nnumber of tie game : {RockPaperScissors.__tie_game}\nplayer_score : {RockPaperScissors.__player_1_score}\nplayer_2_score : {RockPaperScissors.__player_2_score}"

            else :
                RockPaperScissors.__counter += 1
                RockPaperScissors.__player_1_score += 1
                return f'player_1 wins! player_1 select {self.player_selection[self.player_1_selection]} and player_2 select {self.player_selection[self.player_2_selection]}\n'\
                    f"number of game : {RockPaperScissors.__counter}\nnumber of tie game : {RockPaperScissors.__tie_game}\nplayer_score : {RockPaperScissors.__player_1_score}\nplayer_2_score : {RockPaperScissors.__player_2_score}"

        elif self.player_selection[self.player_2_selection] == 'Scissors':
            if self.player_selection[self.player_1_selection] == 'Paper':
                RockPaperScissors.__counter += 1
                RockPaperScissors.__player_2_score += 1
                return f'player_2 wins! player_2 select {self.player_selection[self.player_2_selection]} and player_1 select {self.player_selection[self.player_1_selection]}\n'\
                    f"number of game : {RockPaperScissors.__counter}\nnumber of tie game : {RockPaperScissors.__tie_game}\nplayer_score : {RockPaperScissors.__player_1_score}\nplayer_2_score : {RockPaperScissors.__player_2_score}"

            else :
                RockPaperScissors.__counter += 1
                RockPaperScissors.__player_1_score += 1
                return f'player_1 wins ! player_1 select {self.player_selection[self.player_1_selection]} and player_2 select {self.player_selection[self.player_2_selection]}\n'\
                    f"number of game : {RockPaperScissors.__counter}\nnumber of tie game : {RockPaperScissors.__tie_game}\nplayer_score : {RockPaperScissors.__player_1_score}\nplayer_2_score : {RockPaperScissors.__player_2_score}"

        else :
            return " something error try agin "
            exit()
