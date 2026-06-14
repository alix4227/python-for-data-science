from classes import CNI
import sys
import json
from datetime import datetime
from dateutil.relativedelta import relativedelta


def test(Cni):
    with open('report.txt', 'w') as file:
        
        date_of_issue = Cni.id_elements['Date_of_issue']
        expiration_date = Cni.id_elements['Expiration_date']
        date_of_birth = Cni.id_elements['Date_of_birth']
        date_of_issue_formated = datetime.strptime(date_of_issue, "%d %m %Y").date()
        expiration_date_formated = datetime.strptime(expiration_date, "%d %m %Y").date()
        date_of_birth_formated = datetime.strptime(date_of_birth, "%d %m %Y").date()
        if (date_of_issue_formated < expiration_date_formated) and \
        (date_of_birth_formated < expiration_date_formated) and \
        (date_of_birth_formated < date_of_issue_formated):
            file.write("Dates: Dates' coherence\n")
        else:
            file.write("Dates: Dates' incoherency\n")
        diff = relativedelta(expiration_date_formated, date_of_issue_formated)

        if diff.years == 10 and diff.months == 0 and diff.days == 0:
            file.write("Delay: Dates' coherence\n")
        else:
            file.write("Delay: Dates' incoherency\n")
        print('Test Done! Open report.txt')
                
def main(args):
    if len(args) != 2:
        print('Wrong number of arguments')
        return (1)
    if args[1] != 'ocr.json':
        print('Wrong arguments')
        return(1)
    try:
        Cni = CNI()
        Cni.get_cni_info(args[1])
        Cni.fill_id_elements()
        test(Cni)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Reading error")
    except Exception:
        print("ERROR")
    
if __name__ == "__main__":
    main(sys.argv)