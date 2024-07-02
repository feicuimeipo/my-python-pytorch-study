from torch.utils.tensorboard import SummaryWriter
from torchvision import transforms
from PIL import Image

"""
用ToTensor将PIL图片转为Tensor图片
"""
# 绝对路径 D:\workspace\python\learn_torch\data\train\ants\0013035.jpg
img_path = "data/train/bees/16838648_415acd9e3f.jpg"
img = Image.open(img_path)
trans_toTensor = transforms.ToTensor()
img_tensor = trans_toTensor(img)

writer = SummaryWriter("logs")
writer.add_image("tensor_img", img_tensor)

"""
2. 用Normalize实现Tensor图片归一化
"""
trans_norm_0 = transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5, ])
img_norm_0 = trans_norm_0(img_tensor)
writer.add_image("Normalize", img_norm_0, 1)

trans_norm = transforms.Normalize([6, 3, 2], [9, 3, 5])
img_norm = trans_norm(img_tensor)
writer.add_image("Normalize", img_norm, 2)
# 运行，测蔗
# tensorboard  --logdir=logs


"""
2. Resize-等比例缩放
"""
trans_resize = transforms.Resize((512, 512))
# img_PIl --> img_resize PIL
img_resize = trans_resize(img)
# image PIl ---> toTensor --> 转为 tensor
img_resize = trans_toTensor(img_resize)
# print(img_resize)
writer.add_image("Resize", img_resize, 1)

"""
transforms.Compose
# trans_toTensor： 输入
# trans_resize_2： 输出
"""
trans_resize_2 = transforms.Resize(100)
trans_compose = transforms.Compose([trans_resize_2, trans_toTensor])
img_resize_2 = trans_compose(img)
writer.add_image("Resize", img_resize_2, 0)

"""
transforms.RandomCrop：随机裁剪
"""
trans_random = transforms.RandomCrop((150, 500))
trans_compose_2 = transforms.Compose([trans_random, trans_toTensor])
for i in range(10):
    img_crop = trans_compose_2(img)
    writer.add_image("RandomCrop", img_crop, i)


writer.close()
