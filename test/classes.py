import json
import re
from abc import ABC


class Document(ABC):
    def __init__(self):
        self.id_elements = {
           "Firstname": "", "Name": "", "Date_of_birth": "", "Document_number": "", 
            "Expiration_date": "", "Nationality": "", "Type_of_document": "", 
            "Sex": "", "Place_of_birth": "", "Height": "", "Date_of_issue": ""
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
                value = value.lstrip('E').replace('-', ' ')
            if key in ('Date_of_birth', 'Expiration_date'):
                value = value.replace('/', ' ')
            if key == 'Height':
                value = value.strip('S')
            self.id_elements[key] = value

class MRZ(Document):
    def __init__(self):
        super().__init__()
        self.mrz_info =""
        self.id_elements = {
           "Firstname": "", "Name": "", "Date_of_birth": "", "Document_number": "", 
            "Expiration_date": "", "Nationality": "", "Type_of_document": "", 
            "Sex": ""
        }

    def get_mrz_info(self, document):
        with open(document, "r") as file:
            self.mrz_info = json.load(file)
            self.mrz_info = self.mrz_info['text']['page_2']
            self.mrz_info = re.search(r'FRANCAISE\s+(.+)', self.mrz_info).group(1)
            self.mrz_info = [item.lstrip() for item in self.mrz_info.split('<') if item.strip()]

    def parse_name_and_firstnames(self, names):
        if names:
            self.id_elements['Name'] = re.sub(r'[^A-Z]', '', names[0]) 
            self.id_elements['Firstname'] = ' '.join(names[1:]) if len(names) > 1 else ""
        else:
            self.id_elements['Name'] = ""
            self.id_elements['Firstname'] = ""

    def parse_document_type_and_number(self, string):
        document_number = re.search(r'IDFRA(.+)', string)
        self.id_elements['Document_number'] = document_number.group(1)[:-1] if document_number else ""
        
        if string.find('IDFRA') != 1:
            self.id_elements['Type_of_document'] = 'CNI'

    def parse_dates_and_sex(self, string):
        date_of_birth = re.search(r"(\d{2}\d{2}\d{2})", string) 
        self.id_elements['Date_of_birth'] = date_of_birth.group(1) if date_of_birth else ""
        self.id_elements['Date_of_birth'] = f"{self.id_elements['Date_of_birth'][4:6]} {self.id_elements['Date_of_birth'][2:4]} 19{self.id_elements['Date_of_birth'][0:2]}"
        
        if (string[7] == 'F'):
            self.id_elements['Sex'] = 'F'
        elif (string[7] == 'M'):
            self.id_elements['Sex'] = 'M'
        
        expiration_date = re.search(r"(\d{2}\d{2}\d{2})", string[7:])
        self.id_elements['Expiration_date'] = expiration_date.group(1) if expiration_date else ""
        self.id_elements['Expiration_date'] = f"{self.id_elements['Expiration_date'][4:6]} {self.id_elements['Expiration_date'][2:4]} 20{self.id_elements['Expiration_date'][0:2]}"
        if (string.find('FRA')) != 1:
            self.id_elements['Nationality'] = 'FRA'
    
    def fill_id_elements(self):
        mrz_parts = {
           "Document_type_and_number": self.mrz_info[0], 
           "Dates_and_sex": self.mrz_info[1],
           "Names": self.mrz_info[2:]
        }
        self.parse_name_and_firstnames(mrz_parts['Names'])
        self.parse_document_type_and_number(mrz_parts['Document_type_and_number'])
        self.parse_dates_and_sex(mrz_parts['Dates_and_sex'])
           

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
        self.id_elements['Firstname'] = self.id_elements['Firstname'].replace(',', '').replace('-', ' ')
        
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

        delivrary = re.search(r"Date of issue\s+(\d{2} \d{2} \d{4})", self.cni_info)
        self.id_elements['Date_of_issue'] = delivrary.group(1).strip() if height else ""
