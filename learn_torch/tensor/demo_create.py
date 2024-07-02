import numpy as np
import torch


def printTensor(tensor):
    print(tensor)
    print("numel =", tensor.numel())
    # 张量中元素个数确定
    print("dim =", tensor.dim())
    # 张量的维度确定
    print("type =", tensor.type())


'''常用的Tensor定义'''
print("--------------as_tensor--------------")
shape = [[2, 3], [4, 5], [6, 7]]
# 张量的形状确定的两种方法：
# 1. 属性确定：可以使用张量的shape属性确定张量的形状；
# 2. 方法确定：可以使用张量的size()方法确定张量的形状。
tensor = torch.as_tensor(shape)
printTensor(tensor)

print("--------------Tensor(* Size)--------------")
shape = [(2, 3), (4, 5), [6, 7]]
tensor1 = torch.Tensor(shape)
printTensor(tensor1)

print("--------------numpy.array()--------------")
data_array = np.array([[2, 3], [4, 5], [6, 7]])
tensor = torch.tensor(data_array)
printTensor(tensor)

# 创建一个3行3列的张量
print("--------------torch.ones--------------")
tensor = torch.ones((3, 3))
printTensor(tensor)

print("--------------torch.zeros--------------")
tensor = torch.zeros(2, 2)
printTensor(tensor)

print("--------------torch.zeros_like--------------")
tensorlike = torch.zeros_like(tensor1)
printTensor(tensorlike)

print("--------------torch.randn--------------")
tensor = torch.randn(2, 2)
printTensor(tensor)

'''正态分布'''
print(u"--------------torch.normal mean为均值，std为标准差-1--------------")
# std=5组不同的正诚分布，5组都是随机的标准差和 mean =0
tensor = torch.normal(mean=0.0, std=torch.rand(5))
printTensor(tensor)

print(u"--------------torch.normal mean为均值，std为标准差-2--------------")
# std=5组不同的正诚分布，5组都是随机的标准差和随机的mean
tensor = torch.normal(mean=torch.rand(5), std=torch.rand(5))
printTensor(tensor)

print(u"--------------torch.uniform_--------------")
tensor = torch.Tensor(4, 2).uniform_()
printTensor(tensor)

'''定义一个序列'''
print(u"--------------torch.arange--------------")
# 定义一个序列, 步长为2， 最后10不包含在序列中
tensor = torch.arange(0, 10, 2)
printTensor(tensor)

print(u"--------------torch.linspace--------------")
# 等间节切分,5为个数，11为范围，0为起始值
tensor = torch.linspace(0, 11, 5)
printTensor(tensor)

# 定义长度分别为3个长度的坐标: [0,2] [1,0] [1,2],
indices = torch.tensor([[0, 1, 1], [2, 0, 2]])
# 以上3组从坐标对应的三个非0元素 3,4,5
values = torch, tensor([3, 4, 5], dtype=torch.float32)
# 原张量的形状是一个2,4的tensor
x = torch.sparse_coo_tensor(indices, values, [2, 4])
