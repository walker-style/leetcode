"""
Place for solutions and workings to leetcode 75 challenges
"""
from typing import List


class SeventyFive:  # pylint: disable=too-few-public-methods
    """
    Class to capture answers to leet code 75 challenges
    """

    def is_subsequence(self, s: str, t: str) -> bool:
        """
        Is s a subsequence of t. By removing 0 or more letters can `t` be
        transformed into `s`.

        Args:
            s str: subsequence string
            t str: string to check if i can be subsquences.

        Returns:
            bool: is s a subsequence of t

        >>> leet = SeventyFive()
        >>> leet.is_subsequence( s = "abc", t = "ahbgdc")
        True

        >>> leet.is_subsequence("axc", t = "ahbgdc")
        False
        """
        if not s:
            return True

        for i, s_char in enumerate(s):
            for j, t_char in enumerate(t):
                if s_char == t_char:
                    if i + 1 == len(s):
                        return True
                    if j + 1 == len(t):
                        return False
                    t = t[j + 1 :]
                    break
                if j + 1 == len(t):
                    return False
        return False

    def move_zeros(self, nums: list[int]) -> None:
        """
        in place move zeros to end of list without moving other numbers

        Args:
            nums list[int]: numbers to be sorted

        Returns:
            None: list is sorted in place

        >>> leet = SeventyFive()
        >>> nums = [0,1,0,3,12]
        >>> leet.move_zeros(nums)
        >>> assert nums == [1,3,12,0,0]
        """

        count = 0

        while 0 in nums:
            nums.remove(0)
            count += 1

        for _ in range(count):
            nums.append(0)

    def compress(self, chars: list[str]) -> int:
        """
        compressed version of string, grouping like characters

        Args:
            chars list[str]: characters to compress

        Returns:
            int: length of compressed list

        >>> leet = SeventyFive()
        >>> leet.compress(chars = ["a","a","b","b","c","c","c"])
        6

        >>> leet.compress(chars = ["a"])
        1

        >>> leet.compress(chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"])
        4
        """

        length = len(chars)
        index = 0
        total = 0

        while total + 1 < length:
            count = 1
            while chars[index] == chars[index + count]:
                count += 1
                if count + total == length:
                    break
            if count == 1:
                index += 1
                total += 1
                continue

            arr_count = list(str(count))
            for i, a in enumerate(arr_count):
                chars[index + 1 + i] = a

            for i in range(count - 1 - len(arr_count)):
                chars.pop(index + 1 + len(arr_count))
            index += len(arr_count) + 1
            total += count

        return len(chars)

    def increasing_triplet(self, nums: list[int]) -> bool:
        """
        Return True if there exists three ascending values
        for which their indicies also increase

        Args:
            nums list[int]: numbers to check

        Returns:
            bool: existence of triplet or not

        >>> leet = SeventyFive()
        >>> leet.increasing_triplet(nums = [1,2,3,4,5])
        True

        >>> leet.increasing_triplet(nums = [5,4,3,2,1])
        False

        >>> leet.increasing_triplet(nums = [2,1,5,0,4,6])
        True
        """

        if len(set(nums)) < 3:
            return False
        for i, num in enumerate(nums):
            for j, next_num in enumerate(nums[i + 1 :]):
                if num < next_num:
                    if next_num < max(nums[i + j + 2 :]):
                        return True
        return False

    def product_except_self(self, nums: list[int]) -> list[int]:
        """
        Gives product of all other elements

        Args:
            nums list[int]: list of numbers to be producted except self

        Returns
            list[int]: products excluding self

        >>> leet = SeventyFive()
        >>> leet.product_except_self(nums = [1,2,3,4])
        [24, 12, 8, 6]

        >>> leet.product_except_self( nums = [-1,1,0,-3,3])
        [0, 0, 9, 0, 0]
        """
        product = 1
        result = None
        for num in nums:
            if num:
                product *= num

        if 0 in nums:
            result = [0 if num else product for num in nums]
        else:
            result = [int(product / num) for num in nums]

        if 0 in nums:
            nums.remove(0)
            if 0 in nums:
                return [0 for _ in range(len(nums) + 1)]
        return result

    def reverse_string(self, s: str) -> str:
        """
        Reverse words in a string

        Args:
            s str: string to be reversed

        Returns:
            str: reversed string

        >>> leet = SeventyFive()
        >>> leet.reverse_string(s = "the sky is blue")
        'blue is sky the'

        >>> leet.reverse_string(s = "  hello world  ")
        'world hello'

        >>> leet.reverse_string(s = "a good   example")
        'example good a'
        """

        return " ".join([w for w in s.split(" ")[::-1] if w])

    def reverse_vowels(self, s: str) -> str:
        """
        Reverses the vowels of a string and returns string

        Args:
            s str: string to have vowels reversed

        Return:
            str: the string with reversed vowels

        >>> leet = SeventyFive()
        >>> leet.reverse_vowels("Hello")
        'Holle'

        >>> leet.reverse_vowels("leetcode")
        'leotcede'
        """

        vowels = "aeiouAEIOU"

        reversed_vowels = [letter for letter in s if letter in vowels]
        reversed_word = ""

        for letter in s:
            if letter in vowels:
                reversed_word += reversed_vowels.pop()
            else:
                reversed_word += letter

        return reversed_word

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
        for i, _ in enumerate(flowerbed):
            if not sum(flowerbed[max(i - 1, 0) : min(len(flowerbed) + 1, i + 2)]):
                flowerbed[i] = 1
                count += 1
                if count == n:
                    return True
        return False

    def greatest_candies(
        self, candies: List[int], extraCandies: int  # pylint: disable=C0103
    ) -> List[bool]:
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
