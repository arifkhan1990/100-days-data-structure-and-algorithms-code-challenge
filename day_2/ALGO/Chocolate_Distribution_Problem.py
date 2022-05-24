
#                     Name : Arif Khan
#                     Judge: geeks for geeks
#                     problem: Chocolate Distribution Problem
#                     Difficulty: Easy
#                     Time Complexity: O(N*Log(N))
#                     Problem Link: https://practice.geeksforgeeks.org/problems/chocolate-distribution-problem3825/1#
#                     Date: 2022-05-23

#User function Template for python3

class Solution:

    def findMinDiff(self, A,N,M):
        distribute = []
        A.sort()
        if M == N:
            return A[-1] - A[0]
        for i in range(0,  N - (M - 1)):
            distribute.append(A[i+(M-1)] - A[i])
        distribute.sort()
        return distribute[0]
        
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        A = [int(x) for x in input().split()]
        M = int(input())


        solObj = Solution()

        print(solObj.findMinDiff(A,N,M))
# } Driver Code Ends