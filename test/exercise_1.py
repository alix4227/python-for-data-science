import json
import re
from abc import ABC
import sys
class Document(ABC):
    def __init__(self):
        self.id_elements = {
           "Firstname": "", "Name": "", "Date_of_birth": "", "Document_number": "", 
            "Expiration_date": "", "Nationality": "", "Type_of_document": "", 
            "Sex": "", "Place_of_birth": "", "Height": ""
        }
    
class Qrcode(Document):
    def __init__(self):
        super().__init__()
        self.qrcode_info =""

    def get_qrcode_info(self, document):
        with open(document, "r") as file:
            self.qrcode_info = json.load(file)
            self.qrcode_info = self.qrcode_info['text'].split(';')

    def fill_id_elements(self):
        for key, value in zip(self.id_elements.keys(), self.qrcode_info):
            if key == 'Firstname':
                value = value.lstrip('E')
            if key in ('Date_of_birth', 'Expiration_date'):
                value = value.replace('/', ' ')
            if key == 'Height':
                value = value.strip('S')
            self.id_elements[key] = value

class CNI(Document):
    def __init__(self):
        super().__init__()
        self.cni_info =""

    def get_cni_info(self, document):
        with open(document, "r") as file:
            self.cni_info = json.load(file)
            self.cni_info = self.cni_info['text']['page_1'] + self.cni_info['text']['page_2']
    def fill_id_elements(self):
        name = re.search(r"Surname\s+(\w+)", self.cni_info)
        self.id_elements['Name'] = name.group(1) if name else ""

        firstname = re.search(r"Given names\s+(.+?) SEXE", self.cni_info)
        self.id_elements['Firstname'] = firstname.group(1) if firstname else ""
        
        document_number = re.search(r"Document No.\s+(\w+)", self.cni_info)
        self.id_elements['Document_number'] = document_number.group(1) if document_number else ""
        
        date_of_birth = re.search(r"Date of birth (\d{2} \d{2} \d{4})", self.cni_info)
        self.id_elements['Date_of_birth'] = date_of_birth.group(1) if date_of_birth else ""
        
        expiration_date = re.search(r"Expiry date (\d{2} \d{2} \d{4})", self.cni_info)
        self.id_elements['Expiration_date'] = expiration_date.group(1) if expiration_date else ""

        nationality = re.search(r"Nationality\s+(\w+)", self.cni_info)
        self.id_elements['Nationality'] = nationality.group(1) if nationality else ""
        
        if "CARTE NATIONALE D'IDENTITE" in self.cni_info:
            self.id_elements['Type_of_document'] = "CNI"
        
        sex = re.search(r"Sex\s+(\w+)", self.cni_info)
        self.id_elements['Sex'] = sex.group(1) if sex else ""
        
        place_of_birth = re.search(r"Place of birth\s+(\w+)", self.cni_info)
        self.id_elements['Place_of_birth'] = place_of_birth.group(1) if place_of_birth else ""
        
        height = re.search(r"Height\s+(.+?)m", self.cni_info)
        self.id_elements['Height'] = height.group(1).strip() if height else ""
    
def test(Cni, qrcode):
    with open('report.txt', 'w') as file:
        for key in Cni.id_elements.keys():
            if Cni.id_elements[key].lower() == qrcode.id_elements[key].lower():
                file.write(f"{key}: OK\n")
            else:
                file.write(f"{key}: No matching {key}\n")
                
def main(args):
    try:
        qrcode = Qrcode()
        qrcode.get_qrcode_info(args[1])
        qrcode.fill_id_elements()
        print(qrcode.id_elements)

        Cni = CNI()
        Cni.get_cni_info(args[2])
        Cni.fill_id_elements()
        print(Cni.id_elements)
        test(Cni, qrcode)
    except Exception:
        print(Exception)
    
if __name__ == "__main__":
    main(sys.argv)
