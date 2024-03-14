"""
Place to complete leetcode challenges.
https://leetcode.com/walker-style/
"""

from typing import Optional
from src.helper import ListNode, LinkedListFactory


class Daily:  # pylint: disable=too-few-public-methods
    """
    Class to house daily leetcode challenges
    """

    def num_subarray_with_sum(self, nums: list[int], goal: int) -> int:
        """
        Find number of subarrays that give the goal value in binary

        Args:
            nums list(int): array from which to search subarrays

            goal int: number to which subarray needs to match when 
            converted to binary

        Returns:
            int: number of subarrays that equal goal

        >>> leet = Daily()
        >>> leet.num_subarray_with_sum([0,0,0,0,0], 0)
        15
        
        >>> leet.num_subarray_with_sum( nums = [1,0,1,0,1], goal=2)
        4
        """

        count = {0: 1}
        curr_sum = 0
        total_subarrays = 0
        
        for num in nums:
            curr_sum += num
            if curr_sum - goal in count:
                total_subarrays += count[curr_sum - goal]
            count[curr_sum] = count.get(curr_sum, 0) + 1

        return total_subarrays

        # bin_goal = [int(i) for i in list(bin(goal)[2:])]
        #
        # subarrays = []
        #
        # for i in range(len(nums)-len(bin_goal)):
        #     for j in range(len(nums)-len(bin_goal)):
        #         subarray = nums[i : i + len(bin_goal) + j]
        #
        #         if subarray[len(subarray)-len(bin_goal):] == bin_goal:
        #             subarrays.append(subarray)
        #
        # print(subarrays)
        #
        # return len(subarrays)
        # 


    def pivot_integer(self, n: int) -> int:
        """
        Finds the pivot integer.

        Args:
            n int: produces a range from 1 to n from which to find the
                pivot integer

        Returns:
            int: pivot integer if it exists or -1 if it does not

        >>> leet = Daily()
        >>> leet.pivot_integer(n=8)
        6

        >>> leet.pivot_integer(n=1)
        1

        >>> leet.pivot_integer(n=4)
        -1
        """

        array = list(range(1, n + 1))

        for i, number in enumerate(array):
            if sum(array[: i + 1]) == sum(array[i:]):
                return number
        return -1

    def remove_zero_sum_sublist(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Remove consecutive sequencenses of nodes that sum to zero

        Args:
            head Optional[ListNode]: node from which to start checking for zero sum sequences

        Return:
           Optional[ListNode]: list with no consecutive zero sum nodes

        >>> leet = Daily()
        >>> head = LinkedListFactory.create_from_array([1,2,-3,3,1])
        >>> leet.remove_zero_sum_sublist(head = head)
        [3, 1]

        >>> head = LinkedListFactory.create_from_array([1,2,3,-3,4])
        >>> leet.remove_zero_sum_sublist(head = head)
        [1, 2, 4]

        >>> head = LinkedListFactory.create_from_array([1,2,3,-3,-2])
        >>> leet.remove_zero_sum_sublist(head = head)
        [1]
        """

        dummy = ListNode(0)
        dummy.next = head
        prefix_sum = 0
        prefix_sum_map = {}

        current = dummy

        while current:
            prefix_sum += current.val
            prefix_sum_map[prefix_sum] = current
            current = current.next

        current = dummy
        prefix_sum = 0

        while current:
            prefix_sum += current.val
            if prefix_sum in prefix_sum_map:
                current.next = prefix_sum_map[prefix_sum].next
            current = current.next

        return dummy.next

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


