from dinov2.data.datasets import ImageNet
# print(ImageNet.Split)#<enum '_Split'>
# for split in ImageNet.Split:
#     print(split) 
#     #_Split.TRAIN ==> 'train 
#     # _Split.VAL ==> 'val'
#     # _Split.TEST ==> 'test'
#     dataset = ImageNet(split=split, root="/home/jovyan/dinov2/dataset", extra="/home/jovyan/dinov2/dataset_extra2")
#     dataset.dump_extra()

import numpy as np

i = np.load('/home/jovyan/dinov2/dataset_extra/class-ids-TRAIN.npy')
print(i)#['0' '1' '2']
n = np.load('/home/jovyan/dinov2/dataset_extra/class-names-TRAIN.npy')
print(n) #['A' 'B' 'C']
e = np.load('/home/jovyan/dinov2/dataset_extra/entries-TRAIN.npy')
#(actual_index, class_index, class_id, class_name)
print(e)
#[( 10159, 0, '0', 'A') (101591, 0, '0', 'A') (101592, 0, '0', 'A')
#  (101593, 0, '0', 'A') ( 10159, 1, '1', 'B') (101591, 1, '1', 'B')
#  (101592, 1, '1', 'B') (101593, 1, '1', 'B') ( 10159, 2, '2', 'C')
#  (101591, 2, '2', 'C') (101592, 2, '2', 'C') (101593, 2, '2', 'C')]



t = np.load('/home/jovyan/dinov2/dataset_extra/entries-TRAIN.npy', mmap_mode="r")
print(t)
#[( 10159, 0, '0', 'A') (101591, 0, '0', 'A') (101592, 0, '0', 'A')
#  (101593, 0, '0', 'A') ( 10159, 1, '1', 'B') (101591, 1, '1', 'B')
#  (101592, 1, '1', 'B') (101593, 1, '1', 'B') ( 10159, 2, '2', 'C')
#  (101591, 2, '2', 'C') (101592, 2, '2', 'C') (101593, 2, '2', 'C')]

print(type(t))#<class 'numpy.memmap'>
actual_index = t[1]["actual_index"]
print(actual_index) #101591
