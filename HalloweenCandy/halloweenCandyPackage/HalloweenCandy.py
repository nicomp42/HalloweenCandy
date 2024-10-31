# HalloweenCandy.py
# Bill Nicholson

import random

class HalloweenCandy:
    """
    Model Halloween Candy preference
    """
    def __init__(self, name, favorite):
        """
        Constructor
        @param name String: Your name
        @param favorite String: Your favorite candy on Halloween
        """
        self.__name = name
        self.__favorite = favorite
        self.__affinity_list = ["likes", "enjoys", "prefers", "adores", "craves", "loves", "appreciates", "desires"]

    def get_affinity(self):
        """
        Get the list of synomyms for 'like'
        @return list: The list
        """
        return random.choice(self.__affinity_list)

    def __str__(self):
        return self.__name + " " + self.get_affinity() + " " + self.__favorite
    
