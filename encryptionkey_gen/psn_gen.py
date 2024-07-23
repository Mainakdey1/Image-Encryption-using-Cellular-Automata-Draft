def rule30(left, center, right):
    return left^(center | right)

def initialize_ca(size,tbit):
    cells=np.zeros(size, dtype=int)
    cells[tbit]=1
    return cells

def update_cells(cells):
    new_cells = np.zeros_like(cells)
    for i in range(1, len(cells) - 1):
        new_cells[i] = rule30(cells[i - 1], cells[i], cells[i + 1])
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
bloated_psn=3*(str(pseudo_random_number))
bloated_psn=bloated_psn + 75030*("0")


