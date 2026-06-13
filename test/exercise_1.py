import json
import re
class CNI:
    def __init__(self):
        Name = self.name
        Firstname = self.firstname
        Date_of_birth = self.date_of_birth
        Document_number = self.document_number
        Expiration_date = self.expiration_date
        Nationality = self.nationality
        Type_of_document = self.type_of_document
        Sex = self.sex
        Place_of_birth = self.place_of_birth
        Height = self.height
    
class Qrcode(CNI):
    def __init__(self):
        super().__init__()




def main():
    with open("qrcode.json", "r") as file:
        Qrcode = json.load(file)
        Qrcode = Qrcode['text'].split(';')
        Id_elements = {"Name": "", "Firstname": "", "Date_of_birth": "", "Document_number": "", 
                       "Expiration_date": "", "Nationality": "", "Type_of_document": "", 
                       "Sex": "", "Place_of_birth": "", "Height": ""}
        for key, value in zip(Id_elements.keys(), Qrcode):
            if key == 'Name':
                value = value.lstrip('E')
            if key == 'Height':
                value = value.strip('S')
            Id_elements[key] = value
    

    with open("ocr.json", "r") as file2:
        Ocr = json.load(file2)
        page1 = Ocr['text']['page_1']
    name = re.search(r"Surname\s+(\w+)", page1)
    firstname = re.search(r"Given names\s+(.+?) SEXE", page1)
    ocr_elements = {
    "Name": name.group(1) if name else None,
    "Firstname": firstname.group(1) if firstname else None
}
    print(ocr_elements)
if __name__ == "__main__":
    main()
