from classes import CNI,Qrcode,MRZ
import sys
import json

def test(Cni, mrz):
    with open('report.txt', 'w') as file:
        for key in mrz.id_elements.keys():
            if Cni.id_elements[key].lower() == mrz.id_elements[key].lower():
                file.write(f"{key}: OK\n")
            else:
                file.write(f"{key}: No matching {key}\n")
                
def main(args):
    if len(args) != 2:
        print('Wrong number of arguments')
        return (1)
    if args[1] != 'ocr.json':
        print('Wrong arguments')
        return(1)
    try:
        mrz = MRZ()
        mrz.get_mrz_info(args[1])
        mrz.fill_id_elements()
        print(mrz.id_elements)

        Cni = CNI()
        Cni.get_cni_info(args[1])
        Cni.fill_id_elements()
        print(Cni.id_elements)

        test(Cni, mrz)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Reading error")
    except Exception:
        print("ERROR")
    
if __name__ == "__main__":
    main(sys.argv)