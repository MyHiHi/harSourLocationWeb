# coding=utf-8

import numpy as np
import math

def joint_diag_rc(A, threshold):
    '''
    % Givens旋转子程序
            % 输入：A-需要联合对角化的矩阵
    %      threshold-门限值，判断迭代终止条件
            % 输出：V-酉矩阵
    '''
    [m, nm] = A.shape
    V_a = np.eye(m, m)
    V = np.mat(V_a)
    encore = 1
    while encore:
        encore = 0
        for p in range(1, m):
            for q in range(p + 1, m + 1):
                '''
                  计算Givens旋转  计算g矩阵，g矩阵为一个2*m维矩阵，
                '''
                gtemp = np.mat(A[p - 1, p - 1:nm:m] - A[q - 1, q - 1:nm:m])
                gte = np.row_stack((gtemp, A[p - 1, q - 1:nm:m] + A[q - 1, p - 1:nm:m]))
                g = (gte .dot(gte.H)).real

                ton = g[0, 0] - g[1, 1]
                toff = g[0, 1] + g[1, 0]

                theta = 0.5 * math.atan2(toff, ton + np.sqrt(ton * ton + toff * toff))
                c = np.cos(theta)
                s = np.sin(theta)

                encore = encore | (np.abs(s) > threshold)

                if (np.abs(s) > threshold):
                    '''%如果s的绝对值大于门限，就更新'''

                    Mp = A[:, p - 1 : nm : m]
                    Mq = A[:, q - 1 : nm : m]

                    tp1=c * Mp + s * Mq
                    tp2=c * Mq - s * Mp

                    A[:, p - 1: nm: m] = tp1
                    A[:, q - 1: nm: m] = tp2

                    rowp = A[p - 1, :]
                    rowq = A[q - 1, :]

                    tp3=c * rowp + s * rowq
                    tp4=c * rowq - s * rowp

                    A[p - 1, :] = tp3
                    A[q - 1, :] = tp4

                    temp = V[:, p - 1]
                    tp5=c * V[:, p - 1] + s * V[:, q - 1]
                    tp6=c * V[:, q - 1] - s * temp
                    V[:, p - 1] = tp5
                    V[:, q - 1] = tp6
    return V
