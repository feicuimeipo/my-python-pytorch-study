import torchvision.utils
from torch.utils.tensorboard import SummaryWriter
from PIL import Image
import numpy as np

# 实始化一个SummaryWriter, 图径logs，该路么要和tensorboard --logdir=logs 相对
writer = SummaryWriter()

"""
add_image的使用
"""
ants_img_path = "data_for_tensorboard/train/ants_image/0013035.jpg"
img_PIL = Image.open(ants_img_path)
# 将img_path路径对应的图片对象转为numpy类型, 并赋值给image
img_array = np.array(img_PIL)
# 查看图片通道 默认的通道以在最后一位
# 从PIL到numpy，需要在add_images()中指定shape中每一个数字/维表示的含义，即要设置add_image中dataformats参数
writer.add_image("test", img_array, 1, dataformats="HWC")



bees_img_path = "data_for_tensorboard/train/bees_image/16838648_415acd9e3f.jpg"
bees_img_PIL = Image.open(bees_img_path)
bees_img_array = np.array(bees_img_PIL)
writer.add_image("test", bees_img_array, 3, dataformats="HWC")



"""
# add_scalar() 的使用
"""
for i in range(200):
    # 图是的展示是根据title来里合的
    # 当x和y轴改变时，需要将title一起改否则图像会有问题 (被拟合在一块，除非本身就需要执行这样的拟合），
    # 当存错误的拟合问题时：解决办法是将logs文件下的文件删除重新开始
    writer.add_scalar("y=x", i, i)



# 关闭
writer.close()

