
# Definition for singly-linked list.
class ListNode:  # pylint: disable=too-few-public-methods

    """
    ListNode to define node for exercise
    """

    def __init__(self, val=0, next=None):  # pylint: disable=W0622
        self.val = val
        self.next = next

    def __repr__(self):  # pylint: disable=W0622
        arr = [self.val]
        while self.next:
            self = self.next  # pylint: disable=W0642
            arr.append(self.val)
        return str(arr)


class LinkedListFactory:  # pylint: disable=too-few-public-methods

    """
    Easy way to make linked list from array
    """

    @staticmethod
    def create_from_array(array):
        """
        Turn array into linked list
        """

        if not array:
            return None

        head = ListNode(array[0])
        current_node = head
        for val in array[1:]:
            current_node.next = ListNode(val)
            current_node = current_node.next

        return head


