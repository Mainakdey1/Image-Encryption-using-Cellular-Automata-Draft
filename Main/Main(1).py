import subprocess
import pkg_resources



required={'imageio','numpy','opencv-python','pysimplegui'}
installed={pkg.key for pkg in pkg_resources.working_set}
missing=required-installed
if missing:
    subprocess.check_call([sys.executable,"-m","pip","install",*missing])



import imageio.v3
import time
import sys
import os
import numpy as np
import cv2
import random
import encoded_file_storage
import PySimpleGUI as sg
from os.path import expanduser


str_to_int_limits=100000
nca_limit=10000
size=101
tbit=size//2
stat_inp=0
dir_pathV= expanduser("~")+"\\"
sg.theme('DarkTeal10')







start_time=time.time()
sys.set_int_max_str_digits(str_to_int_limits)








#Logger class for logging events. Events have 3 severity:info, warning and critical
#info: call with this to record events that are part of the normal functioning of the program
#warning: call with this severity to record events that are crucial but will not break the funtioning of the program.
#critical: call with this severity to record events that are critical to the functioning of the program.

class logger:


    def __init__(self,_log_file,_global_severity=0 ,_dir_path=str,_logobj= str):
        self._logobj=_logobj
        self._global_severity=_global_severity
        self._log_file=_log_file
        self._dir_path=_dir_path
        
    

    def info(self,_function_name,_message):

    
        log_file=open(self._dir_path+self._log_file,"a+")
        log_file.write("\n"+time.ctime()+" at "+str(time.perf_counter_ns())+"    "+_function_name+"   called (local_severity=INFO)with message:  "+_message)
        log_file.close()


    def warning(self,_function_name,_message):

        log_file=open(self._dir_path+self._log_file,"a+")
        log_file.write("\n"+time.ctime()+" at "+str(time.perf_counter_ns())+"    "+_function_name+"   called (local_severity=WARNING)with message:  "+_message)
        log_file.close()

    def critical(self,_function_name,_message):

        log_file=open(self._dir_path+self._log_file,"a+")
        log_file.write("\n"+time.ctime()+" at "+str(time.perf_counter_ns())+"    "+_function_name+"   called (local_severity=CRITICAL)with message:  "+_message)
        log_file.close()
 
#call this method to produce the log file
    def producelog(self):
        log_file=open(self._dir_path+self._log_file,"r")
        msg=log_file.readlines()
        log_file.close()
        return msg
    
#call this method to find the privilege level of the current logging instance.
    def privilege(self):
        if self._global_severity==0:
            print("This logger is at the highest privilege level")
        else:
            return self._global_severity
        
#call this method to identify the logging instance, if there are several instances initiated.
    def identify(self):
        print(self._logobj)




    




logins=logger("logfile.txt",0,dir_pathV,"globallogger")
logins.info('MAIN', 'successful')







def img_inp_method(path):
    try:
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


        logins.info("IMAGE INPUT METHOD CALLED","CALLED")
        return R+G+B
        
    
    except:
        logins.critical('IMAGE INPUT METHOD ',"FUNCTION INITIATION FAILED")

def text_inp_method(raw_text):
    try:
        res=[]
        lt=len(raw_text)
        for i in range(lt):
            res+=[ord(raw_text[i]),]

        logins.info('TEXT INPUT METHOD ','CALLED')
        return res
    except:
        logins.critical('TEXT INPUT METHOD ','FUNCTION INITIATION FAILED')


def signo_inp_method(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    height,width=image.shape
    pixel_values = image.flatten()

    return height, width, pixel_values


def sbox(hieght,width):
    res_arr=[]
    for i in range(hieght*width):
        res_arr+=[random.randint(0,255),]

    return res_arr

def rule_30(left, center, right):
    return (left^(center | right)) 

def rule90(left,center, right):
    return (left | right)

def initialize_ca(size,tbit):
    cells=np.zeros(size, dtype=int)
    cells[tbit]=1
    return cells

def update_cells(cells):
    rule_randomizer_int=0



    new_cells = np.zeros_like(cells)

    for i in range(1, len(cells) - 1):

        rule_randomizer_int=random.randint(0,1)
        if rule_randomizer_int==0:

            new_cells[i] = rule_30(cells[i - 1], cells[i], cells[i + 1])
        elif rule_randomizer_int==1:
            new_cells[i] = rule90(cells[i - 1], cells[i], cells[i + 1])

        


    
    return new_cells

            
def generate_psn(size,nbit, target_bit):
    cells=initialize_ca(size,target_bit)
    bit_stream=[]
    probar_count=0
    for _ in range(nbit):
        temp_cell=update_cells(cells)
        bit_stream+=[temp_cell[target_bit],]
        probar_count+=(100/nca_limit)
        window['-PROGRESS-'].update(probar_count)

    window.close()
    return bit_stream





        
    



title_bar = [
    [sg.Text('Encrypter', background_color='#2e756a', text_color='white', pad=(10, 0), size=(30, 1)),
     ]
]






layout = [[sg.Column(title_bar, background_color='#2e756a')], [sg.Image(filename='dark.png' )], 
    [sg.Text('Cellular Automata Maker')], 
    [sg.ProgressBar(max_value=100, orientation='h', size=(20, 20), key='-PROGRESS-')],
    [sg.Button('Start'), sg.Button('Exit')] , [sg.Text('Enter the number of iterations: '), sg.InputText(key='-ITER-')] ]


window = sg.Window('Encrypter', layout, no_titlebar=True)


while True:
    event, values = window.read()


    if event == sg.WIN_CLOSED:

        break
    elif event == 'Exit':
        sys.exit()



    elif event == 'Start':
        try:
            nca_limit=int(values['-ITER-'])
        except: 
            nca_limit=10000
        
        

       
        size=101
        tbit=size//2
 
        ngen=generate_psn(size,nca_limit,tbit)
        pseudo_random_number = int("".join(map(str, ngen)), 2)






#################################




def enc_key_packer(key_arr):
    packed_key=""
    for i in range(len(key_arr)):
        packed_key+=str(key_arr[i])+"|"


    return packed_key


#################################






def image_encrpt_decrypt(pseudo_random_number,unenc_key_arr):

    #Important information: The pseudo random number must be in integer format and the unenc_key_arr argument must recieve only list objects.

    if len(unenc_key_arr)>=len(str(pseudo_random_number)):
        temp=len(unenc_key_arr)//len(str(pseudo_random_number))
        rem=pseudo_random_number-int(temp*(str(pseudo_random_number)))
        pseudo_random_number=temp*(str(pseudo_random_number))+rem

    else:
        pseudo_random_number=int(str(pseudo_random_number)[:len(unenc_key_arr)])

        
    def encrypter(enc_len,enc_text, psn):
        enc_out=[]
        for i in range(enc_len):
            enc_out+=[int(enc_text[i]) ^ int(psn[i])]


        return enc_out
    
    print("The raw rgb pixel values are: ",unenc_key_arr)

    print("The encrypted rgb pixel values are : ",encrypter(len(unenc_key_arr),unenc_key_arr,pseudo_random_number))


    

def text_encrypt_decrypt(pseudo_random_number,unenc_key_arr):


    #Important information: The pseudo random number must be in integer format and the unenc_key_arr argument must recieve only list objects.





    if len(unenc_key_arr)>=len(str(pseudo_random_number)):
        temp=len(unenc_key_arr)//len(str(pseudo_random_number))
        rem=pseudo_random_number-int(temp*(str(pseudo_random_number)))
        pseudo_random_number=temp*(str(pseudo_random_number))+rem
    else:
        pseudo_random_number=int(str(pseudo_random_number)[:len(unenc_key_arr)]
                                )
        

    enc_list=[]
    for i in range(len(unenc_key_arr)):
        enc_list+=[unenc_key_arr[i]^int(str(pseudo_random_number)[i]),]

    fin=""
    for i in enc_list:
        fin+=chr(i)

    print("\nThe encrypted data is thus: ",fin)

    un_encrypted_ls=[]
    for i in range(len(unenc_key_arr)):
        un_encrypted_ls+=[enc_list[i]^int(str(pseudo_random_number)[i])]

    res=""

    for i in un_encrypted_ls:
        res+=chr(i)


    print("\nThe un-encrypted data is thus: ",res)





def signature_encrypt_decrypt(pseudo_random_number, unenc_key_arr,height, width):
    prim_len=len(unenc_key_arr)
    sbox_arr=sbox(height,width)
    if prim_len>=len(str(pseudo_random_number)):
        temp=prim_len//len(str(pseudo_random_number))
        rem=prim_len-temp*(len(str(pseudo_random_number)))
        pseudo_random_number=temp*(str(pseudo_random_number))+rem*"0"

    else:
        pseudo_random_number=int(str(pseudo_random_number)[:len(unenc_key_arr)])
        

    
    enc_key_arr=[]
    for i in range(prim_len):
        enc_key_arr+=[unenc_key_arr[i]^int(str(pseudo_random_number)[i]),]


    enc_dict_pck={}
    for i in range(prim_len):
        enc_dict_pck[sbox_arr[i]]=enc_key_arr[i]

    

    

    enc_np_arr=np.array(sbox_arr)

    enc_image=enc_np_arr.reshape((height,width))
    enc_image=enc_image.astype(np.uint8)
    





    unenc_arr=[]
    for i in range(prim_len):
        unenc_arr+=[enc_dict_pck[sbox_arr[i]],]
    
    for i in range(len(unenc_key_arr)):
        unenc_arr[i]=[enc_key_arr[i]^int(str(pseudo_random_number)[i]),]
    


    unenc_np_arr=np.array(unenc_arr)
    unenc_image=unenc_np_arr.reshape((height,width))
    unenc_image=unenc_image.astype(np.uint8)
    cv2.imshow("Encrypted signature",enc_image)
    cv2.imshow("Un- Encrypted signature", unenc_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    sys.exit()
    postext=enc_key_packer(sbox_arr)
    



















def main():
    sg.theme("DarkTeal10")


    layout = [
    [sg.Text('Please select the type of data you want to encrypt :')],
    [sg.Radio('Text Encryption', 'RADIO1', key='te', size=(40)), sg.Radio('Image encryption', 'RADIO1', key='ie', size=40), sg.Radio('Signature encryption', 'RADIO1', key='sige' , size=40) ],
    
    [sg.Button('Submit'), sg.Button('Cancel') ]
    ]

    # Create the window
    window = sg.Window( "new window", layout, no_titlebar=True)
    event , vals= window.read()



    for k in vals:
        if  k=='te' and vals[k]==True :
            stat_inp=1
   
        elif k=='ie' and vals[k]==True :
            stat_inp=2
        elif k=='sige' and vals[k]==True :
            stat_inp=3

    if stat_inp==2:
    
        path=img_inp_method(str(input("Please enter the path of your image: \n")))
        unenc_key_arr=img_inp_method(path)
        image_encrpt_decrypt(pseudo_random_number,unenc_key_arr)
        

    elif stat_inp==1:
        layout = [[sg.Input(key='-IN-'), sg.FileBrowse()],
          [sg.Button('Go'), sg.Button('Exit')]]


        window = sg.Window('File Browser', layout)
        event,values = window.read()
        file_path = values['-IN-']
        with open(file_path, 'r') as file:
            content = file.read()
        window.close()
        

        unenc_key_arr=text_inp_method(str(content))
        text_encrypt_decrypt(pseudo_random_number,unenc_key_arr)
    elif stat_inp==3:
        layout = [[sg.Input(key='-IN-'), sg.FileBrowse()],
          [sg.Button('Go'), sg.Button('Exit')]]


        window = sg.Window('File Browser', layout)
        event,values = window.read()
        file_path = values['-IN-']
        window.close()
        
        title_bar = [
            [sg.Text('Image Preview', background_color='#2e756a', text_color='white', pad=(10, 0), size=(30, 1)),
            ]
]

        layout= [[sg.Column(title_bar, background_color='#2e756a')],
                 [sg.Image(file_path)],
                 [sg.Text('Do you wish to use this image?')],
                 [sg.Yes() , sg.No()]]
        window= sg.Window('Preview Image',layout, no_titlebar=True)
        event, values= window.read()
 
    

        if event== 'Yes':

            height,width, unenc_key_arr=signo_inp_method(file_path)
            signature_encrypt_decrypt(pseudo_random_number,unenc_key_arr,height,width)
        else:
            sys.exit()


    sys.exit()
try:
    if __name__=="__main__":
        main()
except:
    sys.exit()


