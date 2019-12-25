# 分支界限计算最短路径和最短路径长度
import math
import numpy as np
from copy import deepcopy
# 初始化图参数 用字典初始初始化这个图

# def zhuan(graph):
# graph = {1: {1:0,2: 8, 5: 9},
#          2: {3: 7},
#          3: {4: 6},
#          4: {7: 5},
#          5: {6: 10},
#          6: {11: 11, 12: 12},
#          7: {8: 4, 9: 3},
#          8: {},
#          9: {10: 2, 14: 1},
#          10: {},
#          11: {},
#          12: {13: 13},
#          13: {},
#          14: {},
#          }

# 分支界限：计算起始节点到其他所有节点的最短距离
"""
1.将起始节点入队，并且初始化起始节点到其他所有节点距离为inf，用costs
2.检测起始节点的到子节点的距离是否变短，若是，则将其子节点入队
3.子节点全部检测完，则将起始节点出队，
4.让队列中的第一个元素作为新的起始节点，重复1,2,3,4
5.对队列为空，则退出循环
"""


# 数据结构：队列，树
def banch(graph, start):
    costs = {}  # 记录start到其他所有点的距离
    trace = {start: [start]}  # 记录start到其他所有点的路径

    # 初始化costs
    for key in graph.keys():
        costs[key] = math.inf
    costs[start] = 0

    queue = [start]  # 初始化queue

    while len(queue) != 0:
        head = queue[0]  # 起始节点
        for key in graph[head].keys():  # 遍历起始节点的子节点
            dis = graph[head][key] + costs[head]
            if costs[key] > dis:
                costs[key] = dis
                temp = deepcopy(trace[head])  # 深拷贝
                temp.append(key)
                trace[key] = temp  # key节点的最优路径为起始节点最优路径+key
                queue.append(key)

        queue.pop(0)  # 删除原来的起始节点
    # print(costs)
    # print(trace)

    ans=[];
    for k,v in trace.items():
        temp=[]
        for j in range(len(v)-1):
            x1,x2=v[j],v[j+1];
            lp=graph.get(x1,0).get(x2,0);
            if lp:
                temp.append(lp);
        ans.append(temp);
    ans.pop(0)
    # print(ans)

    tx = trace.keys()

    tx =list(tx)
    b = [i - 1 for i in tx]
    # print(b)
    b.pop(0)
    # print(b)
    tx = b
    # print(tx)

    num = 13
    M = np.zeros((num, num))

    for i in range(len(tx)):
        lie = tx[i]
        print(lie)

        hang = ans[i]
        print(hang)
        for m in range(len(hang)):
            M[hang[m]-1,lie-1] = 1
    # print(M)
    return M


# banch(graph, 1)
# return(M)