import zlib
from PIL import Image,ImageGrab
def image_resize():
    im=ImageGrab.grab()
    im.save("c:\\tmp\\screenshoot.jpg")
    imBytes=im.tobytes()
    print(len(imBytes))
    compressedBytes=zlib.compress(imBytes)
    print(len(compressedBytes))

    im1=Image.frombytes('RGB',im.size,zlib.decompress(compressedBytes))
    #im1.tobytes()==imBytes
      # 保存新图
    im1.save("c:\\tmp\\screenshoot_resize.jpg")  # 保存新图

image_resize()