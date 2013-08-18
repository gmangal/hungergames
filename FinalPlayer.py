'''
This player attempts to survive by analyzing the overall returns from hunting
and slacking each round. The array of decisions made during the round is saved
and then compared to the array of returns from each interaction that is given in
the hunt_outcomes method. 

If this player slacked for an interaction, the returns
(positive or negative) are added to a slackEarnings variable. Similarly, if this
player hunted for an interaction, the returns are added to a huntEarnings
variable. 

If the communal food is received due to the number of hunts exceeding
m, those earnings are added to huntEarnings since that food is earned by players
hunting

If, for any given round, hunting is overall earning the player more food (or
losing less) than slacking, this means that more players are hunting. This
player tries to take advantage of that by attempting to slack more often.

However, if slacking is earning more than hunting, that probably means that
other players are responding to this player's slack by slacking themselves
(note: this is more a case of minimizing losses than maximizing returns). Thus,
this player tries to encourage others to hunt more by opting to hunt more often.
'''
class Player():
    # player that adjusts threshold for hunting based on aggreate
    # results of each action for the previous round
    # lowers upper bound if hunter earnings are greater than slack earnings
    def __init__(self):
        self.name = "AggregateReturnsPerRoundSlacker"
        # thresholds, if partner rep is between these (inclusive), then hunt
        self.low = .22
        self.up = .72
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
            if self.low <= rep and rep <= self.up:
                self.hunt_decisions.append('h')
            else:
                self.hunt_decisions.append('s')
        
        return self.hunt_decisions
    
    def hunt_outcomes(self, food_earnings):
        
        # total earnings from hunting, reset to 0 for the round
        self.huntEarnings = 0
        # total earnings from slacking, reset to 0 for the round
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
        # constrict threshold so that we hunt less often
        if self.huntEarnings > self.slackEarnings:
            if self.up > 0.2:
                self.up -= 0.1
        else:
            if (self.up - self.low) < 1.0:
                self.up += 0.1
