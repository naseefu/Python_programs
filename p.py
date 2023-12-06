def solve(N, A, M, Q):
    prefix_sum = [0]
    for num in A:
        prefix_sum.append(prefix_sum[-1] + num)
    
    result = []
    for q in Q:
        target_profit = q
        left, right = 0, N
        days_needed = float('inf')
        
        while left <= right:
            mid = (left + right) // 2
            if prefix_sum[mid] >= target_profit:
                days_needed = min(days_needed, mid)
                right = mid - 1
            else:
                left = mid + 1
        
        if days_needed == float('inf'):
            result.append(-1)
        else:
            result.append(days_needed)
    
    return result

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    M = int(input())
    Q = list(map(int, input().split()))
    out = solve(N, A, M, Q)
    print(' '.join(map(str, out)))