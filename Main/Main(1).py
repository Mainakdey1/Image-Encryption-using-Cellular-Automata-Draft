
import imageio.v3
import time
import sys
import numpy as np
import cv2
import random

str_to_int_limits=100000
nca_limit=10000

start_time=time.time()

sys.set_int_max_str_digits(str_to_int_limits)
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


def signo_inp_method(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    pixel_values = image.flatten()

    return pixel_values









#use imgcolor for further analysis


sys.set_int_max_str_digits(10000000)

def sbox(hieght,width):
    res_arr=[]
    for i in range(hieght*width):
        res_arr+=[random.randint(0,255),]

    return res_arr

def rule_combined(left, center, right):
    return (left^(center | right)) 

def initialize_ca(size,tbit):
    cells=np.zeros(size, dtype=int)
    cells[tbit]=1
    return cells

def update_cells(cells):
    new_cells = np.zeros_like(cells)
    for i in range(1, len(cells) - 1):
        new_cells[i] = rule_combined(cells[i - 1], cells[i], cells[i + 1])
    return new_cells

def generate_psn(size,nbit, target_bit):
    cells=initialize_ca(size,target_bit)
    bit_stream=[]
    for _ in range(nbit):
        temp_cell=update_cells(cells)
        bit_stream+=[temp_cell[target_bit],]


    return bit_stream


size=101
iterations=nca_limit
tbit=size//2

ngen=generate_psn(size,iterations,tbit)
pseudo_random_number = int("".join(map(str, ngen)), 2)






def image_encrpt_decrypt(pseudo_random_number,cnv_list):

    #Important information: The pseudo random number must be in integer format and the cnv_list argument must recieve only list objects.

    if len(cnv_list)>=len(str(pseudo_random_number)):
        temp=len(cnv_list)//len(str(pseudo_random_number))
        rem=pseudo_random_number-int(temp*(str(pseudo_random_number)))
        pseudo_random_number=temp*(str(pseudo_random_number))+rem

    else:
        pseudo_random_number=int(str(pseudo_random_number)[:len(cnv_list)])

        
    def encrypter(enc_len,enc_text, psn):
        enc_out=[]
        for i in range(enc_len):
            enc_out+=[int(enc_text[i]) ^ int(psn[i])]


        return enc_out
    
    print("The raw rgb pixel values are: ",cnv_list)

    print("The encrypted rgb pixel values are : ",encrypter(len(cnv_list),cnv_list,pseudo_random_number))


    

def text_encrypt_decrypt(pseudo_random_number,cnv_list):


    #Important information: The pseudo random number must be in integer format and the cnv_list argument must recieve only list objects.





    if len(cnv_list)>=len(str(pseudo_random_number)):
        temp=len(cnv_list)//len(str(pseudo_random_number))
        rem=pseudo_random_number-int(temp*(str(pseudo_random_number)))
        pseudo_random_number=temp*(str(pseudo_random_number))+rem
    else:
        pseudo_random_number=int(str(pseudo_random_number)[:len(cnv_list)]
                                )
        

    enc_list=[]
    for i in range(len(cnv_list)):
        enc_list+=[cnv_list[i]^int(str(pseudo_random_number)[i]),]

    fin=""
    for i in enc_list:
        fin+=chr(i)

    print("\nThe encrypted data is thus: ",fin)

    un_encrypted_ls=[]
    for i in range(len(cnv_list)):
        un_encrypted_ls+=[enc_list[i]^int(str(pseudo_random_number)[i])]

    res=""

    for i in un_encrypted_ls:
        res+=chr(i)


    print("\nThe un-encrypted data is thus: ",res)


def signature_encrypt_decrypt(pseudo_random_number, cnv_list):
    height = 360
    width = 480
    sbox_arr=sbox(height,width)
    if len(cnv_list)>=len(str(pseudo_random_number)):
        temp=len(cnv_list)//len(str(pseudo_random_number))
        rem=len(cnv_list)-temp*(len(str(pseudo_random_number)))
        pseudo_random_number=temp*(str(pseudo_random_number))+rem*"0"

    else:
        pseudo_random_number=int(str(pseudo_random_number)[:len(cnv_list)])
        
    print(len(str(pseudo_random_number)))
    print(len(cnv_list))
    cn=[]
    def invert(cnv_list):
        for i in cnv_list:
            
            i=125-i
            cn+=[i,]
    enc_list=[]
    for i in range(len(cnv_list)):
        enc_list+=[cnv_list[i]^int(str(pseudo_random_number)[i])^sbox_arr[i],]
    
    print("Encrypted signature is: ")



    

    enc_np_arr=np.array(enc_list)

    enc_image=enc_np_arr.reshape((height,width))
    enc_image=enc_image.astype(np.uint8)
    cv2.imshow("Encrypted signature",enc_image)



    print("Encrypted reconstructed image: ")
    unenc_arr=[]
    for i in range(len(cnv_list)):
        unenc_arr+=[enc_list[i]^int(str(pseudo_random_number)[i])^sbox_arr[i],]
    

    print("Un-Encrypted reconstructed image is: ")
    unenc_np_arr=np.array(unenc_arr)
    unenc_image=unenc_np_arr.reshape((height,width))
    unenc_image=unenc_image.astype(np.uint8)
    cv2.imshow("Un- Encrypted signature", unenc_image)


    cv2.waitKey(0)
    cv2.destroyAllWindows()






def main():
    print("1. Image Encryption\n2. Plain-Text Encryption\n3. Signature Encryption")
    stat_inp=str(input())

    if stat_inp=="1":
    
        path=img_inp_method(str(input("Please enter the path of your image: \n")))
        cnv_list=img_inp_method(path)
        image_encrpt_decrypt(pseudo_random_number,cnv_list)
        

    elif stat_inp=="2":

        cnv_list=text_inp_method(str(input("Please enter your text: \n")))
        text_encrypt_decrypt(pseudo_random_number,cnv_list)
    elif stat_inp=="3":
        cnv_list=signo_inp_method(r"C:\Users\chestor\Desktop\sample.webp")
        signature_encrypt_decrypt(pseudo_random_number,cnv_list)

main()

