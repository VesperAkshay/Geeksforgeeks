#User function template for Python

class Solution:	
	def remove_duplicate(self, A, N):
	    if N == 0 or N == 1:
            return N

    
        st = []

        
        for i in range(N):

            if not st or A[i] != st[-1]:
                st.append(A[i])

        
        for i in range(len(st)):
            A[i] = st[i]

        return len(st)


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        N = int(input())
        A = list(map(int, input().strip().split()))
        ob = Solution()
        n = ob.remove_duplicate(A,N)
        for i in range(n):
            print(A[i], end=" ")
        print()


# } Driver Code Ends