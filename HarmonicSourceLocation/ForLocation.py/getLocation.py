import numpy as np
# from du import  excel_to_matrix
from .toMatrix import banch


def suanfa(matrix, Is, t):
    # datafile1 ='D:\\xiebo\\test3.xls'
    A = matrix
    # A = excel_to_matrix(datafile1);

    row, col = A.shape
    Az = np.transpose(A)
    M = row
    N = col
    # datafile2 ='D:\\xiebo\\yyy.xls'
    y = Is
    # y = excel_to_matrix(datafile2)

    rn = np.zeros((M, 1), dtype='complex128')  # 定义一个都为0的列
    product = np.zeros((M, 1), dtype='complex128')
    thls = np.zeros((M, 1), dtype='complex128')
    theta = np.zeros((M, 1), dtype='complex128')

    ss = 0
    # for ss in range(M):
    #      rn[ss,0] = y[ss,0]+1j*y[ss,1]
    # y = rn
    rn = y

# ***************************************
    # t = 11#迭代次数t

    At = np.zeros((M, N))  # 定义一个全都是0的矩阵，用来存储列
    Zero = np.zeros((M, 1))  # 定义一个都为0的列
    Post = np.zeros((1, t))  # 存储这一列的序号

    for ii in range(t):
        product = np.dot(Az, rn)

        val = max(list(map(abs, product)))
        pos = list(map(abs, product)).index(val)
        At[:, ii] = A[:, pos]
        Post[0, ii] = pos
        A[:, pos] = [0]*M

        temp1 = np.transpose(At[:, 0:ii+1])
        temp2 = np.linalg.inv(np.dot(temp1, At[:, 0:ii+1]))
        thls = np.dot(np.dot(temp2, temp1), y)
        rn = y - np.dot(At[:, 0:ii+1], thls)

    o = 0

    for o in range(t):
        theta[int(Post[0, o]), 0] = complex(thls[o, 0])
    # print(theta)
    arr = abs(theta)
    # print(arr)
    # return theta

    p1 = np.sort(arr, axis=0)
    p2 = np.argsort(arr, axis=0)

    p1 = p1[::-1]
    p2 = p2[::-1]  # 这是把数据倒过来的函数，我也不知道怎么倒过来的
    for i in range(len(p1)):
        print(p2[i]+1, ":", p1[i])
