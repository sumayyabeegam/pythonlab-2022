class Publisher:
    def __init__(self,name="DC"):
        self.__name=name
    def display(self):
        print("Book Details")
        print("name=",self.__name)
class Book(Publisher):
    def __init__(self,name,title,author):
        super().__init__(name)
        self.__title=title
        self.__author=author
    def display(self):
        super().display()
        print("Title=",self.__title)
        print("Author=",self.__author)
class Python(Book):
    def __init__(self,name,title,author,price,pages):
        super().__init__(name,title,author)
        self.__price=price
        self.__pages=pages
    def display(self):
        super().display()
        print("price:",self.__price)
        print("no of pages",self.__pages)
a=Python('DC BOOKS','Taming python by programming','Jeeva Jose',220,248)
a.display()
