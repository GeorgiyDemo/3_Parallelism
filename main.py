import multiprocessing as mp
import yaml
import random
from typing import List

def print_matrix(matrix : List[List[int]]) -> None:
    """Вывод матрицы на экран"""
    r = "\n" + "\n".join(["\t".join([str(cell) for cell in row]) for row in matrix])
    print(r)

def matrix_reader(file_name : str):
    """Читает матрицу из уазанного файла"""
    with open (file_name, "r") as file:
        return yaml.load(file)

def matrix_gen(n : int, m : int) -> List[List[int]]:
    """Генерация матрицы"""
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(random.randint(1,100))
    return matrix

def worker(i: int, j: int, A: list, B: list, que: mp.Queue) -> None:
    """
    Обработчик перемножения элементов матрицы
    Запускается в отдельном процессе
    """
    
    buffer_list = []
    for k in range(len(A[0]) or len(B)):
        buffer_list.append(A[i][k] * B[k][j])

    result_dict = {}
    result_dict["result"] = sum(buffer_list)
    result_dict["i"] = i
    result_dict["j"] = j
    
    que.put(result_dict)

def main():
    manager = mp.Manager()

    n = int(input('Введите кол-во строк в матрице -> '))
    m = int(input('Введите кол-во столбцов в матрице -> '))
    matrix1 = matrix_gen(n,m)
    matrix2 = matrix_gen(m,n)
    matrix3 = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix2[0]))]

    print_matrix(matrix1)
    print_matrix(matrix2)

    #Список процессов
    processes_list = list()
    #Очередь ответов
    que = manager.Queue()

    for i in range(len(matrix3)):
        for j in range(len(matrix3[i])):
            p = mp.Process(target=worker, args=(i, j, matrix1, matrix2, que, ))
            processes_list.append(p)

    for p in processes_list: p.start()
    for p in processes_list: p.join()

    for i in range(len(matrix3)):
        for j in range(len(matrix3[i])):
            r = que.get()
            matrix3[r["i"]][r["j"]] = r["result"]
    
    print_matrix(matrix3)

if __name__ == '__main__':
    main()