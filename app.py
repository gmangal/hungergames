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
            BoundedHunter(.4, .6), HuntUntilLosingFood(.5)]
    game = Game(players)
    gamesToPlay = 1
    if len(sys.argv) > 1:
        gamesToPlay = sys.argv[1]
    game.play_game(gamesToPlay)
