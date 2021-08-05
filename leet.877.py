class Solution(object):
    def stoneGame(self, piles):
        """
        Answer is always true because the player who starts (Alex) can decide to pick up all the piles
        in odd indices or all the piles in even indices. And we know that:
        . len(piles) == 2n, n beign a natural number
        . sum(piles) is odd
        And with this two statements we can assure that the sum of the even piles and the sum of the odd piles
        will be different (sum(piles[0::2]) != sum(piles[1::2])) so one must be greater than the other
        and therefore the first player can choose to pick those piles and always win.
        """
        return True