import argparse
import base64
import time
import sys



def main():

    parser = argparse.ArgumentParser(description=".")
    parser.add_argument("file", help="Path to the file you want to read")
    args = parser.parse_args()
    

    try:
        if args.file.endswith('.pxe'):
                
            with open(args.file, 'r') as f:
                content = f.read()
                decoded_byte= base64.b64decode(content)
                dec_text=decoded_byte.decode('utf-8')
                primary_len=len(dec_text)

                data=[]
                key=''
                ac_key='30393769176'
                count=0
                new_data=''

                for i in range(primary_len):
                    if dec_text[i] == '|':
                        if count==0:
                            
                            data+=[dec_text[count:i],]
                            count=i
                        else:
                            data+=[dec_text[count+1:i],]
                            count=i


                    elif dec_text[i] == '~':
                        data+=[dec_text[count+1:i],]
                        key=dec_text[i+1:]

                modified_primary_len=len(data)
                for i in range(modified_primary_len):
                    new_data+=chr(int(data[i])^int(key[i])^int(ac_key[i]))

                    



                print(new_data)
                time.sleep(10)
                sys.exit()
                

                



    except FileNotFoundError:
        print(f"Error: The file '{args.file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
