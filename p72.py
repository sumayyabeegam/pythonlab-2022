class Flower:
    def getName(self):
        self.name=input('Enter flower name:')
    def display(self):
        if hasattr(self,'petalColor'):
            print('%s %s'%(self.petalColor,self.name))
        else:
            print('Unknown flower')
try:
    f1=Flower()
    f1.getName()
    setattr(f1,'petalColor','red')
    f1.display()
    delattr(f1,'petalColor')
    f1.display()
except Exception as e:
    print(e)    
