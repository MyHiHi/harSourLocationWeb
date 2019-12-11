# coding=utf-8

import numpy as np
from numpy import sqrt, mean
from scipy.linalg import sqrtm
from .hsnum import harsnum_e
from .joint_diag_rc import joint_diag_rc


def jade(MatrixDX, m, XX1,XX2):
    #path = 'fuzhixiangwei1000.xlsx'
    #path = 'week.xlsx'
    m = harsnum_e(XX1,XX2).get('hs_num')
    MatrixDX = harsnum_e(XX1,XX2).get('MatrixDX')

    MatrixDXt = MatrixDX.T

    [n, T] = (MatrixDX.shape)

    nem = m
    seuil = 1 / sqrt(T) / 100
    '''
    1. 白化过程，得到白化后的信号Y，白化矩阵W
    '''
    if m < n:
        D, U = np.linalg.eig(MatrixDX.dot(MatrixDXt) / T)
        puiss_sortlist = sorted(D, reverse=False)
        k = np.array(np.argsort(np.abs(D)))
        ibl_sortlist = sqrt(puiss_sortlist[n - m:n] - mean(puiss_sortlist[0:n - m]))
        ibl = np.diag(ibl_sortlist)
        z = np.empty(shape=[ibl.shape[0], ibl.shape[1]])
        bl = np.mat(z)

        for i in range(ibl.shape[0]):
            bl[i, i] = 1 / ibl[i, i]
            W = bl.dot((U[0:n, k[n - m :n]]).T)
            IW = (U[0:n, k[n - m :n]]).dot(ibl)
    else:
        IW = sqrtm(MatrixDX.dot(MatrixDXt) / T)
        W = np.matrix(IW).I
    '''
    Y为白化后的观测信号
    YY为Y的转置矩阵
    '''
    Y = W.dot(MatrixDX)
    YY = Y.T

    '''
    2. 计算四阶积累量矩阵 M
    '''
    R = (Y.dot(YY)) / T
    C = (Y.dot(YY)) / T

    Yl = np.zeros([1, T], dtype=np.complex64)
    Ykl = np.zeros([1, T], dtype=np.complex64)
    Yjkl = np.zeros([1, T], dtype=np.complex64)
    '''%Q初始化为(m*m*m*m)*1的列向量'''
    Q = np.zeros([m * m * m * m, 1], dtype=np.complex64)

    index = 0

    '''
    四阶积累量矩阵计算公式
    '''
    for lx in range(1, m + 1):
        Yl = Y[lx - 1, :]
        '''Yl=Y矩阵的第lx行'''
        for kx in range(1, m + 1):
            p = (np.conj(Y[kx - 1, :]))
            Ykl = np.multiply(Yl, (np.conj(Y[kx - 1, :])))
            '''Yk1=Y1*Y矩阵kx行的共轭'''
            for jx in range(1, m + 1):
                Yjkl = np.multiply(Ykl, (np.conj(Y[jx - 1, :])))
                '''Yjk1=Yk1*Y矩阵jx行的共轭'''
                for ix in range(1, m + 1):
                    '''Q为一个列向量，R(ix,jx)表示R矩阵第ix行第jx列的元素，conj(C(jx,kx))表示C矩阵dijx行第kx列元素的共轭,'''
                    Q[index] = Yjkl * (Y[ix - 1, :].H) / T - R[ix - 1, jx - 1] * R[lx - 1, kx - 1] - R[ix - 1, kx - 1] * R[lx - 1, jx - 1] - C[ix - 1, lx - 1] * np.conj(C[jx - 1, kx - 1])
                    index = index + 1

    '''
    Q.reshape((m * m), (m * m))矩阵进行奇异值分解，得到特征向量矩阵U和特征值矩阵D
    '''

    D, U = np.linalg.eig((Q.reshape((m * m), (m * m))))
    la = sorted(abs(D), reverse=False)
    K = np.array(np.argsort(np.abs(D)) + 1)

    '''
    初始化四阶积累量矩阵组M，此时M是一个m行，nem*m列的矩阵，初始化为0矩阵
    '''
    M = np.zeros([m, nem * m], dtype=np.complex64)
    Z = np.zeros([m, m], dtype=np.complex64)
    h = m * m

    for u in range(1, m * nem, m):
        Z = U[:, K[h - 1]-1].reshape(m, m).T
        M[:, u - 1:u + m - 1] = la[h - 1] * Z
        h = h-1
    '''
    3. 应用joint_diag_rc子函数对四阶积累量矩阵M进行联合近似对角化
    '''
    seuil = 1 / sqrt(T) / 100
    V = joint_diag_rc(M, seuil)
    '''
    估计混合矩阵A和分离出源信号S   %混合矩阵A=IW*酉矩阵V  源信号的估计值S=酉矩阵的共轭转置矩阵V'*白化信号Y
    '''
    DA = IW.dot(V)
    DS = V.H.dot(Y)

    return DA, DS
