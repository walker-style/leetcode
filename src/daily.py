"""
Place to complete leetcode challenges.
https://leetcode.com/walker-style/
"""


class Daily:  # pylint: disable=too-few-public-methods
    """
    Class to house daily leetcode challenges
    """

    def custom_sort_string(self, order: str, s: str) -> str:
        """
        Reorder s so that any characters in s are in the same order
        as order

        Args:
            order str: ordered string
            s str: string to be ordered

        Return:
            str: s reordered for any overlapping cha between s and ordered

        Raises:
            TODO

        >>> daily = Daily()
        >>> daily.custom_sort_string("cba", "abcd")
        'cbad'

        >>> daily.custom_sort_string("bcafg", "abcd")
        'bcad'
        """
        ordered: str = ""
        c_arr = list(s)
        for c in order:
            while c in c_arr:
                c_arr.remove(c)
                ordered += c

        ordered += "".join(c_arr)
        return ordered
