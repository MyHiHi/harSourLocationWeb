# coding=utf-8

import numpy as np

def harsnum_e(XX1,XX2):
    X = np.array([XX1, XX2])
    XX = np.array([XX1, XX2])
    # X = np.array([XX6, XX8,XX12,XX14])
    # XX = np.array([XX1, XX2, XX3, XX4, XX5, XX6, XX7, XX8, XX9, XX10, XX11, XX12, XX13, XX14])

    MatrixX = np.mat(X)
    MatrixXX = np.mat(XX)
    MatrixXt = MatrixX.T

    z1 = np.empty(shape=[MatrixX.shape[0], MatrixX.shape[1] - 1])
    MatrixDX = np.mat(z1)
    for i in range(MatrixX.shape[0]):
        for j in range(MatrixX.shape[1] - 1):
            MatrixDX[i, j] = MatrixX[i, j + 1] - MatrixX[i, j]
    z2 = np.empty(shape=[MatrixXX.shape[0], MatrixXX.shape[1] - 1])
    MatrixDXDX = np.mat(z2)
    for i in range(MatrixXX.shape[0]):
        for j in range(MatrixXX.shape[1] - 1):
            MatrixDXDX[i, j] = MatrixXX[i, j + 1] - MatrixXX[i, j]
    MatrixDXt = MatrixDX.T
    MatrixXXT = MatrixDX.dot(MatrixDXt)
    tezhengzhi, tezhengxiangliang = np.linalg.eig(MatrixXXT)
    tezhengshunxu = sorted(tezhengzhi, reverse=True)
    bizhik = np.array(range(len(tezhengshunxu) - 1), dtype=np.float32)
    for i in range(len(tezhengshunxu) - 1):
        bizhik[i] = tezhengshunxu[i + 1] / tezhengshunxu[i]
    list_bizhik = bizhik.tolist()
    hs_num = list_bizhik.index(bizhik.min()) + 2

    dict = {'MatrixX': MatrixX,
            'hs_num': hs_num,
            'MatrixDX': MatrixDX,
            'MatrixDXDX': MatrixDXDX}

    return dict
