MOD = 1000000007

# 행렬의 곱셈 함수
def multMat(A, B):

    # 두 개의 2x2 행렬을 곱한 후 각 요소를 MOD로 나눈 나머지를 반환
    return [[(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % MOD, (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD],
            [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % MOD, (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD]]

# 행렬의 n거듭제곱 구하는 함수(축소 정복)
def powerMat(x, n):
    if n == 1:
        return [[element % MOD for element in row] for row in x]
    elif (n % 2) == 0:
        return powerMat(multMat(x, x), n // 2)
    else:
        return multMat(x, powerMat(multMat(x, x), (n - 1) // 2))

# 피보나치 수열 구하는 함수
def fib_mat(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    mat = [[1, 1], [1, 0]]
    result = powerMat(mat, n)
    return result[0][1]

# 입력 및 출력
n = int(input())
print(fib_mat(n))
