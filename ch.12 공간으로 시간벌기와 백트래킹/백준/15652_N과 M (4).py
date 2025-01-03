def solve():
    n, m = map(int, input().split())
    
    s = []
    
    def backtrack(k, start):
        if k == m:
            print(*s)
            return
        
        for i in range(start, n + 1):
            s.append(i)
            backtrack(k + 1, i)
            s.pop()
                
    backtrack(0, 1)

solve()
