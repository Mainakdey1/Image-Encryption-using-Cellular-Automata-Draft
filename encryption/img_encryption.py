
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

