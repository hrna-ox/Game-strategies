"""
Game

    In Liars Game, a community of n players start with the same amount of money each.
    Every round each individual selects how much they want to contribute to the central pot.
    After each round the central point is distributed between the entire community.
    The community does not like selfish people, so they kick out the person who gives the least amount of money each round.
    This also means that if you give too much in the beginning, you will not have enough in the end to survive.
    What strategy increases the odds of you coming out victorious?
    
Remark

    The Uniformly Random function might not perform very well, but for now it is the only one introducing a significant amount of randomness. Without it the other strategies become deterministic and provide for a very boring analysis
    In a game where all opponents always put everything, then you are limited to do the same. However as soon as someone else has a different strategy, you can beat it by putting slightly more and then always putting almost everything.
"""

import pandas as pd
