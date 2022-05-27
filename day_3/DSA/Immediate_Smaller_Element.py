#                     Name : Arif Khan
#                     Judge: geeks for geeks
#                     problem: Immediate Smaller Element
#                     Difficulty: Easy
#                     Time Complexity: O(N)
#                     Problem Link: https://practice.geeksforgeeks.org/problems/immediate-smaller-element1142/1
#                     Date: 2022-05-24

#User function Template for python3
class Solution:
    def immediateSmaller(self,arr,n):
        for i in range(n):
            if i < n-1 and arr[i] > arr[i+1]:
                arr[i] = arr[i+1]
            else:
                arr[i] = -1
        return arr

#{ 
#  Driver Code Starts

if __name__ == '__main__':
    tcs=int(input())

    for _ in range(tcs):
        n=int(input())
        arr=[int(x) for x in input().split()]
        ob = Solution()
        ob.immediateSmaller(arr,n)
        for x in arr:
            print(x, end=" ")
        print()
# } Driver Code Ends