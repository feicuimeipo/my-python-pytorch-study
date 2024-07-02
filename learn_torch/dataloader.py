import torchvision.datasets
from torch.utils.data import DataLoader

# 准备的测试数据集
from torch.utils.tensorboard import SummaryWriter

test_data = torchvision.datasets.CIFAR10("./data_torchvision_dataset", train=False, transform=torchvision.transforms.ToTensor(),download=True)
# 加载测试集:取四个数据，进行打包,batch_size = 20 数据一共四条，0~3
test_loader = DataLoader(dataset=test_data, batch_size=64, shuffle=True, num_workers=0, drop_last=True)

# 测试数据集中第一张图片，及target
# target指目录在classes包下label的索引
img, target = test_data[0]
print("channel:", img.shape)
print("label=", test_data.classes[target])
print("dataset_len=", len(test_data))

# 展示
writer = SummaryWriter("logs_dataloader")
# 重复输出两次相同的数据,shuffle=True代表两次数据顺序不同
for epoch in range(2):
    step = 0
    for data in test_loader:
        # 读取数据
        # 实际操作时，读取完数据后，会将读出的数据直接输送到神经网络，作为神网的输入
        myImg, myTarget = data
        # format：格式化输出
        writer.add_images("Epoch:{}".format(epoch), myImg, step)
        step = step + 1

writer.close()