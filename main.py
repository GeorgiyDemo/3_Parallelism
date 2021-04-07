from multiprocessing import Process, Pool


def element(index, A, B):
    i, j = index
    res = 0
    # get a middle dimension
    N = len(A[0]) or len(B)
    for k in range(N):
        res += A[i][k] * B[k][j]
    return res


def main():
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[2, 0], [1, 2]]

    res = 0

    p1 = Process(target=element, args=[(0, 0), matrix1, matrix2, res])
    p1.start()
    p1.join()

    print(res)

if __name__ == '__main__':
    main()