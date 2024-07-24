
import imageio.v3
import time
import sys



import numpy as np






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












#use imgcolor for further analysis
primary_len=10000

sys.set_int_max_str_digits(10000000)

def rule_combined(left, center, right):
    return (left^(center | right)) | (left^right)

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
iterations=primary_len
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




def main():
    print("1. Image Encryption\n2. Plain-Text Encryption")
    stat_inp=str(input())

    if stat_inp=="1":
    
        path=img_inp_method(str(input("Please enter the path of your image: \n")))
        cnv_list=img_inp_method(path)
        image_encrpt_decrypt(pseudo_random_number,cnv_list)
        

    elif stat_inp=="2":

        cnv_list=text_inp_method(str(input("Please enter your text: \n")))
        text_encrypt_decrypt(pseudo_random_number,cnv_list)


main()

