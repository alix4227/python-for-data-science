from classes import CNI,Qrcode
import sys
import json

def test(Cni, qrcode):
    with open('report.txt', 'w') as file:
        for key in Cni.id_elements.keys():
            if Cni.id_elements[key].lower() == qrcode.id_elements[key].lower():
                file.write(f"{key}: OK\n")
            else:
                file.write(f"{key}: No matching {key}\n")
                
def main(args):
    if len(args) != 3:
        print('Wrong number of arguments')
        return (1)
    if args[1] != 'qrcode.json' or args[2] != 'ocr.json':
        print('Wrong arguments')
        return(1)
    try:
        qrcode = Qrcode()
        qrcode.get_qrcode_info(args[1])
        qrcode.fill_id_elements()
        print(qrcode.id_elements)

        Cni = CNI()
        Cni.get_cni_info(args[2])
        Cni.fill_id_elements()

        test(Cni, qrcode)
        print(Cni.id_elements)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Reading error")
    except Exception:
        print("ERROR")
    
if __name__ == "__main__":
    main(sys.argv)