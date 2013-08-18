from __future__ import division, print_function

import arguments
from Game import Game
from bots import *
from Player import Player


# Change these to edit the default Game parameters
DEFAULT_VERBOSITY = True
DEFAULT_MIN_ROUNDS = 1000
DEFAULT_AVERAGE_ROUNDS = 2000
DEFAULT_END_EARLY = False
DEFAULT_PLAYERS = [Player(), Pushover(), Freeloader(), Alternator(), MaxRepHunter(), Random(.2), Random(.8)]

# Bare minimum test game. See README.md for details.


if __name__ == '__main__':
    players = [Player(), Pushover(), Freeloader(), Alternator(), MaxRepHunter(),
               Random(.2), Random(.8), FairHunter(), AverageHunter(),
               CommunityMan(), GoWithTheFlow(), BoundedHunter(.2, .7),
               BoundedHunter(.3,.7), BoundedHunter(.4, .7), BoundedHunter(.5,.7),
               BoundedHunter(.2, .8), BoundedHunter(.3,.8),  BoundedHunter(.4, .8),
               BoundedHunter(.5,.8),  BoundedHunter(.2, .6), BoundedHunter(.3,.6),
               BoundedHunter(.4, .6), HuntUntilLosingFood(.5),

               AggregateReturnsPerRoundSlacker(.22, .72),
               AggregateReturnsTotalSlacker(.22, .72),
           
               AggregateReturnsTotalSlacker(.2, .6),

               Freeloader(), Freeloader(), Freeloader(),
               Random(.3), Random(.4), Random(.5), Random(.6), Random(.7),
               Random(.41), Random(.42), Random(.43), Random(.44), Random(.45),
               Random(.38), Random(.39)
               
               ]
    
    game = Game(players)
    game.play_game()