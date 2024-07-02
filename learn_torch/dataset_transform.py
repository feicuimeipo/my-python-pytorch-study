import torchvision.datasets
from torch.utils.tensorboard import SummaryWriter

# 将图片数据都转为tensor类型
# 可以对数据集做任何transforms范围内的操作，该例子只针对数据做toTensor
dataset_transform = torchvision.transforms.Compose([
    torchvision.transforms.ToTensor
])

# 使用CIFAR10数据集
# 如果下载比较慢，可以将控制台打印的下载链接放到专门的下载工具中下载,下载的是一个压缩包，会自动解压
train_set = torchvision.datasets.CIFAR10(root="./data_torchvision_dataset", train=True, download=True)

# 测试集
test_set = torchvision.datasets.CIFAR10(root="./data_torchvision_dataset", train=False, download=True)

# 用tensorboard显示前10张图片
# 运行tensorboard  --logdir=p10
writer = SummaryWriter("logs_dataset")
for i in range(0):
    img, target = test_set[i]
    writer.add_image("dataset_transform", img, i)

writer.close()
