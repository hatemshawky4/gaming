from rockpaperscissors2 import RockPaperScissors
try:
    while True :
        game = RockPaperScissors()
        x = game.start()
        if x == 1 :
            x = print(game.check_winner_computer_vs_you())
        elif x == 2 :
            print(game.check_winner_you_vs_friend())
except KeyboardInterrupt:
    pass
