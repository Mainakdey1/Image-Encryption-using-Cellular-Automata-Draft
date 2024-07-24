
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
