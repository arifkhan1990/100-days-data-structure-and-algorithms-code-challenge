#                     Name : Arif Khan
#                     Judge: geeks for geeks
#                     problem: Sort a stack
#                     Difficulty: Easy
#                     Time Complexity: O(N*N)
#                     Problem Link: https://practice.geeksforgeeks.org/problems/sort-a-stack/1#
#                     Date: 2022-05-24


class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack
    def sorted(self, s):
        # Code here
        com_s = []
        temp = []
        while s != []:
            if com_s == []:
                com_s.append(s.pop())
            else:
                while com_s != [] and s[-1] > com_s[-1]:
                    temp.append(com_s.pop())
                else:
                    com_s.append(s.pop())
                    
            while temp != []:
                com_s.append(temp.pop())

        while com_s != []:
            s.append(com_s.pop())
        return s
#{ 
#  Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.sorted(arr)
        for e in range(len(arr)):
            print(arr.pop(), end=" ")
        print()


# } Driver Code Ends