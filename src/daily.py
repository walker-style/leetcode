"""
Place to complete leetcode challenges.
https://leetcode.com/walker-style/
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        arr = [self.val]
        while self.next:
            self = self.next
            arr.append(self.val)
        return str(arr)

class LinkedListFactory:
    @staticmethod
    def create_from_array(array):
        if not array:
            return None

        head = ListNode(array[0])
        current_node = head
        for val in array[1:]:
            current_node.next = ListNode(val)
            current_node = current_node.next

        return head


class Daily:  # pylint: disable=too-few-public-methods
    """
    Class to house daily leetcode challenges
    """

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
