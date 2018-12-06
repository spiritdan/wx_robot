import img2letter
import letter2img
import combine_img
filename='jiang'
input_img='.\\input_img\\'+filename+'.png'
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
    letter2img.convert(filename,i,j)
    j=j+1
#img合并
combine_img.image_compose(IMAGES_PATH,filename,output_path)
