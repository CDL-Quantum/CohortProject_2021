import os
import re

root_dataset_path = './dataset/'
dir_pattern = r'n(\d+)_m(\d+)'
for dir_name in os.listdir(root_dataset_path):
    mat = re.match(dir_pattern, dir_name)
    if mat is not None:
        n, m = mat.group(1), mat.group(2)
