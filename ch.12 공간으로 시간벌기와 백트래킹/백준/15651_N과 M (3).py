def solve():
    n, m = map(int, input().split())
    
    s = []
    
    def backtrack(k):
        if k == m:
            print(*s)
            return
        
        for i in range(1, n + 1):
            s.append(i)
            backtrack(k + 1)
            s.pop()
                
    backtrack(0)

solve()
