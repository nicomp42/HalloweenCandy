# main.py

from halloweenCandyPackage.HalloweenCandy import *

if __name__ == "__main__":
    myFavorite = HalloweenCandy("Bill", "Chocolate")
    print(myFavorite)   # Invokes __str__ by default
    
    yFavorite = HalloweenCandy("Heitor", "Bis")
    print(myFavorite)   # Invokes __str__ by default
    