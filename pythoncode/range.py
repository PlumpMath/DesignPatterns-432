# range/enumerate


# 生成二维数组
board = [[1 for _ in range(10)] for _ in range(10)]


# enumerate的使用：遍历序列中的元素以及它们的下标
>>> t = [1 for _ in range(10)]
>>> t
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

>>> for i in enumerate(t):
...     print(i)
... 
(0, 1)
(1, 1)
(2, 1)
(3, 1)
(4, 1)
(5, 1)
(6, 1)
(7, 1)
(8, 1)
(9, 1)

# i是下标，j是元素
>>> for i, j in enumerate(t):
...     print(i,j)
... 
0 1
1 1
2 1
3 1
4 1
5 1
6 1
7 1
8 1
9 1
>>> 

