"""打印指定目录及子目录下所有文件的绝对路径"""
import os

root_dir = '/Users/chenxilin/Code/Study/python_basic'
for parent, dir_names, file_names in os.walk(root_dir):
    for file_name in file_names:
        print(parent + '/' + file_name)
