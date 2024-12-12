import os
import torch


print(os.system("echo %CUDA_VISIBLE_DEVICES%"))
print('torch.cuda.device_count:',torch.cuda.device_count())
print('torch.cuda.current_device:',torch.cuda.current_device())
print(torch.device("cuda"))

print('=== os.environ ===')
os.environ["CUDA_VISIBLE_DEVICES"] = "0,1"
print(os.system("echo %CUDA_VISIBLE_DEVICES%"))
print('torch.cuda.device_count:',torch.cuda.device_count())
print('torch.cuda.current_device:',torch.cuda.current_device())
print(torch.device("cuda"))
