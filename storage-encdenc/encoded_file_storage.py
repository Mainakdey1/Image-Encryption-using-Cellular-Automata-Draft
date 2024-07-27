import random
import numpy as np


class encoded_file_storage():
    #storage

    def __init__(self,file_path = None) -> None:
        self._file_path=file_path
        
    def encode(self,pretext):
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
            for _ in range(nbit):
                temp_cell=update_cells(cells)
                bit_stream+=[temp_cell[target_bit],]


            return bit_stream

        size=101
        nbit=10000
        target_bit=size//2
        binary_gen=generate_psn(size,nbit, target_bit)
        _binary_representation = ''.join(format(ord(char), '08b') for char in pretext)
        prim_len=len(_binary_representation)
        pseudo_random_number = int("".join(map(str, binary_gen)), 2)

        if prim_len>=len(str(pseudo_random_number)):
            temp=prim_len//len(str(pseudo_random_number))
            rem=prim_len-temp*(len(str(pseudo_random_number)))
            pseudo_random_number=temp*(str(pseudo_random_number))+rem*"0"

        else:
            pseudo_random_number=int(str(pseudo_random_number)[:(len(_binary_representation))])


        _enc_binary_string=""
        for i in range(prim_len):
            _enc_binary_string+=str(int(str(pseudo_random_number)[i])^int(_binary_representation[i]))

        


        with open(self._file_path, "w+") as file:
            file.write(_enc_binary_string)

            file.close()

        











