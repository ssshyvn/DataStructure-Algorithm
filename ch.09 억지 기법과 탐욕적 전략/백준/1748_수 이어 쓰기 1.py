def count_digits(N):
    length = 0   # 총 자리수 저장
    start = 1    # 자리수 시작 숫자
    digit = 1    # 현재 자리수

    while start <= N:   # 현재 구간의 시작 값이 N보다 작거나 같은 동안 반복.(구간별로 계산 진행)
        end = min(N, start * 10-1)  # 현재 자리수에서의 끝 숫자
        length += (end-start+1) * digit # 해당 자리수에서 더해질 자리수 계산.
                                        # (end-start+1: 현재 구간에 포함된 숫자의 개수,
                                        #  개수*digit: 해당 숫자들이 차지하는 총 자리수 계산)
        start *= 10  # 다음 자리수로 이동
        digit += 1  # 자리수 증가

    return length

N = int(input())
print(count_digits(N))
