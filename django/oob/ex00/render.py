import sys, os, re
#!/usr/bin/env python3

def main(args):
    try:
        content = {}
        with open("settings.py", 'r') as file:
            lines = file.readlines()
            for line in lines:
                key = line.split('=')[0].strip()
                value = line.split('"')[1]
                content[key] = value
        with open(args[1], 'r') as file2:
            content2 = file2.read()
        with open("file.html", 'w') as file3:
           result = re.sub(r"\{(\w+)\}", lambda m: content[m.group(1)], content2)
           file3.write(result)
    except ValueError:
        print(ValueError)
    


if __name__ == '__main__':
    main(sys.argv)