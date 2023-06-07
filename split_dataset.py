#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :split_dataset.py
# @Time      :2023/6/7 上午9:17
# @Author    :NMWJ
# split_data.py
# 划分数据集flower_data，数据集划分到flower_datas中，训练验证比例为8：2
import os
import random
from shutil import copy


def mkfile(file):
    if not os.path.exists(file):
        os.makedirs(file)


# 获取data文件夹下所有文件夹名（即需要分类的类名）
# 划分数据集flower_data，数据集划分到flower_datas中
file_path = '/home/xjs/lzz/mmpretrain/data/fruit30'
new_file_path = '/home/xjs/lzz/mmpretrain/data/fruit30_dataset'

# 划分比例，训练集 : 验证集 = 8 : 2
split_rate = 0.8
data_class = [cla for cla in os.listdir(file_path)]
train_path = new_file_path + '/training_set/'
val_path = new_file_path + '/val_set/'
test_path = new_file_path + '/test_set/'
mkfile(new_file_path)

# 创建 训练集train 文件夹，并由类名在其目录下创建子目录
mkfile(train_path)
for cla in data_class:
    mkfile(train_path + cla)

# 创建 验证集val 文件夹，并由类名在其目录下创建子目录
mkfile(val_path)
for cla in data_class:
    mkfile(val_path + cla)

# 创建 测试集val 文件夹，并由类名在其目录下创建子目录
mkfile(test_path)
for cla in data_class:
    mkfile(test_path + cla)

# 遍历所有类别的全部图像并按比例分成训练集和验证集
for cla in data_class:
    cla_path = file_path + '/' + cla + '/'  # 某一类别的子目录
    images = os.listdir(cla_path)  # images 列表存储了该目录下所有图像的名称
    num = len(images)
    train_index = random.sample(images, k=int(num * split_rate))  # 从images列表中随机抽取 k 个图像名称
    val_test_index = []
    for index, image in enumerate(images):
        # train_index 中保存验证集val的图像名称
        if image in train_index:
            image_path = cla_path + image
            new_path = train_path + cla
            copy(image_path, new_path)
        else:
            val_test_index.append(image)

    val_index = random.sample(val_test_index, k=int(len(val_test_index) * 0.5))

    for image in val_test_index:
        # val_index 中保存验证集val的图像名称
        if image in val_index:
            image_path = cla_path + image
            new_path = val_path + cla
            copy(image_path, new_path)  # 将选中的图像复制到新路径

        # 其余的图像保存在训练集test中
        else:
            image_path = cla_path + image
            new_path = test_path + cla
            copy(image_path, new_path)
        # print("\r[{}] processing [{}/{}]".format(cla, index + 1, num), end="")  # processing bar
        # print()

print("processing done!")



