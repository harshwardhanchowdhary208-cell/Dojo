def solve():
    n, target = map(int, input().split())
    arr = list(map(int, input().split()))
    
    i = 0
    p = n - 1

    min_diff = float('inf')
    best_pair = (0, 0)
    
    while i < p:
        current_sum = arr[i] + arr[p]
        current_diff = abs(current_sum - target)
        
        if current_diff < min_diff:
            min_diff = current_diff
            best_pair = (arr[i], arr[p])
            
        elif current_diff == min_diff:
            if current_sum < (best_pair[0] + best_pair[1]):
                best_pair = (arr[i], arr[p])
        
        if current_sum < target:
            i += 1
        elif current_sum > target:
            p -= 1
        else:
            break
            
    print(best_pair[0], best_pair[1])

solve()
