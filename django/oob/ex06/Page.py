from elements import*


ELEMENTS = ['html', 'head', 'body',
'title', 'meta', 'img', 'table', 'th', 'tr', 'td' , 'ul', 'ol', 'li', 'h1', 'h2', 'p', 'div', 'span', 'hr', 'br']

class Page(Elem):
    def __init__(self, element):
        self.element = element
        self.balises = []


    def check_head_and_title(self):
        head_block = str(self.element.content[0])
        balises = [tag.split('>')[0].lstrip('/') for tag in head_block.split('<')[1:]]
        check_list = ['head', 'title']
        for item in balises:
            if item not in check_list:
                return (False)
        return(True)
        
    def check_body_content(self, body):
        body_block = self.element.content[1]
        if isinstance(body.content, Div):
            self.check_body_content(body.content)
        # balises = [tag.split('>')[0].lstrip('/') for tag in str(body_block).split('<')[1:]]
        # check_list = ['body', 'h1', 'h2', 'div', 'table', 'ul', 'ol', 'span']
        # for item in balises:
        #     if item not in check_list:
        #         return (False)
        return(True)


    def check_body_and_head(self):
        body = head = 0
        if self.balises[1] != 'head':
            return(False)
        for item in self.balises:
            if item == 'head':
                head += 1
            if item == 'body':
                body += 1
        return (body == 2 and head == 2)

    def check_elements(self):
        for item in self.balises:
            if item not in ELEMENTS:
                return (False)
        return(True)

    def checker(self):
        html_page = str(self.element)
        self.balises = [tag.split('>')[0].lstrip('/') for tag in html_page.split('<')[1:]]
        if not self.check_body_and_head():
            return False
        if not self.check_elements():
            return False
        if not self.check_head_and_title():
            return False
        if not self.check_body_content(self.element.content[1]):
            return False
        return True


    def is_valid(self):
        return(self.checker())

            
    def __str__(self):
        return(f'{self.element.content}')

def main(): 
    test = Page(Html( [Head(content=Title(Text('hello'))), Body(Div(Div()))] ))
    print(test.is_valid())


if __name__ == '__main__':
    main()