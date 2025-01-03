def solve():
    n, m = map(int, input().split())
    
    s = []
    visited = [False] * (n + 1)
    
    def backtrack(k):
        if k == m:
            print(*s)
            return
        
        for i in range(1, n + 1):
            if not visited[i]:
                visited[i] = True
                s.append(i)
                backtrack(k + 1)
                s.pop()
                visited[i] = False
                
    backtrack(0)

solve()
