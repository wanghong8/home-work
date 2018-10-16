#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1
@author: autmanli
@license: Apache Licence
@file: homework.py
@time: 2018/10/4 20:39
"""

import numpy as np
#八皇后问题
n=0  # 记录解得个数

def eight_solve(deep, graph, path):
    '''解决八皇后问题的函数'''
    for i in range(8):
        if graph[deep][i] == 0:  # 如果这个点没有灰化，则说明是有效点
            path.append((deep + 1, i + 1))
            if deep == 7:  # 如果到了第7层，即对应第八个皇后，则输出路径，跳出此路径
                print(path)
                global n
                n = n + 1
                path.pop()
                return

            else:
                make_gray(graph, deep, i, 0, deep + 1)  # 灰化
                eight_solve(deep + 1, graph, path)
                make_gray(graph, deep, i, deep + 1, 0)  # 解灰化

            path.pop()


def make_gray(graph, x, y, oldvalue, newvalue):
    '''灰化函数,让点(x,y)所在行列，和斜线上的点为不可用，或者解除不可用状态'''
    for i in range(8):
        if graph[x][i] == oldvalue:  # 竖直方向设置为不可用
            graph[x][i] = newvalue

        if graph[i][y] == oldvalue:
            graph[i][y] = newvalue  # 横向设置为不可用

        slash(graph, x - 1, y - 1, -1, -1, oldvalue, newvalue)  # 左斜上方
        slash(graph, x + 1, y - 1, 1, -1, oldvalue, newvalue)  # 右斜上方
        slash(graph, x - 1, y + 1, -1, -1, oldvalue, newvalue)  # 左斜下方
        slash(graph, x + 1, y + 1, 1, 1, oldvalue, newvalue)  # 右斜下方


def slash(graph, x, y, x_increment, y_increment, oldvalue, newvalue):
    '''斜线方向上,graph为图数组，x为横坐标，y为纵坐标，x_increment为x方向增量，
        y_increment为y方向增量，oldvalue为老的值，newvalue为新设的值'''
    xx = x
    yy = y
    while -1 < xx < 8 and -1 < yy < 8:
        if graph[xx][yy] == oldvalue:
            graph[xx][yy] = newvalue

        xx += x_increment
        yy += y_increment


mygraph = np.zeros((8,8))

mypath = []
eight_solve(0, mygraph, mypath)
print(n)

