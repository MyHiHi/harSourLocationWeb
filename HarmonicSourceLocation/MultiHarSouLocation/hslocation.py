# coding=utf-8
import numpy as np
from .hsnum import harsnum_e
from .jade import jade

#path='fuzhixiangwei1000.xlsx'
def porhowlyuu(X,XX):
    Node_num = 14
    m = harsnum_e(X,XX).get('hs_num')
    MatrixDX = harsnum_e(X,XX).get('MatrixDX')
    MatrixDXDX = harsnum_e(X,XX).get('MatrixDXDX')
    DA, DSe = jade(MatrixDX, m,X,XX)
    xieboyuanjuzhen1 = np.ones(shape=[m, Node_num])
    xieboyuanjuzhen = np.mat(xieboyuanjuzhen1)
    xieboyuandingwei = []
    for i in range(m):
        for j in range(Node_num):
            temp = np.mat(np.corrcoef((DSe[i, :]).T, (MatrixDXDX[j, :]).T, rowvar=False))
            xieboyuanjuzhen[i, j] = abs(temp[0, 1])
    # print(xieboyuanjuzhen)
    location=(xieboyuanjuzhen.argmax(axis=1) + 1)
    # print('谐波源为：', location)
    return xieboyuanjuzhen,location
