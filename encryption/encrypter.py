def encrypter(enc_len,enc_text, psn):
    enc_out=[]
    for i in range(enc_len):
        enc_out+=[int(enc_text[i]) ^ int(psn[i])]


    return enc_out


