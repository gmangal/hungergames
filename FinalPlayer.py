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
        # constrict threshold so that we hunt less often
        if self.huntEarnings > self.slackEarnings:
            if self.up > 0.2:
                self.up -= 0.1
        else:
            if (self.up - self.low) < 1.0:
                self.up += 0.1