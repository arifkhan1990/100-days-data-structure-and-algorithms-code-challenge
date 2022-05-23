#                     Name : Arif Khan
#                     Judge: geeks for geeks
#                     problem: Majority Element
#                     Difficulty: Easy
#                     Time Complexity: O(N)
#                     Problem Link: https://practice.geeksforgeeks.org/problems/majority-element-1587115620/1#
#                     Date: 2022-05-22

#User function template for Python 3

class Solution:
    def majorityElement(self, A, N):
        majority_element = {}

        for i in range(N):
            if A[i] in majority_element:
                majority_element[A[i]] += 1
            else:
                majority_element[A[i]] = 1
                
        for i in majority_element:
            if majority_element[i] > N/2:
                return i
        return -1

import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()

