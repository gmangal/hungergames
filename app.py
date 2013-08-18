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
            # AggregateReturnsPerRoundHunter(.2, .6), 
            AggregateReturnsPerRoundSlacker(.2, .6), 
            AggregateReturnsPerRoundSlacker(.21, .7), 
            AggregateReturnsPerRoundSlacker(.21, .6), 
            AggregateReturnsPerRoundSlacker(.21, .5), 
            AggregateReturnsPerRoundSlacker(.21, .4), 
            AggregateReturnsPerRoundSlacker(.22, .7), 
            AggregateReturnsPerRoundSlacker(.22, .6), 
            AggregateReturnsPerRoundSlacker(.22, .5), 
            AggregateReturnsPerRoundSlacker(.22, .4), 
            AggregateReturnsPerRoundSlacker(.23, .7), 
            AggregateReturnsPerRoundSlacker(.23, .6), 
            AggregateReturnsPerRoundSlacker(.23, .5), 
            AggregateReturnsPerRoundSlacker(.23, .4), 
            AggregateReturnsPerRoundSlacker(.24, .7), 
            AggregateReturnsPerRoundSlacker(.24, .6), 
            AggregateReturnsPerRoundSlacker(.25, .6), 
            AggregateReturnsPerRoundSlacker(.26, .6), 
            AggregateReturnsPerRoundSlacker(.27, .6), 
            AggregateReturnsPerRoundSlacker(.28, .6), 
            AggregateReturnsPerRoundSlacker(.29, .6), 
            AggregateReturnsPerRoundSlacker(.3, .6), 
            AggregateReturnsPerRoundSlacker(.1, .6), 
            AggregateReturnsPerRoundSlacker(.4, .6), 
            # AggregateReturnsTotalHunter(.2, .6),
            AggregateReturnsTotalSlacker(.2, .6),
            AggregateReturnsTotalSlacker(.21, .6),
            AggregateReturnsTotalSlacker(.21, .5),
            AggregateReturnsTotalSlacker(.21, .4),
            AggregateReturnsTotalSlacker(.22, .6),
            AggregateReturnsTotalSlacker(.22, .5),
            AggregateReturnsTotalSlacker(.22, .4),
            AggregateReturnsTotalSlacker(.23, .6),
            AggregateReturnsTotalSlacker(.23, .5),
            AggregateReturnsTotalSlacker(.23, .4),
            AggregateReturnsTotalSlacker(.24, .6),
            AggregateReturnsTotalSlacker(.25, .6),
            AggregateReturnsTotalSlacker(.26, .6),
            AggregateReturnsTotalSlacker(.27, .6),
            AggregateReturnsTotalSlacker(.28, .6),
            AggregateReturnsTotalSlacker(.29, .6),
            AggregateReturnsTotalSlacker(.1, .6),
            AggregateReturnsTotalSlacker(.3, .6),
            AggregateReturnsTotalSlacker(.4, .6),
            Freeloader(), Freeloader(), Freeloader(), 
            Random(.3), Random(.4), Random(.5), Random(.6), Random(.7), 
            Random(.41), Random(.42), Random(.43), Random(.44), Random(.45), 
            Random(.46), Random(.47), Random(.48), Random(.49), 
            Random(.35), Random(.36), Random(.37), Random(.38), Random(.39)]

    # number of games to play
    gamesToPlay = 1
    if len(sys.argv) > 1:
        gamesToPlay = int(sys.argv[1])

    # create new instance of Game for each game to play
    for i in range(0, gamesToPlay):
        game = Game(players)
        game.play_game()
