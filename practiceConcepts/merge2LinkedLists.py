# Definition for singly-linked list.

def listNode(list):
    n1 = list.next
    print("start")
    while n1 != None:
        print(n1.val)
        n1 =  n1.next
    print("fin")
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        currentNode = ListNode()
        L3H = ListNode()
        if (list1 == None) and (list2 == None):
            return None
        elif list1 == None:
            return list2
        elif list2 == None:
            return list1
        if list1.val >= list2.val:
            L3H = ListNode(list2.val, None)
            currentNode = L3H
            list2 = list2.next
        else:
            L3H = ListNode(list1.val, None)
            currentNode = L3H
            list1 = list1.next

        while list1 != None or list2 != None:
            # listNode(L3H)
            # print(n1, n2)
            if list1 and list2:
                if list1.val <= list2.val:
                    newNode = ListNode(val = list1.val)
                    currentNode.next = newNode
                    currentNode = newNode
                    list1 = list1.next

                else:
                    newNode = ListNode(val = list2.val)
                    currentNode.next = newNode
                    currentNode = newNode
                    list2 = list2.next
            elif list1:
                currentNode.next = list1
                return L3H
            elif list2:
                currentNode.next = list2
                return L3H
        return L3H
                

                

    
                
h1 =  ListNode()
a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(4)

h2 =  ListNode()
b1 = ListNode(1)
b2 = ListNode(3)
b3 = ListNode(4)

b2.next = b3
b1.next = b2
h2.next = b1

a2.next = a3
a1.next = a2
h1.next = a1
Sol =  Solution()
listNode(Sol.mergeTwoLists(h1,h2))
