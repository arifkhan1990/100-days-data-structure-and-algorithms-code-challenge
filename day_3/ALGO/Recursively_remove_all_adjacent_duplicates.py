#                     Name : Arif Khan
#                     Judge: geeks for geeks
#                     problem: Recursively remove all adjacent duplicates
#                     Difficulty: Medium
#                     Time Complexity: O(N*N)
#                     Problem Link: https://practice.geeksforgeeks.org/problems/recursively-remove-all-adjacent-duplicates0744/1#
#                     Date: 2022-05-24



#User function Template for python3
import sys
sys.setrecursionlimit(10**5)

class Solution:
    def rremove (self, S):
        adjacent_st = ""
        flag = 1
        if len(S) == 1:
            return S
		for i in range(len(S)):
		    if i == len(S)-1 and S[i] != S[i-1]:
		        adjacent_st += S[i]
		    elif i == 0 and S[i] != S[i+1]:
		        adjacent_st += S[i]
		    elif i > 0 and i < len(S)-1 and S[i] != S[i+1] and S[i] != S[i-1]:
		        adjacent_st += S[i]
		    else:
		        flag = 0
		if flag == 0:
		    return self.rremove(adjacent_st)
		return adjacent_st

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range (t):
        S = input()
        ob = Solution()
        print(ob.rremove(S))


# } Driver Code Ends