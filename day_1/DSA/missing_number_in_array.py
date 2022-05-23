#                     Name : Arif Khan
#                     Judge: geeks for geeks
#                     problem: Missing number in array
#                     Difficulty: Easy
#                     Time Complexity: O(N)
#                     Problem Link: https://practice.geeksforgeeks.org/problems/missing-number-in-array1416/1
#                     Date: 2022-05-22

class Solution:
    def MissingNumber(self,array,n):
        org_sum = n*(n+1) // 2
        arr_sum = 0
        for i in array:
            arr_sum += i
        return org_sum - arr_sum


t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().MissingNumber(a,n)
    print(s)