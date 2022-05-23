
#                     Name : Arif Khan
#                     Judge: geeks for geeks
#                     problem: Leaders in an array
#                     Difficulty: Easy
#                     Time Complexity: O(N)
#                     Problem Link: https://practice.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1
#                     Date: 2022-05-22


class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self, A, N):
        #Code here
        curr_large = A[-1]
        leader_arr = [curr_large]
        n = N-2

        while n >= 0:
            if curr_large <= A[n]:
                curr_large = A[n]
                leader_arr.append(curr_large)
            n -= 1
        return reversed(leader_arr)

import math

    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        A=[int(x) for x in input().strip().split()]
        obj = Solution()
        
        A=obj.leaders(A,N)
        
        for i in A:
            print(i,end=" ")
        print()
        
        T-=1

if __name__=="__main__":
    main()
