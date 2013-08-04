from Player import BasePlayer
import random

class Pushover(BasePlayer):
    '''Player that always hunts.'''
    def __init__(self):
        self.name = "Pushover"
    
    def hunt_choices(
                    self,
                    round_number,
                    current_food,
                    current_reputation,
                    m,
                    player_reputations,
                    ):
        return ['h']*len(player_reputations)

        
class Freeloader(BasePlayer):
    '''Player that always slacks.'''
    
    def __init__(self):
        self.name = "Freeloader"
    
    def hunt_choices(
                    self,
                    round_number,
                    current_food,
                    current_reputation,
                    m,
                    player_reputations,
                    ):
        return ['s']*len(player_reputations)
        

class Alternator(BasePlayer):
    '''Player that alternates between hunting and slacking.'''
    def __init__(self):
        self.name = "Alternator"
        self.last_played = 's'
        
    def hunt_choices(
                    self,
                    round_number,
                    current_food,
                    current_reputation,
                    m,
                    player_reputations,
                    ):
        hunt_decisions = []
        for i in range(len(player_reputations)):
            self.last_played = 'h' if self.last_played == 's' else 's'
            hunt_decisions.append(self.last_played)

        return hunt_decisions

class MaxRepHunter(BasePlayer):
    '''Player that hunts only with people with max reputation.'''
    def __init__(self):
        self.name = "MaxRepHunter"

    def hunt_choices(
                    self,
                    round_number,
                    current_food,
                    current_reputation,
                    m,
                    player_reputations,
                    ):
        threshold = max(player_reputations)
        return ['h' if rep == threshold else 's' for rep in player_reputations]


class Random(BasePlayer):
    '''
    Player that hunts with probability p_hunt and
    slacks with probability 1-p_hunt
    '''
    
    def __init__(self, p_hunt):
        self.name = "Random" + str(p_hunt)
        self.p_hunt = p_hunt

    def hunt_choices(
                    self,
                    round_number,
                    current_food,
                    current_reputation,
                    m,
                    player_reputations,
                    ):
        return ['h' if random.random() < self.p_hunt else 's' for p in player_reputations]

class FairHunter(BasePlayer):
    '''Player that tries to be fair by hunting with same probability as each opponent'''
    def __init__(self):
        self.name = "FairHunter"

    def hunt_choices(
                self,
                round_number,
                current_food,
                current_reputation,
                m,
                player_reputations,
                ):
        return ['h' if random.random() < rep else 's' for rep in player_reputations]
        
class BoundedHunter(BasePlayer):
    '''Player that hunts whenever the other's reputation is within some range.'''
    def __init__(self,lower,upper):
        self.name = "BoundedHunter" + str(lower)+'-'+str(upper)
        self.low = lower
        self.up = upper

    def hunt_choices(
                    self,
                    round_number,
                    current_food,
                    current_reputation,
                    m,
                    player_reputations,
                    ):
        return ['h' if self.low <= rep <= self.up else 's' for rep in player_reputations]
        
class AverageHunter(BasePlayer):
    '''Player that tries to maintain the average reputation, but spreads its hunts randomly.'''
    
    def __init__(self):
        self.name = "AverageHunter"

    def hunt_choices(
                    self,
                    round_number,
                    current_food,
                    current_reputation,
                    m,
                    player_reputations,
                    ):
        avg_rep = sum(player_reputations) / float(len(player_reputations))
        return ['h' if random.random() < avg_rep else 's' for rep in player_reputations]

class CommunityMan(BasePlayer):
    def __init__(self):
        self.name = "CommunityMan"
    
    def hunt_choices(
                     self,
                     round_number,
                     current_food,
                     current_reputation,
                     m,
                     player_reputations,
                     ):
        hunt_decisions = list()
        numPlayers = len(hunt_decisions)
            
        for reputation in player_reputations:
        # hunt if enemy hunts relatively frequently
            if reputation > .25:
                hunt_decisions.append('h')
            else:
                hunt_decisions.append('s')            
        return hunt_decisions

class GoWithTheFlow(BasePlayer):
    def __init__(self):
        self.name = "GoWithTheFlow"
    
    def hunt_choices(
                     self,
                     round_number,
                     current_food,
                     current_reputation,
                     m,
                     player_reputations,
                     ):
        hunt_decisions = list()
        numPlayers = len(hunt_decisions)
        

        for reputation in player_reputations:
            # hunt if enemy hunts relatively frequently
            if reputation > .25:
                hunt_decisions.append('h')
            else:
                # hunt if more than half the players need to hunt to receive
                # the communal food prize
                if m > ((numPlayers*(numPlayers - 1))/4):
                    hunt_decisions.append('h')
                else:
                    hunt_decisions.append('s')
        
        return hunt_decisions

class HuntUntilLosingFood(BasePlayer):
    def __init__(self, threshold):
        self.name = "HuntUntilLosingFood - " + str(threshold)
        self.threshold = threshold
        self.startingFood = 0

    def hunt_choices(
                     self,
                     round_number,
                     current_food,
                     current_reputation,
                     m,
                     player_reputations,
                     ):

        # record amount of food you start off with
        if round_number == 1:
            self.startingFood = current_food

        # percent of orignal food you have (can be over 100%)
        percentFoodLeft = float(current_food) / self.startingFood

        hunt_decisions = list()
        
        for reputation in player_reputations:
            # keep hunting until you have less than the threshold percent 
            # of your orignal food stock remaining, then slack until 
            # you can gain back more food
            if percentFoodLeft < self.threshold:
                hunt_decisions.append('s')
            else:
                hunt_decisions.append('h')
        
        return hunt_decisions

class AggregateReturnsPerRound(BasePlayer):
    # player that adjusts threshold for hunting based on aggreate 
    # results of each action for the previous round
    def __init__(self,lower,upper):
        self.name = "AggregateReturnsPerRound"
        # thresholds, if partner rep is between these (inclusive), then hunt
        self.low = lower
        self.up = upper
        # last round's decisions
        self.hunt_decisions = list()
        # total earnings from hunting in the past round
        self.huntEarnings = 0
        # total earnings from slacking in the past round
        self.slackEarnings = 0

    def hunt_choices(
                    self,
                    round_number,
                    current_food,
                    current_reputation,
                    m,
                    player_reputations,
                    ):
        for rep in player_reputations:
            if self.low <= rep <= self.up:
                self.hunt_decisions.append('h')
            else:
                self.hunt_decisions.append('s')

        return self.hunt_decisions

    def hunt_outcomes(self, food_earnings):

        self.huntEarnings = 0
        # total earnings from slacking
        self.slackEarnings = 0

        for i in range(0, len(food_earnings)):
            if self.hunt_decisions[i] == 'h':
                self.huntEarnings += food_earnings[i]
            else:
                self.slackEarnings += food_earnings[i]

    def round_end(self, award, m, number_hunters):
        # communal award can be considered earnings from hunting, since 
        # it signals that a fair number of players are hunting
        self.huntEarnings += award

        # if earnings from hunting are greater than earnings from slacking, 
        # that means more people are probably hunting. In that case, 
        # expand threshold so that we hunt more often
        if self.huntEarnings > self.slackEarnings:
            if self.up < 1.0:
                self.up += 0.1
        else:
            if (self.up - self.low) > .1:
                self.up -= 0.1

class AggregateReturnsTotal(BasePlayer):
    # player that adjusts threshold for hunting based on aggreate 
    # results of each action for the previous round
    def __init__(self,lower,upper):
        self.name = "AggregateReturnsTotal"
        # thresholds, if partner rep is between these (inclusive) then hunt
        self.low = lower
        self.up = upper
        # decisions of previous round
        self.hunt_decisions = list()
        # total returns from hunting over entire game
        self.huntEarnings = 0
        # total returns from slacking over entire game
        self.slackEarnings = 0

    def hunt_choices(
                    self,
                    round_number,
                    current_food,
                    current_reputation,
                    m,
                    player_reputations,
                    ):
        for rep in player_reputations:
            if self.low <= rep <= self.up:
                self.hunt_decisions.append('h')
            else:
                self.hunt_decisions.append('s')

        return self.hunt_decisions

    def hunt_outcomes(self, food_earnings):

        for i in range(0, len(food_earnings)):
            if self.hunt_decisions[i] == 'h':
                self.huntEarnings += food_earnings[i]
            else:
                self.slackEarnings += food_earnings[i]

    def round_end(self, award, m, number_hunters):
        # communal award can be considered earnings from hunting, since 
        # it signals that a fair number of players are hunting
        self.huntEarnings += award

        # if earnings from hunting are greater than earnings from slacking, 
        # that means more people are probably hunting. In that case, 
        # expand threshold so that we hunt more often
        if self.huntEarnings > self.slackEarnings:
            if self.up < 1.0:
                self.up += 0.1
        else:
            if (self.up - self.low) > .1:
                self.up -= 0.1



