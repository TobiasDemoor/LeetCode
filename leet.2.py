# Definition for singly-linked list.
from typing import List


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        aux1 = l1
        aux2 = l2
        auxR = head
        carry = 0
        while aux1 != None and aux2 != None:
            currentSum = aux1.val + aux2.val + carry
            if currentSum > 9:
                currentSum -= 10
                carry = 1
            else:
                carry = 0
            newNode = ListNode(currentSum)
            auxR.next = newNode
            auxR = newNode
            aux1 = aux1.next
            aux2 = aux2.next

        if aux2 != None:
            aux1 = aux2
        while aux1 != None:
            currentSum = aux1.val + carry
            if currentSum > 9:
                currentSum -= 10
                carry = 1
            else:
                carry = 0
            newNode = ListNode(currentSum)
            auxR.next = newNode
            auxR = newNode
            aux1 = aux1.next
        if carry > 0:
            auxR.next = ListNode(carry)
        return head.next