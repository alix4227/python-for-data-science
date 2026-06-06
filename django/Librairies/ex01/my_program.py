from path import Path

def main():
    try:
        Path("test").mkdir_p()
        with open("test/test.txt", 'w') as file:
            file.write("hello")
        with open("test/test.txt", 'r') as file:
            print(file.read())
    except Exception as e:
        print(e)
        

if __name__ == "__main__":
    main()
