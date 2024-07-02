import torch
import numpy as np

# 创建一个 numpy ndarray
numpy_tensor = np.random.randn(10, 20)

# 我们可以使用下面两种方式将numpy的ndarray转换到tensor上
pytorch_tensor1 = torch.Tensor(numpy_tensor)
pytorch_tensor2 = torch.from_numpy(numpy_tensor)

# 同时我们也可以使用下面的方法将 pytorch tensor 转换为 numpy ndarray
# 如果 pytorch tensor 在 cpu 上
numpy_array = pytorch_tensor1.numpy()

# 如果 pytorch tensor 在 gpu 上
numpy_array = pytorch_tensor1.cpu().numpy()



torch.empty()
torch.randint()