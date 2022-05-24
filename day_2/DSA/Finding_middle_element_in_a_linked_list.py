#                     Name : Arif Khan
#                     Judge: geeks for geeks
#                     problem: Finding middle element in a linked list
#                     Difficulty: Easy
#                     Time Complexity: O(N)
#                     Problem Link: https://practice.geeksforgeeks.org/problems/finding-middle-element-in-a-linked-list/1#
#                     Date: 2022-05-23


# your task is to complete this function

'''
class node:
    def __init__(data):
        self.data = data
        self.next = None
'''
class Solution:
    #  Should return data of middle node. If linked list is empty, then  -1
    def findMid(self, head):
        lsLen = self.listLen(head) // 2

        while lsLen:
            head = head.next
            lsLen -= 1
        
        head.next = None
        # printlist(head)
        return head.data
    
    #linked list len calculation
    def listLen(self, head):
        c = 0
        while head:
            c += 1
            head = head.next
        return c


# Node Class    
class node:
    def __init__(self):
        self.data = None
        self.next = None

# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert(self, data):
        if self.head == None:
            self.head = node()
            self.tail = self.head
            self.head.data = data
        else:
            new_node = node()
            new_node.data = data
            new_node.next = None
            self.tail.next = new_node
            self.tail = self.tail.next

def printlist(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print('')

# Driver Program
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        list1 = Linked_List()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in values:
            list1.insert(i)
        ob = Solution()
        print(ob.findMid(list1.head))
