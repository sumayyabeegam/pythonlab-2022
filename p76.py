class Time:
   def __init__(self,hour=0,min=0,sec=0):
       self.__hour = hour
       self.min = min
       self.sec = sec
   def show(self):
     print(self.__hour,':',self.min,':',self.sec)
   def __add__(self,other):
    h=self.__hour+other.__hour
    m=self.min+other.min
    s=self.sec+other.sec
    if s==60:
        s=0
        m+=1
    if m==60:
         m=0
         h+=1
    return Time(h,m,s)
t1=Time(4,20,30)
t2=Time(5,30,20)
t1.show()
t2.show()
t3=t1+t2
t3.show()
    
