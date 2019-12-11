# coding=utf-8
import numpy as np
from .hsnum import harsnum_e
from .jade import jade

#path='fuzhixiangwei1000.xlsx'
def porhowlyuu(XX1,XX2):
    Node_num = 14
    m = harsnum_e(XX1,XX2).get('hs_num')
    MatrixDX = harsnum_e(XX1,XX2).get('MatrixDX')
    MatrixDXDX = harsnum_e(XX1,XX2).get('MatrixDXDX')
    DA, DSe = jade(MatrixDX, m, XX1,XX2)
    xieboyuanjuzhen1 = np.ones(shape=[m, Node_num])
    xieboyuanjuzhen = np.mat(xieboyuanjuzhen1)
    xieboyuandingwei = []
    for i in range(m):
        for j in range(Node_num):
            temp = np.mat(np.corrcoef((DSe[i, :]).T, (MatrixDXDX[j, :]).T, rowvar=False))
            xieboyuanjuzhen[i, j] = abs(temp[0, 1])
    print(xieboyuanjuzhen)
    print('谐波源为：', xieboyuanjuzhen.argmax(axis=1) + 1)
    return xieboyuanjuzhen.argmax(axis=1) + 1
