def find_a_factor(N):
    factor_list = []
    
    for num in range(1, (N // 2) + 1):
        if N % num == 0:
            factor_list.append(num)
    return factor_list


def whole_factor_sum(N):
    factor_list = find_a_factor(N)
    
    if sum(factor_list) == N:
        answer = f"{N} = {' + '.join(map(str, factor_list))}"
    else:
        answer = f"{N} is NOT perfect."
        
    return answer


if __name__ == "__main__":
    while True:
        N = int(input())
        
        if N == -1:
            break
            
        print(whole_factor_sum(N))