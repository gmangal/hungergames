from __future__ import division, print_function
from Game import Game
from bots import *
from Player import Player
import sys

# Bare minimum test game. See README.md for details.

if __name__ == '__main__':
    players = [Player(), Pushover(), Freeloader(), Alternator(), MaxRepHunter(),
            Random(.2), Random(.8), FairHunter(), AverageHunter(),
            CommunityMan(), GoWithTheFlow(), BoundedHunter(.2, .7),
            BoundedHunter(.3,.7), BoundedHunter(.4, .7), BoundedHunter(.5,.7),
            BoundedHunter(.2, .8), BoundedHunter(.3,.8),  BoundedHunter(.4, .8),
            BoundedHunter(.5,.8),  BoundedHunter(.2, .6), BoundedHunter(.3,.6),
            BoundedHunter(.4, .6), HuntUntilLosingFood(.5),
            AggregateReturnsPerRound(.2, .6), AggregateReturnsTotal(.2, .6)]

    # number of games to play
    gamesToPlay = 1
    if len(sys.argv) > 1:
        gamesToPlay = int(sys.argv[1])

    # create new instance of Game for each game to play
    for i in range(0, gamesToPlay):
        game = Game(players)
        game.play_game()
