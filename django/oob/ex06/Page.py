from elements import*

ELEMENTS = ['html', 'head', 'body',
'title', 'meta', 'img', 'table', 'th', 'tr', 'td' , 'ul', 'ol', 'li', 'h1', 'h2', 'p', 'div', 'span', 'hr', 'br']

class Page():
    def __init__(self, element):

        self.element = element



    def check_tag(self):
        if (self.element.tag not in ELEMENTS):
            return (False)
        print(self.element.content[0])
        for i in range(len(self.element.content)):
            element_str = str(self.element.content[i])
            print(element_str)
            start = element_str.find('<') + 1
            end = element_str.find('>')
            if element_str[end - 2] == ' ':
                end -= 1 
            tag = element_str[start:end].strip()
            if (tag not in ELEMENTS):
                return (False)
        return (True)
                
    def is_valid(self):
        return(self.check_tag())
            
    def __str__(self):
        return(f'{self.element.content}')

def main(): 
    test = Page(Html( [Head(content=Title()), Body()] ))
    print(test.is_valid())

if __name__ == '__main__':
    main()