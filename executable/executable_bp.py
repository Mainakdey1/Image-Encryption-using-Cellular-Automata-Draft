import argparse
import base64
import time
import sys
import PySimpleGUI as sg

class file_read:
    def __init__(self, _file_data) -> None:
        self._file_data=_file_data
        primary_len=len(self._file_data)

        self._data=[]

        count=0


        for i in range(primary_len):
            if self._file_data[i] == '|':
                if count==0:
                    
                    self._data+=[self._file_data[count:i],]
                    count=i
                else:
                    self._data+=[self._file_data[count+1:i],]
                    count=i


            elif self._file_data[i] == '~':
                self._data+=[self._file_data[count+1:i],]
                self._key=self._file_data[i+1:]

    
        pass

    def data(self):
        return self._data
    
    def key(self):
        return self._key


def main():


    

    try:
        parser = argparse.ArgumentParser(description=".")
        parser.add_argument("file", help="Path to the file you want to read")
        args = parser.parse_args()
        if args.file.endswith('.pxe'):
                
            with open(args.file, 'r') as f:
                content = f.read()
                decoded_byte= base64.b64decode(content)
                dec_text=decoded_byte.decode('utf-8')


                flr=file_read(dec_text)
                data=flr.data()
                key=flr.key()
                print(data)
                print(key)
                modified_primary_len=len(data)
                new_data=''
                
                try:
                   

                    sg.theme('LightPurple') 
                    title_bar = [
                                [sg.Text('PXEopen', background_color='#2e756a', text_color='white', pad=(10, 0), size=(30, 1)),
                                ]
                            ]
                    layout = [[sg.Column(title_bar, background_color='#2e756a')], [sg.Image(filename='newimg.png' )], [sg.Input(key='-IN-'), sg.FileBrowse()],
                    [sg.Button('Go'), sg.Button('Exit')]]

                    #choose your input file here
                    window = sg.Window('select your encryption key', layout, no_titlebar=True)
                    event,values = window.read()
                    file_path = values['-IN-']
                    with open(file_path, 'r') as file:
                        ac_key = file.read()
                    window.close()

                except:
                    print()

                for i in range(modified_primary_len):
                    new_data+=chr(int(data[i])^int(key[i])^int(ac_key[i]))

                    



                print(new_data)

                sys.exit()
                

                



    except FileNotFoundError:
        print(f"Error: The file '{args.file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")



    except:
        print()
        

if __name__ == "__main__":
    main()
