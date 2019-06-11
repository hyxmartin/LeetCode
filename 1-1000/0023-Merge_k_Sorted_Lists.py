"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""
from queue import PriorityQueue

# Definition for singly-linked list.
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


class SolutionClassBruteForce:
    def mergeKLists(self, list):
        """
        :param list: List[ListNode]
        :return: ListNode
        """
        arr = []
        for node in list:
            while node is not None:
                arr.append(node.val)
                node = node.next
        arr.sort()
        print(arr)
        for num, i in enumerate(arr):
            if num == 0:
                retNode = actNode = ListNode(i)
                continue
            actNode.next = ListNode(i)
            actNode = actNode.next

        return retNode
# Space: O()
# Time: O()


class SolutionClassPriorityQueue(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        q = PriorityQueue()
        for l in lists:
            q.put((l.val, l))

        head = point = ListNode(0)
        while not q.empty():
            val, node = q.get()
            point.next = ListNode(val)
            point = point.next

            if node.next is not None:
                q.put((node.next.val, node.next))

        return head.next


if __name__ == "__main__":
    l1 = LinkedList()
    l1.insertStart(5)
    l1.insertStart(3)
    l1.insertStart(1)
    l1.traverseList()
    print("---")
    l2 = LinkedList()
    l2.insertStart(6)
    l2.insertStart(4)
    l2.insertStart(2)
    l2.traverseList()
    print("---")
    retNode = SolutionClassPriorityQueue().mergeKLists([l1.head, l2.head])
    retList = LinkedList()
    retList.head = retNode
    retList.traverseList()
