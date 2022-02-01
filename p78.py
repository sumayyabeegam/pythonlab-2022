class Person:
    def __init__(self,name='Jack',roll=10):
        self.__name = name
        self.rollno = roll

    def display(self):

        print('Name : ',self.__name)
        print('Rollno: ',self.rollno)
     

class Mark:

    def __init__(self,m=50,c=60):

        self.maths = m
        self.computer=c

    def display(self):

        print('maths mark: ',self.maths)
        print('computer mark: ',self.computer)
        t= self.maths +self.computer
        p=(t//160)*100
        if(p>=50):
            print('Percentage=%f'%p)

class Student(Person,Mark):

    def __init__(self,name,roll,m,c):

        super().__init__(name,roll)

        Mark.__init__(self,m,c)

       

    def display(self):

        super().display()

        Mark.display(self)
       

S=Student("Aksa",10,50,70)
S.display()
           
