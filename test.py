#test.py
import os
print('current working directory', os.getcwd())
print('full directory path', os.path.dirname(os.getcwd()))
dirpath = os.path.join('/babi-tasks','babi', 'tasks_1-20_v1-2','en')
filepath = os.path.join(dirpath, 'qa15_basic-deduction_test.txt')
with open(filepath) as f:
  print(f.readlines())
print('success')
