"""
Place for solutions and workings to leetcode 75 challenges
"""
from typing import List


class SeventyFive: # pylint: disable=too-few-public-methods
    """
    Class to capture answers to leet code 75 challenges
    """

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
