import torch

# 定义长度分别为3个长度的坐标: [0,2] [1,0] [1,2],
indices = torch.tensor([[0, 1, 2], [0, 1, 2]])
# 以上3组从坐标对应的三个非0元素 3,4,5
values = torch.tensor([1, 2, 3], dtype=torch.float32)
# 原张量的形状是一个2,4的tensor, 如果用稠密方式打印，打看到一个2,4的变量
x = torch.sparse_coo_tensor(indices, values, (3, 3)).to_dense()

# torch.eye(3, 3)

print(x)
