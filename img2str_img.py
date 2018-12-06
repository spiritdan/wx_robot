import img2letter
import letter2img
import combine_img

def convert_img(filename,input_img_path,extension):
    input_img = input_img_path + filename + extension
    output_txt='.\\txt\\'+filename+'.txt'
    tmp_path='.\\tmp\\'
    output_path='.\\output_img\\'
    IMAGES_PATH=tmp_path+filename+'\\'
    #转txt
    img2letter.save_txt(input_img,output_txt)

    #txt切片转img
    file=open('.\\txt\\'+filename+'.txt')
    j=0
    for i in file.readlines():
        if i=='\n':
            continue
        letter2img.convert(filename,i,j,tmp_path)
        j=j+1
    print("切片完成")
    #img合并
    img =combine_img.image_compose(IMAGES_PATH,filename,output_path,extension)
   # print(img)
    return img

#test case

image_name = '181206-143442'
extension = '.png'
input_img_path = '.\\input_img\\'

img =convert_img(image_name, input_img_path, extension)
print(img)
