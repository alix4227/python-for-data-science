import sys, os, re
import settings
#!/usr/bin/env python3

def main(args):
    try:
        if len(args) != 2:
            raise(Exception("Error: Wrong number of args"))
        if not os.path.exists(args[1]):
            raise(Exception("Error: File doesnt exist"))
        if not os.path.isfile(args[1]):
            raise(Exception("Error: Not a file"))
        extension_template = os.path.splitext(args[1])[1]
        if extension_template != '.template':
            raise(TypeError(f'Error: Wrong extension->{extension_template}'))
        with open(args[1], 'r') as file2:
            content2 = file2.read()
        with open("file.html", 'w') as file3:
           result = re.sub(r"\{(\w+)\}", lambda m: getattr(settings, m.group(1), ''), content2)
           file3.write(result)
    except TypeError as e:
        print(str(e))
    except IOError:
        print(f"Error: Cannot read file")
    except Exception as e:
        print(str(e))
    


if __name__ == '__main__':
    main(sys.argv)