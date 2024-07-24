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