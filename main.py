import multiprocessing as mp
import yaml
import random
from typing import List

def element(i: int, j: int, A: list, B: list, answer: mp.Queue):
    answer.put((sum(A[i][k] * B[k][j] for k in range(len(A[0]) or len(B))), [i, j]))

def matrix_reader(file_name : str):
    """Читает матрицу из уазанного файла"""
    with open (file_name, "r") as file:
        return yaml.load(file)

def matrix_gen(n : int, m : int) -> List[List[int]]:
    """генерация матрицы"""
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(random.randint(1,100))
    return matrix

def main():
    manager = mp.Manager()

    n = int(input('Введите кол-во строк в матрице -> '))
    m = int(input('Введите кол-во столбцов в матрице -> '))
    matrix1 = matrix_gen(n,m)
    matrix2 = matrix_gen(m,n)



if __name__ == '__main__':
    main()