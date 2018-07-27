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
        if node1:
            while node1:
                mod, val = divmod(node1.val + mod, 10)
                node3.next = ListNode(val)
                node1 = node1.next
                node3 = node3.next
        else:
            while node2:
                mod, val = divmod(node2.val + mod, 10)
                node3.next = ListNode(val)
                node2 = node2.next
                node3 = node3.next
        if mod:
            node3.next = ListNode(mod)
        return l3
