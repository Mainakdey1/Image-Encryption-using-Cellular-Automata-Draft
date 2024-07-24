
import imageio.v3
import time
import sys








start_time=time.time()

sys.set_int_max_str_digits(10000000)
def img_inp_method(path):
    imgcolor=imageio.v3.imread(path) # please add "r" in front of the path in case of input errors.
    rows, cols, rgb=imgcolor.shape

    R=[]
    G=[]
    B=[]
    for i in range(rows):
        for j in range(cols):
            B.append(imgcolor[i,j,0])
            G.append(imgcolor[i,j,1])
            R.append(imgcolor[i,j,2])


    return R+G+B

def text_inp_method(raw_text):
    res=[]
    lt=len(raw_text)
    for i in range(lt):
        res+=[ord(raw_text[i]),]


    return res

print("1. Image Encryption\n2. Plain-Text Encryption")
stat_inp=str(input())

if stat_inp=="1":
 
    cnv_list=img_inp_method(str(input("Please enter the path of your image")))

elif stat_inp=="2":

    cnv_list=text_inp_method(str(input("Please enter your text")))


print(cnv_list)

#use imgcolor for further analysis