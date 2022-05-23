#                     Name : Arif Khan
#                     Judge: geeks for geeks
#                     problem: Subarray with given sum
#                     Difficulty: Easy
#                     Time Complexity: O(N)
#                     Problem Link: https://practice.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1
#                     Date: 2022-05-22


#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum2(self,arr, n, s):
        ans = []
        for i in range (0, n):
            curr_sum += 0
            for j in range(i, n):
                curr_sum += arr[j]
                if s == curr_sum:
                    ans = [i+1, j+1]
                    return ans
                if curr_sum > s:
                    break
        return
    
    def subArraySum(self,arr,n, s):
        ans = []
        curr_sum = 0
        for i in range (0, n):
            curr_sum += arr[i]
            j = 0
            if curr_sum > s:
                while curr_sum > s:
                    curr_sum -= arr[j]
                    j += 1
            if curr_sum == s:
                ans = [j+1, i+1]
                return ans
            
        ans = [-1]
        return ans
                        
    
import math

def main():
    T=int(input())
    while(T>0):
        
        NS=input().strip().split()
        N=int(NS[0])
        S=int(NS[1])
        
        A=list(map(int,input().split()))
        ob=Solution()
        ans=ob.subArraySum(A, N, S)
        
        for i in ans:
            print(i, end=" ")
            
        print()
        
        T-=1


if __name__ == "__main__":
    main()
