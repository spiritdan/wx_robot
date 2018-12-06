import PIL.Image as Image
import os



# 定义图像拼接函数
def image_compose(IMAGES_PATH,filename,output_path,extension):
    #IMAGES_PATH = '.\\tmp\\'  # 图片集地址
    IMAGES_FORMAT = ['.jpg', '.JPG', 'png', 'PNG']  # 图片格式
    #IMAGE_ROW = 20  # 图片间隔，也就是合并成一张图后，一共有几行
    IMAGE_COLUMN = 1  # 图片间隔，也就是合并成一张图后，一共有几列
    IMAGE_SAVE_PATH = output_path+filename+extension  # 图片转换后的地址
    image_names = []
    # 获取图片集地址下的所有图片名称
    for name in os.listdir(IMAGES_PATH):
        # print(name)
        image_names.append(name)
    IMAGE_ROW = len(image_names)

    from_image = Image.open(IMAGES_PATH + image_names[0])
    width = from_image.width
    height = from_image.height
    to_image = Image.new('RGB', (IMAGE_COLUMN * width, IMAGE_ROW * height))  # 创建一个新图
    # 循环遍历，把每张图片按顺序粘贴到对应位置上
    for y in range(1, IMAGE_ROW + 1):
        for x in range(1, IMAGE_COLUMN + 1):
            from_image = Image.open(IMAGES_PATH + image_names[IMAGE_COLUMN * (y - 1) + x - 1])
            width=from_image.width
            height=from_image.height
            to_image.paste(from_image, ((x - 1) * width, (y - 1) * height))
    print("保存字符画中")
    to_image.save(IMAGE_SAVE_PATH)  # 保存新图
    return IMAGE_SAVE_PATH

