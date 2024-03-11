"""
Place for solutions and workings to leetcode 75 challenges
"""
from typing import List


class SeventyFive: # pylint: disable=too-few-public-methods
    """
    Class to capture answers to leet code 75 challenges
    """
    
    def can_place_flowers(self, flowerbed: List[int], n: int) -> bool:
        """
        Returns if flowers can be placed in a garden

        Args:
            flowerbed List[int]: represents plots 1 have plant 0 are empty
            n int: number of potential plants to plant

        Returns:
            bool: if potential plants can be planted

        >>> leet = SeventyFive()
        >>> leet.can_place_flowers(flowerbed = [1,0,0,0,1], n = 1)
        True

        >>> leet.can_place_flowers(flowerbed = [1,0,0,0,1], n = 2)
        False
        """
        if n == 0:
            return True
        count = 0
        for i in range(len(flowerbed)):
            
            if not(sum(flowerbed[max(i-1,0):min(len(flowerbed)+1,i+2)])):
                flowerbed[i] = 1
                count += 1
                if count == n:
                    return True
        return False
                

    def greatest_candies(self, candies: List[int], extraCandies: int) -> List[bool]: # pylint: disable=C0103
        """
        Return which children if given extra candies would have the most candies

        Args:
            candies List[int]: number of candies each kid currently has
            extraCandies int: reserve candies to be given to each kid in check for greatest

        Return:
            List[bool]: list of kids that have most candies if given extraCandies

        >>> leet = SeventyFive()
        >>> first = leet.greatest_candies(candies = [2,3,5,1,3], extraCandies = 3)
        >>> assert(first == [True, True, True, False, True])

        >>> second = leet.greatest_candies(candies = [4,2,1,1,2], extraCandies = 1)
        >>> assert(second == [True, False, False, False, False])
        """

        return [c + extraCandies >= max(candies) for c in candies]
