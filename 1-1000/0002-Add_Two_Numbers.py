"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order
and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0

    # O(1) !!!
    def insertStart(self, val):

        self.size = self.size + 1
        newNode = ListNode(val)

        if not self.head:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def traverseList(self):

        actualNode = self.head

        while actualNode is not None:
            print("%d " % actualNode.val)
            actualNode = actualNode.next


class SolutionClassFinal:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode, carry=0) -> ListNode:
        """
        :param l1: ListNode
        :param l2: ListNode
        :param carry: int
        :return: ListNode
        """
        posval = (l1.val + l2.val + carry) % 10
        carry = (l1.val + l2.val + carry) // 10
        ret = ListNode(posval)

        if l1.next is not None or l2.next is not None or carry != 0:
            if l1.next is None:
                l1.next = ListNode(0)
            if l2.next is None:
                l2.next = ListNode(0)
            ret.next = self.addTwoNumbers(l1.next, l2.next, carry)
        return ret
# Space: O(N)
# Time: O(N)


if __name__ == "__main__":
    l1 = LinkedList()
    l1.insertStart(3)
    l1.insertStart(4)
    l1.insertStart(2)
    l1.traverseList()
    print("---")
    l2 = LinkedList()
    l2.insertStart(4)
    l2.insertStart(6)
    l2.insertStart(5)
    l2.traverseList()
    print("---")
    retlinklist = LinkedList()
    retlinklist.head = SolutionClassFinal().addTwoNumbers(l1.head, l2.head)
    retlinklist.traverseList()
