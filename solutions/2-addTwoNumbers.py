'''
2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative
integers. The digits are stored in reverse order and each of their nodes
contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the
number 0 itself.

Example:

    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    Explanation: 342 + 465 = 807.
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        mod, val = divmod(l1.val + l2.val, 10)
        l3 = ListNode(val)
        node1 = l1.next
        node2 = l2.next
        node3 = l3
        while node1 and node2:
            mod, val = divmod(node1.val + node2.val + mod, 10)
            node3.next = ListNode(val)
            node1 = node1.next
            node2 = node2.next
            node3 = node3.next
        while node1:
            mod, val = divmod(node1.val + mod, 10)
            node3.next = ListNode(val)
            node1 = node1.next
            node3 = node3.next
        while node2:
            mod, val = divmod(node2.val + mod, 10)
            node3.next = ListNode(val)
            node2 = node2.next
            node3 = node3.next
        if mod:
            node3.next = ListNode(mod)
        return l3
