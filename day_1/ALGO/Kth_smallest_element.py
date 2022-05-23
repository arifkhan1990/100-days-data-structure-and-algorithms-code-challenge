#                     Name : Arif Khan
#                     Judge: geeks for geeks
#                     problem: Kth smallest element
#                     Difficulty: Easy
#                     Time Complexity: O(N)
#                     Problem Link: https://practice.geeksforgeeks.org/problems/kth-smallest-element5635/1#
#                     Date: 2022-05-22


class Solution:
    def kthSmallest(self,arr, l, r, k):
        arr.sort()
        return arr[k-1]

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    import random 
    t=int(input())
    for tcs in range(t):
        n=int(input())
        arr=list(map(int,input().strip().split()))
        k=int(input())
        ob=Solution()
        print(ob.kthSmallest(arr, 0, n-1, k))