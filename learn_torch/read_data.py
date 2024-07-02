# 路径
import os.path

# 引入Dataset
from torch.utils.data import Dataset

# 图像操作
from PIL import Image


# import cv2
# 继承：Dataset
class MyData(Dataset):

    # 实始化函数
    def __init__(self, root_dir, label_dir):
        """
         根目录：root_dir
         用目录标签：label_dir
        """
        # 创建时给赋值的变量为全局变量 self.xxx
        self.root_dir = root_dir
        self.label_dir = label_dir
        self.path = os.path.join(self.root_dir, self.label_dir)
        self.img_path = os.listdir(self.path)
        pass

    def __getitem__(self, idx):
        """
          返回一张图片
         :param idx: 图片所有位置index 从0开始
         :return: image对象与标签名
         """

        # 得到文件名
        img_name = self.img_path(idx)
        img_item_path = os.path.join(self.root_dir, self.label_dir, img_name)
        img = Image.open(img_item_path)
        label = self.label_dir
        return img, label

    def __len__(self):
        """
         数据集长度
         :return: 长度
        """
        return len(self.img_path)


if __name__ == '__main__':
    # 指定数据文件夹
    root_dir = "data/train"
    # 标签文件夹
    ant_label_dir = "ants"
    bees_label_dir = "bees"
    # 某一种签检集
    ants_dataset = MyData(root_dir, ant_label_dir)
    bees_dataset = MyData(root_dir, bees_label_dir)
    # 标签合集 - 拼接2或多个小的数据集
    train_data = ants_dataset + bees_dataset
    # 打印数据集长度
    total = len(train_data)
    print(total)
