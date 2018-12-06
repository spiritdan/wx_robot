import os
IMAGES_PATH='.\\tmp\\181206-143020'
for name in os.listdir(IMAGES_PATH):
    print(name)

#数据格式化，保留4位，用0补足显示0019
print('{:0>4}'.format('19'))