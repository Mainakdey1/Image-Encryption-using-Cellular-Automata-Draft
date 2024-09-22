import argparse
import base64
import sys
import PySimpleGUI as sg
import os
import sys

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


image_path = resource_path('newimg.png')

class file_read:
    def __init__(self, _coded_b64) -> None:
        self._coded_b64=_coded_b64
        decoded_byte= base64.b64decode(self._coded_b64)
        _file_data=decoded_byte.decode('utf-8')


        primary_len=len(_file_data)

        self._data=[]

        count=0


        for i in range(primary_len):
            if _file_data[i] == '|':
                if count==0:
                    
                    self._data+=[_file_data[count:i],]
                    count=i
                else:
                    self._data+=[_file_data[count+1:i],]
                    count=i


            elif _file_data[i] == '~':
                self._data+=[_file_data[count+1:i],]
                self._key=_file_data[i+1:]

    
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
                


                flr_pre=file_read(content)
                data=flr_pre.data()
                key=flr_pre.key()
 
                modified_primary_len=len(data)
                new_data=''
                
                try:
                   

                    sg.theme('LightPurple') 
                    title_bar = [
                                [sg.Text('PXEopen', background_color='#2e756a', text_color='white', pad=(10, 0), size=(30, 1)),
                                ]
                            ]
                    layout = [[sg.Column(title_bar, background_color='#2e756a')], [sg.Image(filename=image_path )], [sg.Input(key='-IN-'), sg.FileBrowse()],
                    [sg.Button('Go'), sg.Button('Exit')]]

                    #choose your input file here
                    window = sg.Window('select your encryption key', layout, no_titlebar=True)
                    event,values = window.read()
                    file_path = values['-IN-']
                    file_extension = os.path.splitext(file_path)
                    if file_extension[1] == '.pxe' :
                        try:
                            with open(file_path, 'r') as file:
                                ac_key_b64 = file.read()
                                window.close()
                                flr_post=file_read(ac_key_b64)
                                ac_key_key=flr_post.key()
                                ac_key_data=flr_post.data()
                                ac_key=''
                                for i in range(len(ac_key_data)):
                                    ac_key+=str(int(ac_key_data[i])^int(ac_key_key[i]))

                                
                                for i in range(modified_primary_len):
                                    new_data+=chr(int(data[i])^int(key[i])^int(ac_key[i]))
                                                
                                print(new_data)

                                sys.exit()
                                
                        except Exception as e:
                            print(f"An error occurred: {e}")
                            
                    else:
                        print("Invalid file type for this application")
                        raise Exception("Invalid file type. Please connect both of your brain cells together.")


                except:
                    print()


                    




                



    except FileNotFoundError:
        print(f"Error: The file '{args.file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")



    except:
        print()
        

if __name__ == "__main__":
    main()
