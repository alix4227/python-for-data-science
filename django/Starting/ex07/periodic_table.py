import sys


def main(args):
    dict_elements = {}
    list_elements = []
    keys = ['name', 'atomic_number', 'symbol', 'atomic_mass', 'electron']
    if len(args) != 2:
        return 0
    with open(args[1], 'r') as file:
        data = file.readlines()
        for line in data:
            elements = line.strip().split(',')
            dict_elements = {}
            for i in range(len(elements)):
                if '=' in elements[i]:
                    dict_elements[keys[i]] = elements[i].split('=')[0].strip()
                else:
                    dict_elements[keys[i]] = elements[i].split(':')[1].strip()
            list_elements.append(dict_elements)
    html = "<!DOCTYPE html>\n"
    html += "<html lang=\"en\">\n"
    html += "  <head>\n"
    html += "    <meta charset=\"utf-8\">\n"
    html += "    <title>Periodic Table</title>\n"
    html += "  </head>\n"
    html += "  <body>\n"
    html += "    <table>\n"
    html += "      <tbody>\n"
    i = 0
    while i < 2:
        html += "        <tr>\n"
        j = 0
        k = 0
        while j < 18:
            if j == 0 or j == 17:
                elem = list_elements[k]
                html += "          <td style=\"border: 1px solid black; padding:10px\">\n"
                html += f"            <h4>{elem['name']}</h4>\n"
                html += "            <ul>\n"
                html += f"              <li>{elem['atomic_number']}</li>\n"
                html += f"              <li>{elem['symbol']}</li>\n"
                html += f"              <li>{elem['atomic_mass']}</li>\n"
                html += "            </ul>\n"
                html += "          </td>\n"
                k += 1
            else:
                html += "          <td style=\"border: 1px black; padding:10px\">\n"
                html += "          </td>\n"
            j += 1    
        html += "        </tr>\n"
        i += 2
    while i < len(list_elements):
        html += "        <tr>\n"
        j = 0
        while j < 18 and i + j < len(list_elements):
            elem = list_elements[i + j]
            html += "          <td style=\"border: 1px solid black; padding:10px\">\n"
            html += f"            <h4>{elem['name']}</h4>\n"
            html += "            <ul>\n"
            html += f"              <li>{elem['atomic_number']}</li>\n"
            html += f"              <li>{elem['symbol']}</li>\n"
            html += f"              <li>{elem['atomic_mass']}</li>\n"
            html += "            </ul>\n"
            html += "          </td>\n"
            j += 1
        html += "        </tr>\n"
        i += 18
    html += "      </tbody>\n"
    html += "    </table>\n"
    html += "  </body>\n"
    html += "</html>\n"
    with open("resultat.html", "w") as f:
        f.write(html)
if __name__ == '__main__':
    main(sys.argv)